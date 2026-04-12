"""
Flask — Medium Exercises
=========================
Topics: CRUD REST API, Blueprint, abort, request validation.

Run:  python 02-medium.py
Visit: http://127.0.0.1:5000
"""

from flask import Flask, request, jsonify, abort, Blueprint

app = Flask(__name__)

# In-memory store
books: dict[int, dict] = {}
_next_id = 1


# ---------------------------------------------------------------------------
# 1. Book CRUD API (no blueprint yet)
# ---------------------------------------------------------------------------
# Implement a full CRUD API for books. Each book has:
#   id: int (auto-assigned)
#   title: str (required)
#   author: str (required)
#   year: int (required)
#   available: bool (default True)
#
# Endpoints:
#   POST   /books/             Create a book (status 201)
#   GET    /books/             List all books
#   GET    /books/<int:id>     Get one book (404 if not found)
#   PUT    /books/<int:id>     Replace a book (404 if not found)
#   PATCH  /books/<int:id>/checkout  Mark available=False (400 if already checked out)
#   DELETE /books/<int:id>     Delete (204, 404 if not found)
#
# Validate POST/PUT:
#   - title, author, year must be present → 400: {"error": "Missing fields: [...]"}
#   - year must be an integer             → 400: {"error": "year must be an integer"}

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. Blueprint — separate the /books routes
# ---------------------------------------------------------------------------
# Refactor your book routes into a Blueprint called 'books_bp'
# with url_prefix='/api/books'.
# Register it with the app.
# (Keep the same logic — just move it into the blueprint.)

# YOUR CODE HERE (or refactor above)


# ---------------------------------------------------------------------------
# 3. Stats endpoint
# ---------------------------------------------------------------------------
# GET /api/stats
#   Returns:
#     {
#       "total_books": <int>,
#       "available": <int>,
#       "checked_out": <int>,
#       "authors": [<unique sorted list of authors>]
#     }

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. Search / filter
# ---------------------------------------------------------------------------
# GET /api/books/?author=<name>&available=<true|false>
#   Extend the list endpoint to support optional filtering by:
#     author (case-insensitive contains match)
#     available (bool)
#   Return the filtered list.

# (Update your GET /api/books/ endpoint to support this)


if __name__ == '__main__':
    app.run(debug=True)
