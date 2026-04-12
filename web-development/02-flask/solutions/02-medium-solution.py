"""
Flask — Medium Solutions

Run:  python 02-medium-solution.py
"""

from flask import Flask, request, jsonify, abort, Blueprint

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Data store
# ---------------------------------------------------------------------------
books: dict[int, dict] = {}
_next_id = 1

# ---------------------------------------------------------------------------
# Blueprint
# ---------------------------------------------------------------------------
books_bp = Blueprint('books', __name__, url_prefix='/api/books')


def _validate_book_payload(data: dict) -> tuple[dict | None, str | None]:
    """Returns (cleaned_data, error_message)."""
    missing = [f for f in ('title', 'author', 'year') if f not in data]
    if missing:
        return None, f'Missing fields: {missing}'
    try:
        year = int(data['year'])
    except (ValueError, TypeError):
        return None, 'year must be an integer'
    return {
        'title': str(data['title']),
        'author': str(data['author']),
        'year': year,
        'available': bool(data.get('available', True)),
    }, None


# ---------------------------------------------------------------------------
# 1. POST /api/books/ — create
# ---------------------------------------------------------------------------
@books_bp.route('/', methods=['POST'])
def create_book():
    global _next_id
    data = request.get_json(silent=True) or {}
    clean, err = _validate_book_payload(data)
    if err:
        return jsonify({'error': err}), 400
    books[_next_id] = {'id': _next_id, **clean}
    _next_id += 1
    return jsonify(books[_next_id - 1]), 201


# ---------------------------------------------------------------------------
# 2. GET /api/books/ — list + filter
# ---------------------------------------------------------------------------
@books_bp.route('/', methods=['GET'])
def list_books():
    result = list(books.values())
    author = request.args.get('author')
    available = request.args.get('available')
    if author:
        result = [b for b in result if author.lower() in b['author'].lower()]
    if available is not None:
        flag = available.lower() in ('true', '1', 'yes')
        result = [b for b in result if b['available'] == flag]
    return jsonify(result)


# ---------------------------------------------------------------------------
# 3. GET /api/books/<id>
# ---------------------------------------------------------------------------
@books_bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    if book_id not in books:
        abort(404)
    return jsonify(books[book_id])


# ---------------------------------------------------------------------------
# 4. PUT /api/books/<id> — replace
# ---------------------------------------------------------------------------
@books_bp.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    if book_id not in books:
        abort(404)
    data = request.get_json(silent=True) or {}
    clean, err = _validate_book_payload(data)
    if err:
        return jsonify({'error': err}), 400
    books[book_id].update(clean)
    return jsonify(books[book_id])


# ---------------------------------------------------------------------------
# 5. PATCH /api/books/<id>/checkout
# ---------------------------------------------------------------------------
@books_bp.route('/<int:book_id>/checkout', methods=['PATCH'])
def checkout_book(book_id):
    if book_id not in books:
        abort(404)
    if not books[book_id]['available']:
        return jsonify({'error': 'Book already checked out'}), 400
    books[book_id]['available'] = False
    return jsonify(books[book_id])


# ---------------------------------------------------------------------------
# 6. DELETE /api/books/<id>
# ---------------------------------------------------------------------------
@books_bp.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id not in books:
        abort(404)
    del books[book_id]
    return '', 204


# ---------------------------------------------------------------------------
# 7. Stats
# ---------------------------------------------------------------------------
@app.route('/api/stats')
def stats():
    all_books = list(books.values())
    return jsonify({
        'total_books': len(all_books),
        'available': sum(1 for b in all_books if b['available']),
        'checked_out': sum(1 for b in all_books if not b['available']),
        'authors': sorted({b['author'] for b in all_books}),
    })


# ---------------------------------------------------------------------------
# Error handlers
# ---------------------------------------------------------------------------
@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({'error': str(e)}), 400


app.register_blueprint(books_bp)

if __name__ == '__main__':
    app.run(debug=True)
