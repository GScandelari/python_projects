# FastAPI

A modern, high-performance web framework for building APIs with Python type hints.

**Install:** `pip install fastapi uvicorn[standard]`

**Run:** `uvicorn main:app --reload`

**Docs:** http://127.0.0.1:8000/docs (Swagger UI auto-generated)

---

## 1. Hello World

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello, World!'}
```

Run with `uvicorn main:app --reload` and open http://127.0.0.1:8000.

## 2. Path and Query Parameters

```python
@app.get('/items/{item_id}')
def read_item(item_id: int, q: str | None = None):
    return {'item_id': item_id, 'q': q}

# GET /items/42?q=search
# → {"item_id": 42, "q": "search"}
```

Type annotations are enforced — FastAPI returns a 422 error if `item_id` is not an integer.

## 3. Request Body with Pydantic

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post('/items/', status_code=201)
def create_item(item: Item):
    return item
```

FastAPI parses the JSON body, validates it, and passes a typed `Item` object to your function.

## 4. Response Models

```python
class ItemOut(BaseModel):
    id: int
    name: str
    # price is intentionally excluded from the response

@app.get('/items/{item_id}', response_model=ItemOut)
def get_item(item_id: int):
    return {'id': item_id, 'name': 'Widget', 'price': 9.99}
    # price is filtered out by the response_model
```

## 5. HTTP Exceptions

```python
from fastapi import HTTPException

fake_db = {1: 'Apple', 2: 'Banana'}

@app.get('/fruits/{fruit_id}')
def get_fruit(fruit_id: int):
    if fruit_id not in fake_db:
        raise HTTPException(status_code=404, detail='Fruit not found')
    return {'name': fake_db[fruit_id]}
```

## 6. Dependency Injection

```python
from fastapi import Depends

def get_current_user(token: str = 'anonymous'):
    return {'user': token}

@app.get('/profile')
def profile(user=Depends(get_current_user)):
    return {'profile': user}
```

Dependencies are resolved automatically by FastAPI. Use them for auth, DB sessions, pagination, etc.

## 7. Routers (splitting routes)

```python
# routers/users.py
from fastapi import APIRouter
router = APIRouter(prefix='/users', tags=['users'])

@router.get('/')
def list_users():
    return [{'id': 1}, {'id': 2}]

# main.py
from routers import users
app.include_router(users.router)
```

## 8. Async endpoints

```python
import asyncio

@app.get('/slow')
async def slow_endpoint():
    await asyncio.sleep(1)   # non-blocking I/O
    return {'status': 'done'}
```

Use `async def` for I/O-bound operations (database queries, HTTP calls). Use plain `def` for CPU-bound work.

## 9. CRUD pattern

```python
from typing import Dict

db: Dict[int, Item] = {}
counter = 0

@app.post('/items/', status_code=201)
def create(item: Item):
    global counter
    counter += 1
    db[counter] = item
    return {'id': counter, **item.model_dump()}

@app.get('/items/{item_id}')
def read(item_id: int):
    if item_id not in db:
        raise HTTPException(404, 'Not found')
    return db[item_id]

@app.put('/items/{item_id}')
def update(item_id: int, item: Item):
    if item_id not in db:
        raise HTTPException(404, 'Not found')
    db[item_id] = item
    return item

@app.delete('/items/{item_id}', status_code=204)
def delete(item_id: int):
    if item_id not in db:
        raise HTTPException(404, 'Not found')
    del db[item_id]
```

---

## Quick Reference

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel

app = FastAPI()

# Routes
@app.get('/path/{id}')   # path param
@app.post('/path/')       # request body
@app.put('/path/{id}')    # update
@app.delete('/path/{id}') # delete

# Pydantic model
class MyModel(BaseModel):
    field: str
    optional: int = 0

# Errors
raise HTTPException(status_code=404, detail='Not found')

# Router
from fastapi import APIRouter
router = APIRouter(prefix='/prefix', tags=['tag'])
app.include_router(router)
```

## Practice

| File | Difficulty | Topics |
|---|---|---|
| [01-easy.py](exercises/01-easy.py) | Easy | Routes, path/query params, basic Pydantic |
| [02-medium.py](exercises/02-medium.py) | Medium | CRUD, HTTPException, response models |
| [03-challenge.py](exercises/03-challenge.py) | Challenge | Routers, dependencies, async, auth middleware |

Solutions: [solutions/](solutions/)
