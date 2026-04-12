"""
Flask — Easy Exercises
=======================
Topics: basic routes, request object, jsonify, query params, error handlers.

Run:  python 01-easy.py
      or: flask --app 01-easy run --debug
Visit: http://127.0.0.1:5000
"""

from flask import Flask, request, jsonify, abort

app = Flask(__name__)


# ---------------------------------------------------------------------------
# 1. Static routes
# ---------------------------------------------------------------------------
# Create the following GET routes:
#
# GET /          → returns the plain string 'Hello, Flask!'
# GET /about     → returns JSON: {"app": "My Flask App", "version": "1.0"}
# GET /ping      → returns JSON: {"status": "ok"}

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. Path parameters
# ---------------------------------------------------------------------------
# GET /greet/<name>
#   → JSON: {"greeting": "Hello, Alice!"} when name = 'Alice'
#
# GET /square/<int:n>
#   → JSON: {"n": 5, "result": 25}

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. Query parameters
# ---------------------------------------------------------------------------
# GET /search
#   Query params: q (required), limit (optional int, default 10)
#   If 'q' is missing, return 400 JSON: {"error": "q is required"}
#   Otherwise return: {"q": "python", "limit": 10, "results": []}

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. POST with JSON body
# ---------------------------------------------------------------------------
# POST /echo
#   Accepts any JSON body
#   Returns: {"received": <the body>, "keys": [list of keys]}
#   If the body is not valid JSON, return 400 JSON: {"error": "Invalid JSON"}

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 5. Error handlers
# ---------------------------------------------------------------------------
# Register handlers for 404 and 405 that return JSON instead of HTML:
#   404: {"error": "Not found", "path": <request.path>}
#   405: {"error": "Method not allowed"}

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 6. Calculator endpoint
# ---------------------------------------------------------------------------
# GET /calc
#   Query params: a (float), b (float), op (str: add/sub/mul/div)
#   Returns: {"a": 10, "b": 5, "op": "add", "result": 15}
#   Errors:
#     - missing a or b → 400: {"error": "a and b are required"}
#     - invalid op     → 400: {"error": "op must be add/sub/mul/div"}
#     - division by 0  → 400: {"error": "Cannot divide by zero"}

# YOUR CODE HERE


if __name__ == '__main__':
    app.run(debug=True)
