# ============================================================
# advanced/02-concurrency-async/solutions/02-medium-solution.py
# ============================================================

import threading
import asyncio
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# ----------------------------------------------------------
# Exercise 1 — Thread-safe counter
# ----------------------------------------------------------
class SafeCounter:
    def __init__(self):
        self._count = 0
        self._lock  = threading.Lock()

    def increment(self):
        with self._lock:
            self._count += 1

    def decrement(self):
        with self._lock:
            self._count -= 1

    @property
    def value(self):
        return self._count

print("--- SafeCounter ---")
counter = SafeCounter()
threads = [threading.Thread(target=lambda: [counter.increment() for _ in range(10_000)])
           for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Final count: {counter.value}")   # always 100000


# ----------------------------------------------------------
# Exercise 2 — ThreadPoolExecutor with as_completed
# ----------------------------------------------------------
def fetch_endpoint(endpoint):
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)
    return endpoint, delay

random.seed(7)
endpoints = [f"endpoint_{i}" for i in range(1, 9)]

print("\n--- ThreadPoolExecutor ---")
start = time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(fetch_endpoint, ep): ep for ep in endpoints}
    for future in as_completed(futures):
        ep, delay = future.result()
        print(f"  {ep}: done in {delay:.2f}s")
print(f"  Total: {time.perf_counter() - start:.2f}s")


# ----------------------------------------------------------
# Exercise 3 — Async producer/consumer
# ----------------------------------------------------------
async def producer(queue, items):
    for item in items:
        await asyncio.sleep(random.uniform(0.05, 0.15))
        await queue.put(item)
        print(f"  Producer: put {item}")
    # send one None sentinel per consumer
    await queue.put(None)
    await queue.put(None)

async def consumer(queue, name):
    while True:
        item = await queue.get()
        if item is None:
            break
        await asyncio.sleep(random.uniform(0.02, 0.08))
        print(f"  Consumer {name}: processed {item}")
        queue.task_done()

async def main_pc():
    random.seed(1)
    queue = asyncio.Queue()
    items = [f"task_{i}" for i in range(1, 7)]
    await asyncio.gather(
        producer(queue, items),
        consumer(queue, "A"),
        consumer(queue, "B"),
    )

print("\n--- Producer/Consumer ---")
asyncio.run(main_pc())


# ----------------------------------------------------------
# Exercise 4 — asyncio.wait_for with timeout
# ----------------------------------------------------------
async def slow_operation(name, delay):
    await asyncio.sleep(delay)
    return f"{name}: completed"

async def main_timeout():
    tasks = [("fast", 0.5), ("medium", 1.0), ("slow", 2.0)]
    start = time.perf_counter()
    for name, delay in tasks:
        try:
            result = await asyncio.wait_for(slow_operation(name, delay), timeout=1.1)
            print(f"  {result} in {time.perf_counter()-start:.2f}s")
        except asyncio.TimeoutError:
            print(f"  {name}: timed out after 1.1s")

print("\n--- asyncio timeout ---")
asyncio.run(main_timeout())
