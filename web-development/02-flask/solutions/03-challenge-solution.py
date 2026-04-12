"""
Flask — Challenge Solutions

Run:  python 03-challenge-solution.py
"""

from flask import Flask, request, jsonify, abort, g, Blueprint
import math


# ---------------------------------------------------------------------------
# Pagination helper
# ---------------------------------------------------------------------------
def paginate(items: list, page: int = 1, per_page: int = 10) -> dict:
    total = len(items)
    pages = math.ceil(total / per_page) if per_page > 0 else 0
    start = (page - 1) * per_page
    end   = start + per_page
    return {
        'data': items[start:end],
        'page': page,
        'per_page': per_page,
        'total': total,
        'pages': pages,
    }


# ---------------------------------------------------------------------------
# users_bp
# ---------------------------------------------------------------------------
users_bp = Blueprint('users', __name__)
_FAKE_USERS = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]

@users_bp.route('/')
def list_users():
    return jsonify(_FAKE_USERS)

@users_bp.route('/<int:user_id>')
def get_user(user_id):
    user = next((u for u in _FAKE_USERS if u['id'] == user_id), None)
    if user is None:
        abort(404)
    return jsonify(user)

@users_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json(silent=True) or {}
    if 'name' not in data:
        return jsonify({'error': 'name is required'}), 400
    new_id = max(u['id'] for u in _FAKE_USERS) + 1
    user = {'id': new_id, 'name': data['name']}
    _FAKE_USERS.append(user)
    return jsonify(user), 201


# ---------------------------------------------------------------------------
# products_bp
# ---------------------------------------------------------------------------
products_bp = Blueprint('products', __name__)
_products: dict[int, dict] = {}
_prod_id = 0

@products_bp.route('/', methods=['POST'])
def create_product():
    global _prod_id
    data = request.get_json(silent=True) or {}
    if 'name' not in data or 'price' not in data:
        return jsonify({'error': 'name and price are required'}), 400
    try:
        price = float(data['price'])
    except (ValueError, TypeError):
        return jsonify({'error': 'price must be a number'}), 400
    _prod_id += 1
    _products[_prod_id] = {'id': _prod_id, 'name': str(data['name']), 'price': price}
    return jsonify(_products[_prod_id]), 201

@products_bp.route('/')
def list_products():
    page     = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    return jsonify(paginate(list(_products.values()), page, per_page))

@products_bp.route('/<int:product_id>')
def get_product(product_id):
    if product_id not in _products:
        abort(404)
    return jsonify(_products[product_id])

@products_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id not in _products:
        abort(404)
    del _products[product_id]
    return '', 204


# ---------------------------------------------------------------------------
# Application factory
# ---------------------------------------------------------------------------
def create_app(config=None):
    app = Flask(__name__)

    if config:
        app.config.update(config)

    # Auth middleware
    @app.before_request
    def check_api_key():
        if request.path.startswith('/public'):
            return   # no auth for public routes
        key = request.headers.get('X-API-Key')
        if not key or key != 'valid-key':
            return jsonify({'error': 'Unauthorized'}), 401
        g.api_key = key

    # Public health check
    @app.route('/public/health')
    def health():
        return jsonify({'status': 'healthy'})

    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'error': 'Not found'}), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify({'error': 'Method not allowed'}), 405

    # Register blueprints
    app.register_blueprint(users_bp,    url_prefix='/api/users')
    app.register_blueprint(products_bp, url_prefix='/api/products')

    return app


if __name__ == '__main__':
    app = create_app({'DEBUG': True})
    app.run(debug=True)
