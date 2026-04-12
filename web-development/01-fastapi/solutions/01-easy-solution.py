"""
FastAPI — Easy Solutions

Run:  uvicorn 01-easy-solution:app --reload
Docs: http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Easy Solutions')


# ---------------------------------------------------------------------------
# 1. Hello World
# ---------------------------------------------------------------------------
@app.get('/')
def read_root():
    return {'message': 'Hello, FastAPI!'}


# ---------------------------------------------------------------------------
# 2. Path parameter
# ---------------------------------------------------------------------------
@app.get('/greet/{name}')
def greet(name: str):
    return {'greeting': f'Hello, {name}!'}


# ---------------------------------------------------------------------------
# 3. Query parameters
# ---------------------------------------------------------------------------
@app.get('/square')
def square(n: int, verbose: bool = False):
    result = n ** 2
    if verbose:
        return {'input': n, 'operation': 'square', 'result': result}
    return {'result': result}


# ---------------------------------------------------------------------------
# 4. Pydantic model — request body
# ---------------------------------------------------------------------------
class Product(BaseModel):
    name: str
    price: float
    quantity: int = 1

@app.post('/products', status_code=201)
def create_product(product: Product):
    return {
        'received': product.model_dump(),
        'total_value': product.price * product.quantity,
    }


# ---------------------------------------------------------------------------
# 5. Multiple query params with types
# ---------------------------------------------------------------------------
@app.get('/range')
def number_range(start: int = 0, end: int = 10, step: int = 1):
    if start >= end:
        return {'values': []}
    return {'values': list(range(start, end, step))}


# ---------------------------------------------------------------------------
# 6. Combined path + query
# ---------------------------------------------------------------------------
@app.get('/users/{user_id}/posts')
def user_posts(user_id: int, limit: int = 10, offset: int = 0):
    limit = min(limit, 100)   # cap at 100
    return {
        'user_id': user_id,
        'limit': limit,
        'offset': offset,
        'posts': [],
    }
