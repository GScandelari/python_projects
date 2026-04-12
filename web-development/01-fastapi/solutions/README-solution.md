# FastAPI — Solution Notes

## Easy

**Type annotations = validation:** Every path and query parameter is automatically validated. `item_id: int` means FastAPI rejects non-integer values with a 422 before your function even runs.

**`status_code=201`:** Pass it directly to the decorator. FastAPI uses 200 by default — always be explicit for POST/DELETE.

**Bool query params:** FastAPI accepts `true`, `1`, `yes` (and their falsy counterparts) for `bool` query params. No need to parse manually.

## Medium

**`Field(ge=1, le=5)`:** `ge` = greater-than-or-equal, `le` = less-than-or-equal. Also available: `gt`, `lt`, `min_length`, `max_length`, `regex`.

**`response_model`:** FastAPI serialises your return value through this model — extra fields are stripped, missing optional fields get defaults. Use it to decouple internal data from the API contract.

**In-memory DB pattern:** The `global _next_id` pattern is fine for learning. In production use an actual database (SQLAlchemy, SQLModel, Tortoise) and let the DB handle ID generation.

**204 No Content:** When status code is 204, FastAPI sends no body. Your function should return `None` (or nothing).

## Challenge

**Router organisation:** Keep one router per resource file. The `prefix` and `tags` on `APIRouter` mean you don't repeat them on each decorator. `app.include_router()` mounts them at startup.

**Dependency injection chain:** Dependencies can depend on other dependencies — FastAPI resolves the whole graph. Use this for: auth → get current user → check permissions.

**Header names:** FastAPI converts `x-api-key` (HTTP header) to `x_api_key` (Python identifier). Use `Header()` as the default value to tell FastAPI to read from headers, not query params.

**`async def` vs `def`:** Use `async def` for I/O-bound work (awaiting database/HTTP). Use plain `def` for CPU-bound work — FastAPI runs it in a thread pool automatically so it doesn't block the event loop.

**BackgroundTasks:** The response is sent to the client immediately; the background function runs after. Use `time.sleep` (not `asyncio.sleep`) inside background tasks because they run in a thread pool.

**Custom exception handlers:** Register with `@app.exception_handler(ExceptionClass)`. The handler receives `(request, exc)` and must return a `Response` object. `JSONResponse` sets the Content-Type header automatically.
