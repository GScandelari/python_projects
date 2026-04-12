# ============================================================
# advanced/projects/01-task-queue/solution.py
# ============================================================

import threading
import queue
import time
import random
import functools
import uuid

# ----------------------------------------------------------
# retry decorator with exponential back-off
# ----------------------------------------------------------
def retry(times=3, backoff=1.5, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            delay = 1.0
            last_exc = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exc = e
                    if attempt < times:
                        time.sleep(delay)
                        delay *= backoff
            raise last_exc
        return wrapper
    return decorator


# ----------------------------------------------------------
# TaskQueue
# ----------------------------------------------------------
class TaskQueue:
    def __init__(self, workers=2):
        self._queue   = queue.PriorityQueue()
        self._workers = workers
        self._threads = []
        self._status  = {}          # task_id → status string
        self._lock    = threading.Lock()
        self._listeners = {}        # event → [callbacks]
        self._running = False

    # ---- lifecycle ----

    def start(self):
        self._running = True
        for _ in range(self._workers):
            t = threading.Thread(target=self._worker, daemon=True)
            t.start()
            self._threads.append(t)

    def stop(self, wait=True):
        if wait:
            self._queue.join()
        self._running = False
        for _ in self._threads:
            self._queue.put((0, None, None, None))   # sentinel

    # ---- submission ----

    def submit(self, func, *args, priority=0, **kwargs):
        task_id = str(uuid.uuid4())[:8]
        with self._lock:
            self._status[task_id] = "pending"
        self._queue.put((priority, task_id, func, (args, kwargs)))
        return task_id

    # ---- events ----

    def on(self, event, callback):
        self._listeners.setdefault(event, []).append(callback)

    def _emit(self, event, **data):
        for cb in self._listeners.get(event, []):
            cb(**data)

    # ---- status ----

    def status(self):
        with self._lock:
            return dict(self._status)

    # ---- internal worker ----

    def _worker(self):
        while True:
            item = self._queue.get()
            priority, task_id, func, call = item
            if func is None:   # sentinel
                self._queue.task_done()
                break
            args, kwargs = call
            with self._lock:
                self._status[task_id] = "running"
            try:
                result = func(*args, **kwargs)
                with self._lock:
                    self._status[task_id] = "done"
                self._emit("complete", task_id=task_id, result=result)
            except Exception as e:
                with self._lock:
                    self._status[task_id] = "failed"
                self._emit("failure", task_id=task_id, error=str(e))
            finally:
                self._queue.task_done()


# ----------------------------------------------------------
# @task decorator
# ----------------------------------------------------------
_default_queue = TaskQueue(workers=3)

def task(func=None, *, priority=0):
    if func is None:
        return lambda f: task(f, priority=priority)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return _default_queue.submit(func, *args, priority=priority, **kwargs)
    return wrapper


# ----------------------------------------------------------
# Demo
# ----------------------------------------------------------
if __name__ == "__main__":
    random.seed(42)

    tq = TaskQueue(workers=3)

    tq.on("complete", lambda task_id, result:
          print(f"  [DONE]   {task_id} → {result}"))
    tq.on("failure",  lambda task_id, error:
          print(f"  [FAIL]   {task_id} ✗ {error}"))

    tq.start()

    def job(name, delay, fail_rate=0.0):
        time.sleep(delay)
        if random.random() < fail_rate:
            raise RuntimeError(f"{name} randomly failed")
        return f"{name} finished"

    jobs = [
        ("alpha",   0.3, 0.0),
        ("beta",    0.5, 0.3),
        ("gamma",   0.2, 0.0),
        ("delta",   0.7, 0.5),
        ("epsilon", 0.1, 0.0),
        ("zeta",    0.4, 0.2),
        ("eta",     0.6, 0.0),
        ("theta",   0.3, 0.4),
    ]

    ids = []
    for name, delay, fail_rate in jobs:
        tid = tq.submit(job, name, delay, fail_rate=fail_rate, priority=0)
        ids.append(tid)
        print(f"  [SUBMIT] {tid} → {name}")

    tq.stop(wait=True)

    print("\n--- Final status ---")
    for tid, status in tq.status().items():
        print(f"  {tid}: {status}")
