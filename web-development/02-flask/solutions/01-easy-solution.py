"""
Flask — Easy Solutions

Run:  python 01-easy-solution.py
"""

from flask import Flask, request, jsonify, abort

app = Flask(__name__)


# ---------------------------------------------------------------------------
# 1. Static routes
# ---------------------------------------------------------------------------
@app.route('/')
def index():
    return 'Hello, Flask!'

@app.route('/about')
def about():
    return jsonify({'app': 'My Flask App', 'version': '1.0'})

@app.route('/ping')
def ping():
    return jsonify({'status': 'ok'})


# ---------------------------------------------------------------------------
# 2. Path parameters
# ---------------------------------------------------------------------------
@app.route('/greet/<name>')
def greet(name):
    return jsonify({'greeting': f'Hello, {name}!'})

@app.route('/square/<int:n>')
def square(n):
    return jsonify({'n': n, 'result': n ** 2})


# ---------------------------------------------------------------------------
# 3. Query parameters
# ---------------------------------------------------------------------------
@app.route('/search')
def search():
    q = request.args.get('q')
    if not q:
        return jsonify({'error': 'q is required'}), 400
    try:
        limit = int(request.args.get('limit', 10))
    except ValueError:
        return jsonify({'error': 'limit must be an integer'}), 400
    return jsonify({'q': q, 'limit': limit, 'results': []})


# ---------------------------------------------------------------------------
# 4. POST with JSON body
# ---------------------------------------------------------------------------
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    return jsonify({'received': data, 'keys': list(data.keys())})


# ---------------------------------------------------------------------------
# 5. Error handlers
# ---------------------------------------------------------------------------
@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found', 'path': request.path}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'error': 'Method not allowed'}), 405


# ---------------------------------------------------------------------------
# 6. Calculator endpoint
# ---------------------------------------------------------------------------
@app.route('/calc')
def calc():
    a_str = request.args.get('a')
    b_str = request.args.get('b')
    if a_str is None or b_str is None:
        return jsonify({'error': 'a and b are required'}), 400

    try:
        a, b = float(a_str), float(b_str)
    except ValueError:
        return jsonify({'error': 'a and b must be numbers'}), 400

    op = request.args.get('op', 'add')
    if op not in ('add', 'sub', 'mul', 'div'):
        return jsonify({'error': 'op must be add/sub/mul/div'}), 400
    if op == 'div' and b == 0:
        return jsonify({'error': 'Cannot divide by zero'}), 400

    ops = {'add': a + b, 'sub': a - b, 'mul': a * b, 'div': a / b}
    return jsonify({'a': a, 'b': b, 'op': op, 'result': ops[op]})


if __name__ == '__main__':
    app.run(debug=True)
