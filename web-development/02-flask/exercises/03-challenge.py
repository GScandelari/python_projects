"""
Flask — Challenge Exercises
============================
Topics: application factory, before_request auth middleware,
        pagination helper, custom error classes, g object.

Run:  python 03-challenge.py
Visit: http://127.0.0.1:5000
"""

from flask import Flask, request, jsonify, abort, g, Blueprint


# ---------------------------------------------------------------------------
# 1. Application factory
# ---------------------------------------------------------------------------
# Implement create_app(config=None) that:
#   - Creates a Flask app
#   - Applies the given config dict (if any) via app.config.update()
#   - Registers all blueprints
#   - Registers all error handlers
#   - Returns the app
#
# Blueprints to register (define them below):
#   - users_bp   (url_prefix='/api/users')
#   - products_bp (url_prefix='/api/products')

def create_app(config=None):
    # YOUR CODE HERE
    pass


# ---------------------------------------------------------------------------
# 2. users_bp — Blueprint
# ---------------------------------------------------------------------------
# GET  /api/users/             → list users (fake data: [{id:1,name:'Alice'},{id:2,name:'Bob'}])
# GET  /api/users/<int:id>     → get one user (if id not in [1,2] → 404)
# POST /api/users/             → create user (requires 'name' in body → 201)

users_bp = Blueprint('users', __name__)

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. products_bp — Blueprint
# ---------------------------------------------------------------------------
# In-memory products store.
# POST   /api/products/          → create (requires name, price) → 201
# GET    /api/products/          → list with pagination (page, per_page query params)
# GET    /api/products/<int:id>  → get one or 404
# DELETE /api/products/<int:id>  → delete or 404, return 204

products_bp = Blueprint('products', __name__)
_products: dict[int, dict] = {}
_prod_id = 0

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. API key middleware using before_request
# ---------------------------------------------------------------------------
# In create_app, register a before_request handler on the app that:
#   - Skips the check for routes that start with '/public'
#   - For all other routes, reads the 'X-API-Key' header
#   - If missing or not 'valid-key', returns 401 JSON: {"error": "Unauthorized"}
#   - If valid, stores it in flask.g.api_key

# (Add this inside create_app)


# ---------------------------------------------------------------------------
# 5. Public route — no auth required
# ---------------------------------------------------------------------------
# GET /public/health  → {"status": "healthy"} (no API key needed)
# Add this directly to the app inside create_app (not a blueprint).


# ---------------------------------------------------------------------------
# 6. Pagination helper
# ---------------------------------------------------------------------------
# Implement a function paginate(items, page, per_page) that returns:
# {
#   "data": <slice of items>,
#   "page": page,
#   "per_page": per_page,
#   "total": len(items),
#   "pages": ceil(total / per_page)
# }
# Use it in GET /api/products/.

import math

def paginate(items: list, page: int = 1, per_page: int = 10) -> dict:
    # YOUR CODE HERE
    pass


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    app = create_app({'DEBUG': True})
    app.run(debug=True)
