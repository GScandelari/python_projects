# ============================================================
# advanced/02-concurrency-async/solutions/03-challenge-solution.py
# ============================================================

import asyncio
import threading
import time
import random

# ----------------------------------------------------------
# Exercise 1 — Async rate-limited batch processor
# ----------------------------------------------------------
async def batch_process(items, worker, max_concurrent):
    sem = asyncio.Semaphore(max_concurrent)

    async def limited_worker(item):
        async with sem:
            return await worker(item)

    return await asyncio.gather(*[limited_worker(item) for item in items])

async def simulate_work(item):
    delay = random.uniform(0.1, 0.5)
    print(f"  Start: {item}")
    await asyncio.sleep(delay)
    print(f"  Done:  {item} ({delay:.2f}s)")
    return item

async def main_batch():
    random.seed(42)
    items = [f"job_{i}" for i in range(1, 11)]
    start = time.perf_counter()
    results = await batch_process(items, simulate_work, max_concurrent=3)
    print(f"  All done in {time.perf_counter() - start:.2f}s")
    return results

print("--- Async batch processor (max 3 concurrent) ---")
asyncio.run(main_batch())


# ----------------------------------------------------------
# Exercise 2 — Thread-safe EventBus
# ----------------------------------------------------------
class EventBus:
    def __init__(self):
        self._subscribers = {}
        self._lock = threading.Lock()

    def subscribe(self, event, callback):
        with self._lock:
            self._subscribers.setdefault(event, []).append(callback)

    def publish(self, event, data=None):
        with self._lock:
            callbacks = list(self._subscribers.get(event, []))
        for cb in callbacks:
            cb(data)

    def publish_async(self, event, data, delay):
        def _delayed():
            time.sleep(delay)
            self.publish(event, data)
        t = threading.Thread(target=_delayed, daemon=True)
        t.start()
        return t

bus = EventBus()
bus.subscribe("sale", lambda d: print(f"  Logger: sale={d}"))
bus.subscribe("sale", lambda d: print(f"  Analytics: revenue={d.get('amount', 0):.2f}"))

print("\n--- EventBus ---")
bus.publish("sale", {"product": "Notebook", "amount": 2500.0})

t = bus.publish_async("sale", {"product": "Mouse", "amount": 89.90}, delay=0.2)
t.join()   # wait for delayed event


# ----------------------------------------------------------
# Exercise 3 — Async pipeline with back-pressure
# ----------------------------------------------------------
async def stage_generator(queue_out):
    for i in range(1, 11):
        await asyncio.sleep(0.1)
        await queue_out.put(i)   # blocks if queue is full (back-pressure)
        print(f"  [Gen] produced {i}")
    await queue_out.put(None)    # sentinel

async def stage_transformer(queue_in, queue_out):
    while True:
        item = await queue_in.get()
        if item is None:
            await queue_out.put(None)
            return
        await asyncio.sleep(0.05)
        result = item * 2
        await queue_out.put(result)
        print(f"  [Transform] {item} → {result}")

async def stage_sink(queue_in):
    while True:
        item = await queue_in.get()
        if item is None:
            return
        print(f"  [Sink] output: {item}")

async def main_pipeline():
    q1 = asyncio.Queue(maxsize=3)
    q2 = asyncio.Queue(maxsize=3)
    start = time.perf_counter()
    await asyncio.gather(
        stage_generator(q1),
        stage_transformer(q1, q2),
        stage_sink(q2),
    )
    print(f"  Pipeline done in {time.perf_counter() - start:.2f}s")

print("\n--- Async pipeline with back-pressure ---")
asyncio.run(main_pipeline())
