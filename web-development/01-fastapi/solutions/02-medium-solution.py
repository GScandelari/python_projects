"""
FastAPI — Medium Solutions

Run:  uvicorn 02-medium-solution:app --reload
Docs: http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title='Task Manager API')

tasks: dict[int, dict] = {}
_next_id = 1


# ---------------------------------------------------------------------------
# 1. Pydantic models with validation
# ---------------------------------------------------------------------------
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(default='')
    priority: int = Field(default=3, ge=1, le=5)

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    priority: int
    done: bool


# ---------------------------------------------------------------------------
# 2. Create — POST /tasks
# ---------------------------------------------------------------------------
@app.post('/tasks', response_model=TaskOut, status_code=201)
def create_task(task: TaskCreate):
    global _next_id
    record = {
        'id': _next_id,
        **task.model_dump(),
        'done': False,
    }
    tasks[_next_id] = record
    _next_id += 1
    return record


# ---------------------------------------------------------------------------
# 3. List all — GET /tasks
# ---------------------------------------------------------------------------
@app.get('/tasks', response_model=list[TaskOut])
def list_tasks(priority: Optional[int] = None):
    result = list(tasks.values())
    if priority is not None:
        result = [t for t in result if t['priority'] == priority]
    return result


# ---------------------------------------------------------------------------
# 4. Get one — GET /tasks/{task_id}
# ---------------------------------------------------------------------------
@app.get('/tasks/{task_id}', response_model=TaskOut)
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail='Task not found')
    return tasks[task_id]


# ---------------------------------------------------------------------------
# 5. Update — PUT /tasks/{task_id}
# ---------------------------------------------------------------------------
@app.put('/tasks/{task_id}', response_model=TaskOut)
def update_task(task_id: int, task: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail='Task not found')
    tasks[task_id].update(task.model_dump())
    return tasks[task_id]


# ---------------------------------------------------------------------------
# 6. Mark done — PATCH /tasks/{task_id}/done
# ---------------------------------------------------------------------------
@app.patch('/tasks/{task_id}/done', response_model=TaskOut)
def mark_done(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail='Task not found')
    if tasks[task_id]['done']:
        raise HTTPException(status_code=400, detail='Task already done')
    tasks[task_id]['done'] = True
    return tasks[task_id]


# ---------------------------------------------------------------------------
# 7. Delete — DELETE /tasks/{task_id}
# ---------------------------------------------------------------------------
@app.delete('/tasks/{task_id}', status_code=204)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail='Task not found')
    del tasks[task_id]
