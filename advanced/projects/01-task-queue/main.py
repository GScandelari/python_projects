# ============================================================
# advanced/projects/01-task-queue/main.py
# Capstone: Task Queue — skeleton
# ============================================================
#
# Build a lightweight task queue with:
#
# 1. TaskQueue class
#    - __init__(workers=2) — create a thread pool
#    - submit(func, *args, priority=0, **kwargs) — enqueue a task
#    - on(event, callback) — register event listeners
#       events: "complete", "failure", "retry"
#    - start() / stop() — lifecycle control
#    - status() → dict of {task_id: status_str}
#
# 2. @task decorator
#    - Marks a function as a task (submits it to a default queue)
#    - Usage: @task  or  @task(priority=1)
#
# 3. @retry(times=3, backoff=1.5) decorator
#    - Retries a function on exception
#    - Waits backoff^attempt seconds between retries
#
# 4. Demo
#    - Create a queue with 3 workers
#    - Submit 8 jobs of varying duration and failure probability
#    - Print live progress via event callbacks
#    - Stop the queue gracefully after all jobs complete

import threading
import queue
import time
import random

# Write your implementation here


if __name__ == "__main__":
    pass   # replace with your demo
