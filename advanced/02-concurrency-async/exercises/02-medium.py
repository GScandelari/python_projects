# ============================================================
# advanced/02-concurrency-async/exercises/02-medium.py
# Topic: Concurrency — thread safety, executor, async patterns
# Difficulty: Medium
# ============================================================

import threading
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Exercise 1 — Thread-safe counter
# ---------------------------------
# Write a class SafeCounter with:
#   - A private _count attribute starting at 0
#   - Methods increment() and decrement()
#   - A value property returning _count
#   - Thread safety using threading.Lock
#
# Verify it by running 10 threads that each call increment()
# 10_000 times. The final count should always be 100_000.
#
# Expected:
#   counter.value == 100000   (always, never varies)

# Write your code here


# Exercise 2 — ThreadPoolExecutor with results
# ----------------------------------------------
# Simulate fetching data from 8 "endpoints". Each fetch takes
# between 0.1 and 0.5 seconds (use random.uniform + time.sleep).
# Use ThreadPoolExecutor(max_workers=4) to run them concurrently.
# Print each result as it completes (use as_completed).
# Print the total elapsed time at the end.
#
# Expected:
#   endpoint_3: result in 0.12s
#   endpoint_7: result in 0.18s
#   ...
#   Total: ~0.5s (not 3-4s)

import random
# Write your code here


# Exercise 3 — Async producer/consumer
# --------------------------------------
# Implement an async producer/consumer using asyncio.Queue:
#
#   producer(queue, items) — puts each item into the queue,
#                             simulating work with a small random sleep
#   consumer(queue, name)  — gets items from the queue and processes
#                             them until it receives a None sentinel value
#
# Run 1 producer and 2 consumers concurrently with asyncio.gather().
# Feed items: ["task_1", "task_2", ..., "task_6"]
#
# Expected (order varies):
#   Producer: put task_1
#   Consumer A: processed task_1
#   Producer: put task_2
#   Consumer B: processed task_2
#   ...

# Write your code here


# Exercise 4 — asyncio timeout
# ------------------------------
# Write an async function slow_operation(name, delay) that
# simulates a slow task. Use asyncio.wait_for to run it with
# a 1-second timeout. Handle asyncio.TimeoutError gracefully.
#
# Run three tasks:
#   slow_operation("fast",   0.5)  → completes
#   slow_operation("medium", 1.0)  → completes at the edge
#   slow_operation("slow",   2.0)  → times out
#
# Expected:
#   fast: completed in 0.5s
#   medium: completed in 1.0s
#   slow: timed out after 1s

# Write your code here
