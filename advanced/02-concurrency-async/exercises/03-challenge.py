# ============================================================
# advanced/02-concurrency-async/exercises/03-challenge.py
# Topic: Concurrency — advanced async and threading patterns
# Difficulty: Challenge
# ============================================================

import asyncio
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Exercise 1 — Async rate-limited batch processor
# -------------------------------------------------
# Write an async function batch_process(items, worker, max_concurrent)
# that processes `items` using the async `worker` coroutine, but
# limits concurrent execution to `max_concurrent` at a time.
# Use asyncio.Semaphore for the rate limiting.
#
# Demonstrate with 10 items and max_concurrent=3. Each item
# simulates work with asyncio.sleep(random 0.1-0.5s).
# Print each item when it starts and when it completes.
# Print total elapsed time at the end.
#
# Expected: items process in batches of 3, total ~2s not ~5s

import random
# Write your code here


# Exercise 2 — Thread-safe event bus
# ------------------------------------
# Build a simple EventBus that works safely across threads:
#
#   EventBus:
#     subscribe(event, callback) — register a callback for an event
#     publish(event, data)       — call all callbacks for that event
#                                  (thread-safe, can be called from any thread)
#     publish_async(event, data, delay) — publish after `delay` seconds
#                                         from a background thread
#
# Demonstrate:
#   - Subscribe 2 handlers to "sale" event
#   - Publish from the main thread immediately
#   - Schedule a delayed publish from a background thread
#   - Wait for all events to fire

# Write your code here


# Exercise 3 — Async pipeline with back-pressure
# ------------------------------------------------
# Build a 3-stage async pipeline:
#
#   Stage 1 — generator: produces 10 items (integers 1-10),
#             one every 0.1s, puts them into queue_1
#   Stage 2 — transformer: reads from queue_1, multiplies by 2,
#             puts into queue_2 (simulates 0.05s work per item)
#   Stage 3 — sink: reads from queue_2, prints the result
#
# Use asyncio.Queue(maxsize=3) for back-pressure (stage 1 blocks
# when the queue is full, naturally slowing production).
# Use None sentinels to signal end-of-stream.
# Print total elapsed time at the end.
#
# Expected: items flow through all 3 stages, output shows
# values 2, 4, 6, ..., 20 in order.

# Write your code here
