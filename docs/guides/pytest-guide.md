# pytest — Guide

## Installation & First Run

```bash
pip install pytest pytest-cov

# Run all tests
pytest

# Run specific file / test
pytest tests/test_math.py
pytest tests/test_math.py::test_add
pytest tests/test_math.py::TestMath::test_add

# Verbose output
pytest -v

# Show print statements
pytest -s

# Stop on first failure
pytest -x

# Run last failed tests
pytest --lf
```

---

## Writing Tests

```python
# tests/test_math.py

def add(a, b): return a + b

# Test function — must start with test_
def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

# Test class — must start with Test (no __init__)
class TestAdd:
    def test_zero(self):
        assert add(0, 0) == 0

    def test_float(self):
        assert add(1.5, 2.5) == 4.0
```

---

## Assertions

```python
# Basic
assert result == expected
assert result != unexpected
assert result is None
assert result is not None
assert isinstance(result, int)
assert 'hello' in result

# Approx (floats)
from pytest import approx
assert 0.1 + 0.2 == approx(0.3)
assert 0.1 + 0.2 == approx(0.3, rel=1e-3)   # relative tolerance

# Exceptions
import pytest

with pytest.raises(ValueError):
    int('not a number')

with pytest.raises(ValueError, match='invalid literal'):
    int('not a number')

# Warnings
with pytest.warns(DeprecationWarning):
    old_function()
```

---

## Fixtures

Fixtures provide reusable setup/teardown for tests.

```python
import pytest

@pytest.fixture
def db_connection():
    conn = create_connection(':memory:')
    yield conn               # test runs here
    conn.close()             # teardown

def test_insert(db_connection):
    db_connection.execute('INSERT ...')
    assert db_connection.fetchall() == [...]

# Scope: function (default), class, module, session
@pytest.fixture(scope='module')
def expensive_resource():
    resource = load_large_dataset()
    yield resource

# Built-in fixtures
def test_tmp(tmp_path):           # temporary directory (pathlib.Path)
    f = tmp_path / 'data.txt'
    f.write_text('hello')
    assert f.read_text() == 'hello'

def test_cap(capsys):             # capture stdout/stderr
    print('hello')
    captured = capsys.readouterr()
    assert captured.out == 'hello\n'

def test_monkeypatch(monkeypatch): # patch attributes / env vars
    monkeypatch.setenv('API_KEY', 'test-key')
    monkeypatch.setattr('module.function', lambda: 'mocked')
```

---

## Parametrize

```python
import pytest

@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# Combine with fixtures
@pytest.mark.parametrize('value', [None, '', 0, [], {}])
def test_falsy(value):
    assert not value
```

---

## Markers

```python
import pytest

@pytest.mark.slow
def test_heavy_computation(): ...

@pytest.mark.skip(reason='not implemented yet')
def test_future(): ...

@pytest.mark.skipif(sys.platform == 'win32', reason='Unix only')
def test_unix_feature(): ...

@pytest.mark.xfail(reason='known bug #123')
def test_known_failure(): ...
```

Register custom markers in `pytest.ini` or `pyproject.toml`:

```toml
# pyproject.toml
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow (deselect with '-m not slow')",
    "integration: marks integration tests",
]
```

Run by marker:
```bash
pytest -m slow
pytest -m "not slow"
pytest -m "slow or integration"
```

---

## Coverage

```bash
# Run with coverage
pytest --cov=src

# HTML report
pytest --cov=src --cov-report=html
open htmlcov/index.html

# Fail if coverage below threshold
pytest --cov=src --cov-fail-under=80

# .coveragerc (or pyproject.toml)
```

```toml
# pyproject.toml
[tool.coverage.run]
source = ["src"]
omit = ["*/tests/*", "*/__init__.py"]

[tool.coverage.report]
fail_under = 80
show_missing = true
```

---

## conftest.py

Shared fixtures and plugins, auto-discovered by pytest.

```
tests/
├── conftest.py        ← fixtures available to ALL tests here
├── unit/
│   ├── conftest.py    ← fixtures for unit/ only
│   └── test_math.py
└── integration/
    └── test_api.py
```

```python
# tests/conftest.py
import pytest
from myapp import create_app

@pytest.fixture(scope='session')
def app():
    return create_app(testing=True)

@pytest.fixture
def client(app):
    return app.test_client()
```

---

## pytest.ini / pyproject.toml

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts   = "-v --tb=short"
filterwarnings = ["error::DeprecationWarning"]
```

---

## Project Layout

```
my-project/
├── src/
│   └── myapp/
│       ├── __init__.py
│       └── math.py
├── tests/
│   ├── conftest.py
│   ├── unit/
│   │   └── test_math.py
│   └── integration/
│       └── test_api.py
├── pyproject.toml
└── requirements.txt
```

---

## Quick Reference

```bash
pytest                        # run all
pytest -v                     # verbose
pytest -x                     # stop on first fail
pytest -k "add"               # run tests matching 'add'
pytest -m slow                # run by marker
pytest --lf                   # last failed
pytest --co                   # collect only (list tests)
pytest --cov=src              # coverage
pytest -s                     # don't capture stdout
```
