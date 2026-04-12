"""
FastAPI — Medium Exercises
==========================
Topics: CRUD with in-memory DB, HTTPException, response_model,
        field validation with Pydantic, status codes.

Run:  uvicorn 02-medium:app --reload
Docs: http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title='Task Manager API')


# ---------------------------------------------------------------------------
# Data store (in-memory — resets on server restart)
# ---------------------------------------------------------------------------
tasks: dict[int, dict] = {}
_next_id = 1


# ---------------------------------------------------------------------------
# 1. Pydantic models with validation
# ---------------------------------------------------------------------------
# Define the following models:
#
# TaskCreate — used for POST (input):
#   title: str          — required, min length 1, max length 100
#   description: str    — optional, default ""
#   priority: int       — 1 to 5, default 3
#
# TaskOut — used for GET responses (output):
#   id: int
#   title: str
#   description: str
#   priority: int
#   done: bool
#
# Hint: use Field(min_length=1, max_length=100) and Field(ge=1, le=5)

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. Create — POST /tasks  (status 201)
# ---------------------------------------------------------------------------
# Accept a TaskCreate body.
# Assign an auto-incrementing id and done=False.
# Store in the tasks dict and return the TaskOut.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. List all — GET /tasks
# ---------------------------------------------------------------------------
# Return a list of all tasks as TaskOut.
# Accept an optional query param `priority: int | None = None`.
# If provided, filter tasks to that priority only.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. Get one — GET /tasks/{task_id}
# ---------------------------------------------------------------------------
# Return the TaskOut for the given id.
# Raise 404 with detail "Task not found" if it doesn't exist.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 5. Update — PUT /tasks/{task_id}
# ---------------------------------------------------------------------------
# Accept a TaskCreate body.
# Replace the task's fields (keep the same id and done status).
# Return the updated TaskOut.
# Raise 404 if not found.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 6. Mark done — PATCH /tasks/{task_id}/done
# ---------------------------------------------------------------------------
# Toggle the 'done' field to True.
# Return the updated TaskOut.
# Raise 404 if not found.
# Raise 400 with detail "Task already done" if it's already done.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 7. Delete — DELETE /tasks/{task_id}  (status 204)
# ---------------------------------------------------------------------------
# Remove the task from the store.
# Return None (no body — 204 No Content).
# Raise 404 if not found.

# YOUR CODE HERE
