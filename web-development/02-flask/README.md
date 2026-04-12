# Flask

A lightweight, flexible web framework for Python. Great for APIs, web apps, and prototypes.

**Install:** `pip install flask`

**Run:** `flask --app main run --debug`  
or set `app.run(debug=True)` in `main.py` and run `python main.py`

---

## 1. Hello World

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

## 2. Routes and HTTP Methods

```python
@app.route('/about')           # GET only by default
def about():
    return 'About page'

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return 'Form submitted'
    return 'Show form'

@app.route('/items/<int:item_id>')   # typed path parameter
def get_item(item_id):
    return f'Item {item_id}'
```

## 3. Request Object

```python
from flask import request

@app.route('/search')
def search():
    q = request.args.get('q', '')      # query params
    return f'Searching: {q}'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()          # JSON body
    username = data.get('username')
    return f'Logged in: {username}'
```

## 4. JSON Responses

```python
from flask import jsonify

@app.route('/api/users')
def users():
    return jsonify([
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
    ])

# Custom status code
@app.route('/api/items', methods=['POST'])
def create():
    return jsonify({'id': 1, 'created': True}), 201
```

## 5. Error Handlers

```python
from flask import jsonify

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({'error': str(e)}), 400

# Manual abort
from flask import abort
@app.route('/items/<int:id>')
def get_item(id):
    if id not in db:
        abort(404)
    return jsonify(db[id])
```

## 6. Blueprints (modular routes)

```python
# blueprints/users.py
from flask import Blueprint

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/')
def list_users():
    return jsonify([])

@users_bp.route('/<int:user_id>')
def get_user(user_id):
    return jsonify({'id': user_id})

# main.py
from blueprints.users import users_bp
app.register_blueprint(users_bp)
```

## 7. Templates with Jinja2

```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```

```html
<!-- templates/hello.html -->
<!DOCTYPE html>
<html>
<body>
  <h1>Hello, {{ name }}!</h1>
  {% if name == 'admin' %}
    <p>Welcome back, administrator.</p>
  {% endif %}
</body>
</html>
```

## 8. Application factory pattern

```python
# app/__init__.py
from flask import Flask

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config or 'app.config.DefaultConfig')

    from .blueprints.users import users_bp
    app.register_blueprint(users_bp)

    return app
```

---

## Quick Reference

```python
from flask import Flask, request, jsonify, abort, Blueprint

app = Flask(__name__)

# Routes
@app.route('/path', methods=['GET', 'POST'])
@app.route('/path/<int:id>')

# Request
request.args.get('key')         # query params
request.get_json()              # JSON body
request.form.get('field')       # form data

# Response
return jsonify({...})           # JSON
return jsonify({...}), 201      # with status code
abort(404)                      # error shortcut

# Blueprint
bp = Blueprint('name', __name__, url_prefix='/prefix')
app.register_blueprint(bp)

# Error handler
@app.errorhandler(404)
def not_found(e): ...
```

## Practice

| File | Difficulty | Topics |
|---|---|---|
| [01-easy.py](exercises/01-easy.py) | Easy | Routes, request, jsonify, error handlers |
| [02-medium.py](exercises/02-medium.py) | Medium | CRUD API, blueprints, abort |
| [03-challenge.py](exercises/03-challenge.py) | Challenge | Application factory, auth middleware, pagination |

Solutions: [solutions/](solutions/)
