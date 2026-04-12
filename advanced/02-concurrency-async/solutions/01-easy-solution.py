# ============================================================
# advanced/02-concurrency-async/solutions/01-easy-solution.py
# ============================================================

import threading
import asyncio
import time
import random

# ----------------------------------------------------------
# Exercise 1 — Basic threading
# ----------------------------------------------------------
def thread_worker(number):
    delay = random.uniform(0.1, 0.5)
    print(f"Thread {number} starting")
    time.sleep(delay)
    print(f"Thread {number} done (slept {delay:.2f}s)")

print("--- Basic threading ---")
threads = [threading.Thread(target=thread_worker, args=(i,)) for i in range(1, 6)]
for t in threads: t.start()
for t in threads: t.join()
print("All threads done\n")


# ----------------------------------------------------------
# Exercise 2 — Thread with return value via shared list
# ----------------------------------------------------------
def threaded_square(n, results, index):
    results[index] = n ** 2

print("--- Thread return values ---")
numbers = [1, 2, 3, 4, 5]
results = [None] * len(numbers)
threads = [
    threading.Thread(target=threaded_square, args=(n, results, i))
    for i, n in enumerate(numbers)
]
for t in threads: t.start()
for t in threads: t.join()
print(results)   # [1, 4, 9, 16, 25]


# ----------------------------------------------------------
# Exercise 3 — asyncio sequential
# ----------------------------------------------------------
async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

async def main_sequential():
    start = time.perf_counter()
    await greet("Alice", 0.5)
    await greet("Bob", 1.0)
    await greet("Carol", 0.3)
    print(f"Sequential total: {time.perf_counter() - start:.2f}s\n")  # ~1.8s

print("--- asyncio sequential ---")
asyncio.run(main_sequential())


# ----------------------------------------------------------
# Exercise 4 — asyncio.gather (concurrent)
# ----------------------------------------------------------
async def main_concurrent():
    start = time.perf_counter()
    await asyncio.gather(
        greet("Alice", 0.5),
        greet("Bob",   1.0),
        greet("Carol", 0.3),
    )
    print(f"Concurrent total: {time.perf_counter() - start:.2f}s")  # ~1.0s

print("--- asyncio gather (concurrent) ---")
asyncio.run(main_concurrent())
