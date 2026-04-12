# Solutions Guide — 02-concurrency-async

---

## Key Concepts by Exercise

### Easy 1 — Basic threading
Threads start with `.start()` and the caller blocks on `.join()`. Running all starts before all joins allows true concurrency. `random.uniform(0.1, 0.5)` simulates variable I/O time.

### Easy 2 — Return values via shared list
Python threads can't return values directly. The pattern of pre-allocating a `results` list and writing by index is thread-safe as long as each thread writes to a **different** index (no race condition).

### Easy 3 vs Easy 4 — Sequential vs concurrent
Sequential `await` waits for each coroutine to finish before starting the next — total ≈ sum of delays. `asyncio.gather()` starts all coroutines concurrently — total ≈ max of delays.

---

### Medium 1 — SafeCounter
`with self._lock` is the cleanest way to acquire/release a Lock. The context manager guarantees release even if an exception occurs. Without the lock, 10 threads × 10,000 increments would produce a result anywhere below 100,000 due to race conditions on the read-modify-write cycle.

### Medium 2 — ThreadPoolExecutor
`as_completed()` yields futures as they finish, not in submission order — ideal for printing progress. The context manager (`with ThreadPoolExecutor(...)`) calls `shutdown(wait=True)` automatically on exit.

### Medium 3 — Producer/consumer with Queue
`asyncio.Queue` is the standard async handoff mechanism. Sending one `None` per consumer avoids one consumer consuming two sentinels. `task_done()` + `queue.join()` can be used for stricter completion tracking (not required here).

### Medium 4 — wait_for
`asyncio.wait_for(coro, timeout)` raises `asyncio.TimeoutError` if the coroutine doesn't finish in time. It also cancels the underlying task — resources are cleaned up.

---

### Challenge 1 — Semaphore rate limiting
`asyncio.Semaphore(n)` allows at most `n` coroutines inside `async with sem` at once. Wrapping the worker in `limited_worker` and gathering all of them lets `asyncio` schedule them — the semaphore acts as the concurrency gate.

### Challenge 2 — Thread-safe EventBus
The Lock protects the subscribers dict during reads **and** writes. We copy the callback list before releasing the lock so that callbacks can themselves subscribe/unsubscribe without deadlock. `daemon=True` means the background thread won't block program exit.

### Challenge 3 — Back-pressure pipeline
`asyncio.Queue(maxsize=3)` causes `await queue.put(item)` to suspend when full — naturally slowing the producer. This prevents unbounded memory growth when a slow consumer can't keep up. `None` sentinels propagate end-of-stream through each stage.

---

## Concurrency Model Decision Guide

| Situation | Use |
|---|---|
| Many network requests / API calls | `asyncio` + `gather` |
| CPU-intensive computation | `multiprocessing.Pool` |
| Calling blocking (non-async) I/O libs | `ThreadPoolExecutor` |
| Need back-pressure between stages | `asyncio.Queue(maxsize=N)` |
| Limit concurrent access to a resource | `asyncio.Semaphore` or `threading.Lock` |
| Share data between threads safely | `threading.Lock` + plain dict/list |
