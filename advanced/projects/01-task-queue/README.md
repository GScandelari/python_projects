# Capstone Project 1 — Task Queue

A lightweight in-process task queue that runs jobs in background threads, with retry logic, priority support, and a live status dashboard.

## Concepts Used

| Concept | Where |
|---|---|
| `threading` + `Queue` | Worker pool execution |
| Decorators | `@task`, `@retry` wrappers |
| Generators | Lazy job creation, result streaming |
| Design Patterns | Observer (progress events), Strategy (retry policy) |

## Features

- Submit callable tasks with priority
- Configurable worker pool size
- Automatic retry with exponential back-off
- Per-task status tracking (pending → running → done/failed)
- Event callbacks (on_complete, on_failure, on_retry)

## Structure

```
01-task-queue/
  main.py       ← skeleton to implement
  solution.py   ← full reference implementation
```

## How to Run

```bash
python solution.py
```

## Learning Goals

After completing this project you should be able to:
- Use `threading.Thread` and `queue.PriorityQueue` together
- Build a decorator that registers a function as a task
- Implement retry with exponential back-off
- Notify external listeners of task lifecycle events
