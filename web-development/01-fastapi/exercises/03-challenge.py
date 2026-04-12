"""
FastAPI — Challenge Exercises
==============================
Topics: APIRouter, dependency injection, API key auth, async endpoints,
        background tasks, custom exception handlers.

Run:  uvicorn 03-challenge:app --reload
Docs: http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException, Depends, Header, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from typing import Optional
import asyncio
import time

app = FastAPI(title='Advanced API')

# ---------------------------------------------------------------------------
# 1. APIRouter — split routes into modules
# ---------------------------------------------------------------------------
# Create two APIRouters:
#   - products_router: prefix='/products', tag='products'
#   - orders_router:   prefix='/orders',   tag='orders'
#
# products_router endpoints:
#   GET  /products/        → list all products (return a static list of 3 items)
#   GET  /products/{id}    → return one product (fake data, always found)
#   POST /products/        → create product (accept name+price, return with id=999)
#
# orders_router endpoints:
#   GET  /orders/          → list orders (return empty list for now)
#   POST /orders/          → create order (accept product_id+quantity)
#
# Include both routers in app.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. Dependency injection — pagination
# ---------------------------------------------------------------------------
# Create a dependency function `pagination` that extracts:
#   skip: int = 0
#   limit: int = 10
# and returns them as a dict {"skip": skip, "limit": limit}.
#
# Create a GET endpoint at '/items' that uses this dependency
# and returns {"items": [], "pagination": {"skip": 0, "limit": 10}}.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. API key authentication dependency
# ---------------------------------------------------------------------------
# Create a dependency `require_api_key` that:
#   - Reads an 'x-api-key' header (use Header())
#   - Raises 401 if the key is not exactly 'secret-key-123'
#   - Returns the key if valid
#
# Create a GET endpoint at '/secure/data' that uses this dependency
# and returns {"secret": "this is protected data", "key_used": <key>}.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. Async endpoint with simulated latency
# ---------------------------------------------------------------------------
# Create a GET endpoint at '/async/fetch/{source}' that:
#   - Accepts a path param `source` (str)
#   - Awaits asyncio.sleep(0.5) to simulate I/O
#   - Returns {"source": source, "data": "fetched", "latency_ms": 500}
#
# Also create a GET at '/async/gather' that calls the above logic
# for THREE sources concurrently using asyncio.gather and returns
# all three results in a list.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 5. Background tasks
# ---------------------------------------------------------------------------
# Create a POST endpoint at '/notify' that:
#   - Accepts a body with `email: str` and `message: str`
#   - Adds a background task that prints:
#       f"[BG] Sending email to {email}: {message}"
#       then sleeps 1 second (use time.sleep — background tasks run in threadpool)
#   - Returns immediately with {"status": "notification queued"}

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 6. Custom exception handler
# ---------------------------------------------------------------------------
# Register a custom exception handler for RequestValidationError
# (validation errors from Pydantic) that returns:
# {
#   "error": "Validation failed",
#   "details": <the error details list>
# }
# with status code 422.
#
# Hint: use @app.exception_handler(RequestValidationError)

# YOUR CODE HERE
