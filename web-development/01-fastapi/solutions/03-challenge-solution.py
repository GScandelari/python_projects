"""
FastAPI — Challenge Solutions

Run:  uvicorn 03-challenge-solution:app --reload
Docs: http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException, Depends, Header, BackgroundTasks, APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from typing import Optional
import asyncio
import time

app = FastAPI(title='Advanced API')


# ---------------------------------------------------------------------------
# 1. APIRouter
# ---------------------------------------------------------------------------
products_router = APIRouter(prefix='/products', tags=['products'])
orders_router   = APIRouter(prefix='/orders',   tags=['orders'])

class ProductIn(BaseModel):
    name: str
    price: float

class OrderIn(BaseModel):
    product_id: int
    quantity: int

@products_router.get('/')
def list_products():
    return [
        {'id': 1, 'name': 'Widget', 'price': 9.99},
        {'id': 2, 'name': 'Gadget', 'price': 24.99},
        {'id': 3, 'name': 'Doohickey', 'price': 4.99},
    ]

@products_router.get('/{product_id}')
def get_product(product_id: int):
    return {'id': product_id, 'name': 'Widget', 'price': 9.99}

@products_router.post('/', status_code=201)
def create_product(product: ProductIn):
    return {'id': 999, **product.model_dump()}

@orders_router.get('/')
def list_orders():
    return []

@orders_router.post('/', status_code=201)
def create_order(order: OrderIn):
    return {'id': 1, **order.model_dump(), 'status': 'pending'}

app.include_router(products_router)
app.include_router(orders_router)


# ---------------------------------------------------------------------------
# 2. Dependency injection — pagination
# ---------------------------------------------------------------------------
def pagination(skip: int = 0, limit: int = 10):
    return {'skip': skip, 'limit': limit}

@app.get('/items')
def list_items(page: dict = Depends(pagination)):
    return {'items': [], 'pagination': page}


# ---------------------------------------------------------------------------
# 3. API key authentication
# ---------------------------------------------------------------------------
def require_api_key(x_api_key: str = Header()):
    if x_api_key != 'secret-key-123':
        raise HTTPException(status_code=401, detail='Invalid API key')
    return x_api_key

@app.get('/secure/data')
def secure_data(key: str = Depends(require_api_key)):
    return {'secret': 'this is protected data', 'key_used': key}


# ---------------------------------------------------------------------------
# 4. Async endpoints
# ---------------------------------------------------------------------------
async def _fetch(source: str) -> dict:
    await asyncio.sleep(0.5)
    return {'source': source, 'data': 'fetched', 'latency_ms': 500}

@app.get('/async/fetch/{source}')
async def fetch(source: str):
    return await _fetch(source)

@app.get('/async/gather')
async def gather():
    results = await asyncio.gather(
        _fetch('API-1'),
        _fetch('API-2'),
        _fetch('API-3'),
    )
    return list(results)


# ---------------------------------------------------------------------------
# 5. Background tasks
# ---------------------------------------------------------------------------
class NotifyRequest(BaseModel):
    email: str
    message: str

def _send_email(email: str, message: str):
    print(f'[BG] Sending email to {email}: {message}')
    time.sleep(1)
    print(f'[BG] Done sending to {email}')

@app.post('/notify')
def notify(body: NotifyRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(_send_email, body.email, body.message)
    return {'status': 'notification queued'}


# ---------------------------------------------------------------------------
# 6. Custom exception handler
# ---------------------------------------------------------------------------
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            'error': 'Validation failed',
            'details': exc.errors(),
        },
    )
