# Concurrency & Async

Python offers three concurrency models. Choosing the right one depends on whether your bottleneck is I/O or CPU.

| Model | Best for | Key tools |
|---|---|---|
| `threading` | I/O-bound tasks (network, file) | `Thread`, `Lock`, `ThreadPoolExecutor` |
| `asyncio` | Many concurrent I/O tasks | `async/await`, `Task`, `gather` |
| `multiprocessing` | CPU-bound tasks (computation) | `Process`, `Pool` |

## Table of Contents

- [Threading](#1-threading)
- [Thread Safety — Lock](#2-thread-safety--lock)
- [ThreadPoolExecutor](#3-threadpoolexecutor)
- [asyncio basics](#4-asyncio-basics)
- [async/await patterns](#5-asyncawait-patterns)
- [asyncio.gather — concurrent tasks](#6-asynciogather--concurrent-tasks)
- [multiprocessing basics](#7-multiprocessing-basics)
- [Quick Reference](#quick-reference)
- [What's Next](#whats-next)

---

## 1. Threading

Threads share memory and run concurrently. Due to Python's GIL, only one thread runs Python bytecode at a time — but threads still improve I/O-bound performance since I/O releases the GIL.

```python
import threading
import time

def worker(name, delay):
    print(f"{name} starting")
    time.sleep(delay)         # releases GIL → other threads run
    print(f"{name} done")

t1 = threading.Thread(target=worker, args=("A", 2))
t2 = threading.Thread(target=worker, args=("B", 1))

t1.start()
t2.start()
t1.join()   # wait for t1 to finish
t2.join()
print("All done")
# A starting → B starting → B done → A done (concurrent!)
```

---

## 2. Thread Safety — Lock

Shared state requires protection. Use `threading.Lock` to prevent race conditions:

```python
import threading

counter = 0
lock = threading.Lock()

def increment(n):
    global counter
    for _ in range(n):
        with lock:          # only one thread at a time
            counter += 1

threads = [threading.Thread(target=increment, args=(100_000,)) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)   # always 500000 (without lock it varies)
```

---

## 3. ThreadPoolExecutor

`concurrent.futures.ThreadPoolExecutor` manages a pool of threads and returns `Future` objects:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def fetch(url):
    time.sleep(0.5)   # simulate network I/O
    return f"Data from {url}"

urls = ["url1", "url2", "url3", "url4"]

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(fetch, url): url for url in urls}
    for future in as_completed(futures):
        url = futures[future]
        print(f"{url}: {future.result()}")
```

---

## 4. asyncio basics

`asyncio` is single-threaded but switches between tasks at every `await` point — ideal for many concurrent I/O operations:

```python
import asyncio

async def greet(name, delay):
    await asyncio.sleep(delay)   # suspend this coroutine, run others
    print(f"Hello, {name}!")

async def main():
    await greet("Alice", 2)
    await greet("Bob", 1)        # sequential — Alice first, then Bob

asyncio.run(main())
```

---

## 5. async/await patterns

`async def` defines a **coroutine**. `await` suspends it until the awaitable completes:

```python
import asyncio

async def fetch_data(source, delay):
    print(f"Fetching from {source}...")
    await asyncio.sleep(delay)
    return {"source": source, "data": f"result_{source}"}

async def process(source, delay):
    data = await fetch_data(source, delay)
    print(f"Processed: {data}")
    return data

async def main():
    result = await process("API", 1)
    print(result)

asyncio.run(main())
```

---

## 6. asyncio.gather — concurrent tasks

`gather()` runs coroutines **concurrently** — total time ≈ max individual time (not sum):

```python
import asyncio, time

async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"{name}: done in {delay}s"

async def main():
    start = time.perf_counter()

    # Sequential: 1 + 2 + 3 = 6 seconds
    # results = [await fetch("A",1), await fetch("B",2), await fetch("C",3)]

    # Concurrent: max(1, 2, 3) = 3 seconds
    results = await asyncio.gather(
        fetch("A", 1),
        fetch("B", 2),
        fetch("C", 3),
    )

    elapsed = time.perf_counter() - start
    for r in results:
        print(r)
    print(f"Total: {elapsed:.2f}s")   # ~3.00s

asyncio.run(main())
```

---

## 7. multiprocessing basics

`multiprocessing` spawns real OS processes — each with its own GIL. True parallelism for CPU-bound work:

```python
from multiprocessing import Pool
import math

def heavy_compute(n):
    return sum(math.sqrt(i) for i in range(n))

if __name__ == "__main__":   # required on Windows
    numbers = [1_000_000, 2_000_000, 3_000_000, 4_000_000]

    with Pool(processes=4) as pool:
        results = pool.map(heavy_compute, numbers)

    print(results)
```

---

## Quick Reference

```python
# Threading
t = threading.Thread(target=func, args=(a, b))
t.start(); t.join()
with threading.Lock(): ...   # mutual exclusion

# ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=N) as ex:
    futures = [ex.submit(func, arg) for arg in items]
    results = [f.result() for f in futures]

# asyncio
async def coro(): await something()
asyncio.run(coro())                    # entry point
await asyncio.gather(c1(), c2())       # concurrent
task = asyncio.create_task(coro())     # schedule without awaiting now
await asyncio.wait_for(coro(), timeout=5)

# multiprocessing
with Pool(N) as p:
    results = p.map(func, items)       # parallel map
```

---

## What's Next

Try the exercises in [`exercises/`](./exercises/) — build thread-safe counters, async pipelines, and concurrent I/O simulations.

Next concept: [`03-testing`](../03-testing/)
