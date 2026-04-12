"""
FastAPI — Easy Exercises
========================
Topics: basic routes, path params, query params, Pydantic models.

Run:  uvicorn 01-easy:app --reload
Docs: http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Easy Exercises')


# ---------------------------------------------------------------------------
# 1. Hello World
# ---------------------------------------------------------------------------
# Create a GET endpoint at '/' that returns:
#   {"message": "Hello, FastAPI!"}

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. Path parameter
# ---------------------------------------------------------------------------
# Create a GET endpoint at '/greet/{name}' that returns:
#   {"greeting": "Hello, Alice!"} when called with name='Alice'

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. Query parameters
# ---------------------------------------------------------------------------
# Create a GET endpoint at '/square' that accepts:
#   - n: int (required) — the number to square
#   - verbose: bool (optional, default False)
#
# If verbose=False: return {"result": 25}
# If verbose=True:  return {"input": 5, "operation": "square", "result": 25}

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. Pydantic model — request body
# ---------------------------------------------------------------------------
# Define a Pydantic model `Product` with fields:
#   name: str
#   price: float
#   quantity: int = 1
#
# Create a POST endpoint at '/products' (status 201) that:
#   - Accepts a Product body
#   - Returns {"received": <the product dict>, "total_value": price * quantity}

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 5. Multiple query params with types
# ---------------------------------------------------------------------------
# Create a GET endpoint at '/range' that accepts:
#   - start: int (default 0)
#   - end: int (default 10)
#   - step: int (default 1)
#
# Return {"values": [0, 1, 2, ..., 9]} (like range(start, end, step))
# If start >= end, return {"values": []}

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 6. Combined path + query
# ---------------------------------------------------------------------------
# Create a GET endpoint at '/users/{user_id}/posts' that accepts:
#   - user_id: int (path)
#   - limit: int (query, default 10, max 100)
#   - offset: int (query, default 0)
#
# Return:
#   {"user_id": 1, "limit": 10, "offset": 0, "posts": []}
# (posts is always an empty list for now — the structure is what matters)

# YOUR CODE HERE
