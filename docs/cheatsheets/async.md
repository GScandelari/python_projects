# Concurrency & Async — Cheat Sheet

## Decision Guide

```
Task is I/O-bound (network, file, DB)?
├── Many simultaneous connections → asyncio
└── Simpler / third-party blocking libs → threading

Task is CPU-bound (computation, parsing)?
└── multiprocessing
```

---

## threading

```python
import threading, time

def worker(name, delay):
    time.sleep(delay)
    print(f'{name} done')

# Basic thread
t = threading.Thread(target=worker, args=('Alpha', 0.3))
t.start()
t.join()   # wait for completion

# Thread pool (preferred over raw threads)
from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=4) as ex:
    futures = {ex.submit(worker, f'job-{i}', 0.1): i for i in range(8)}
    for f in as_completed(futures):
        result = f.result()   # raises if worker raised

# Thread safety
lock = threading.Lock()
with lock:
    shared_counter += 1       # atomic

# Thread-local storage
local = threading.local()
local.user_id = 42            # unique per thread
```

---

## asyncio

```python
import asyncio

# Coroutine — defined with async def, called with await
async def fetch(url: str, delay: float) -> str:
    await asyncio.sleep(delay)   # non-blocking pause
    return f'data from {url}'

# Entry point
asyncio.run(main())

# Run concurrently (gather = fan-out)
results = await asyncio.gather(
    fetch('api-1', 0.3),
    fetch('api-2', 0.2),
    fetch('api-3', 0.4),
)
# total time ≈ max(0.3, 0.2, 0.4) = 0.4s

# Create task (schedule without awaiting immediately)
task = asyncio.create_task(fetch('bg', 1.0))
# do other work...
result = await task

# Timeout
try:
    result = await asyncio.wait_for(fetch('slow', 10), timeout=2.0)
except asyncio.TimeoutError:
    print('Too slow')

# Semaphore — limit concurrency
sem = asyncio.Semaphore(5)
async def limited():
    async with sem:
        await do_work()

# Queue — producer/consumer
q = asyncio.Queue(maxsize=10)
await q.put(item)       # blocks if full
item = await q.get()    # blocks if empty
q.task_done()

# asyncio.gather vs asyncio.wait
# gather: all succeed or all cancelled on first exception
# wait:   more control — FIRST_COMPLETED, FIRST_EXCEPTION, ALL_COMPLETED
done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
```

---

## multiprocessing

```python
from multiprocessing import Pool, Process, Queue
import math

def heavy(n):
    return sum(math.sqrt(i) for i in range(n))

# Pool.map — parallel map
if __name__ == '__main__':    # required on Windows
    with Pool(processes=4) as pool:
        results = pool.map(heavy, [500_000, 1_000_000, 750_000])

    # starmap — multiple args
    results = pool.starmap(pow, [(2, 8), (3, 4), (10, 2)])

# Process — manual
p = Process(target=heavy, args=(1_000_000,))
p.start()
p.join()

# Inter-process communication
q = Queue()
q.put({'key': 'value'})
data = q.get()
```

---

## Common Pitfalls

| Pitfall | Fix |
|---|---|
| `time.sleep()` in async code | Use `await asyncio.sleep()` |
| Modifying shared list without a lock | Use `threading.Lock` or `Queue` |
| Running `asyncio.run()` inside a running loop (Jupyter) | Use `await coro()` directly or `nest_asyncio` |
| `multiprocessing` without `if __name__ == '__main__':` | Always guard on Windows |
| Forgetting `await` on a coroutine | The coroutine never runs — Python warns about this |
| Using CPU-bound work in async | Move to `loop.run_in_executor()` with a thread/process pool |

---

## Quick Reference

```python
# --- threading ---
Thread(target=fn, args=()).start() / .join()
with Lock(): ...
with ThreadPoolExecutor(max_workers=N) as ex:
    futures = [ex.submit(fn, arg) for arg in items]
    results = [f.result() for f in as_completed(futures)]

# --- asyncio ---
asyncio.run(main())
await asyncio.gather(*coros)
await asyncio.wait_for(coro, timeout=N)
asyncio.create_task(coro)
async with asyncio.Semaphore(N): ...
await queue.put(x) / await queue.get()

# --- multiprocessing ---
with Pool(N) as p: p.map(fn, items)
Process(target=fn, args=()).start() / .join()
```
