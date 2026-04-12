# Testing with pytest

Writing tests is how you prove your code works — and keep it working as it changes. `pytest` is the industry-standard testing framework for Python.

## Table of Contents

- [Why test?](#1-why-test)
- [Your first test](#2-your-first-test)
- [Assertions](#3-assertions)
- [pytest.raises — testing exceptions](#4-pytestraises--testing-exceptions)
- [Fixtures](#5-fixtures)
- [Parametrize](#6-parametrize)
- [Monkeypatching](#7-monkeypatching)
- [Mocking with unittest.mock](#8-mocking-with-unittestmock)
- [Coverage](#9-coverage)
- [Quick Reference](#quick-reference)
- [What's Next](#whats-next)

---

## 1. Why test?

- **Catch regressions** — changes that break existing behaviour are caught immediately.
- **Document intent** — tests show how your code is supposed to be used.
- **Enable refactoring** — you can clean up code confidently when tests guard it.
- **Design pressure** — hard-to-test code is usually poorly designed.

---

## 2. Your first test

pytest discovers test files automatically — any file named `test_*.py` or `*_test.py`.

```python
# src/calculator.py
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


# tests/test_calculator.py
from src.calculator import add, divide

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)
```

Run with: `pytest` or `pytest -v` (verbose).

---

## 3. Assertions

pytest rewrites `assert` statements to give detailed failure messages — no need for `assertEqual`, `assertTrue`, etc.:

```python
import pytest

def test_assertions():
    # Equality
    assert 1 + 1 == 2

    # Floating point — never use == for floats
    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert 0.1 + 0.2 == pytest.approx(0.3, rel=1e-6)

    # Membership
    assert "python" in ["python", "java", "go"]
    assert "key" in {"key": "value"}

    # Type check
    assert isinstance(42, int)

    # String contains
    assert "Hello" in "Hello, World!"
```

---

## 4. pytest.raises — testing exceptions

```python
import pytest
from src.calculator import divide

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_divide_by_zero_message():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)

def test_divide_normal():
    assert divide(10, 2) == 5.0
```

---

## 5. Fixtures

Fixtures set up (and tear down) test dependencies. They're injected by name as function parameters:

```python
import pytest

@pytest.fixture
def sample_list():
    return [3, 1, 4, 1, 5, 9, 2, 6]

@pytest.fixture
def empty_list():
    return []

def test_sort(sample_list):
    assert sorted(sample_list) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_append(empty_list):
    empty_list.append(42)
    assert empty_list == [42]


# Fixture with setup AND teardown (using yield)
@pytest.fixture
def temp_file(tmp_path):
    path = tmp_path / "data.txt"
    path.write_text("hello")
    yield path            # test runs here
    # teardown — runs after test (even on failure)
    if path.exists():
        path.unlink()

def test_file_content(temp_file):
    assert temp_file.read_text() == "hello"
```

### Fixture scopes

| Scope | Created once per |
|---|---|
| `function` (default) | Each test function |
| `class` | Each test class |
| `module` | Each test module (file) |
| `session` | Entire test session |

---

## 6. Parametrize

Run the same test with multiple input sets:

```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, -50, 50),
])
def test_add(a, b, expected):
    assert a + b == expected

# Combine with fixtures
@pytest.mark.parametrize("text,expected", [
    ("hello", True),
    ("racecar", True),
    ("world", False),
])
def test_is_palindrome(text, expected):
    assert (text == text[::-1]) == expected
```

---

## 7. Monkeypatching

`monkeypatch` replaces attributes, environment variables, or functions during a test:

```python
import os

def get_greeting():
    name = os.environ.get("USER_NAME", "stranger")
    return f"Hello, {name}!"

def test_greeting_default(monkeypatch):
    monkeypatch.delenv("USER_NAME", raising=False)
    assert get_greeting() == "Hello, stranger!"

def test_greeting_custom(monkeypatch):
    monkeypatch.setenv("USER_NAME", "Alice")
    assert get_greeting() == "Hello, Alice!"

def test_custom_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "42")
    assert int(input("Enter: ")) == 42
```

---

## 8. Mocking with unittest.mock

`Mock` objects replace real dependencies (API calls, databases, file I/O) in tests:

```python
from unittest.mock import Mock, patch, MagicMock

def send_email(to, subject, body, smtp_client):
    return smtp_client.send(to=to, subject=subject, body=body)

def test_send_email():
    mock_smtp = Mock()
    mock_smtp.send.return_value = {"status": "sent"}

    result = send_email("alice@test.com", "Hi", "Body", mock_smtp)

    mock_smtp.send.assert_called_once_with(
        to="alice@test.com", subject="Hi", body="Body"
    )
    assert result["status"] == "sent"


# patch() as decorator — replaces during the test, restores after
import requests

def fetch_data(url):
    response = requests.get(url)
    return response.json()

@patch("requests.get")
def test_fetch_data(mock_get):
    mock_get.return_value.json.return_value = {"key": "value"}
    result = fetch_data("http://example.com/api")
    assert result == {"key": "value"}
    mock_get.assert_called_once_with("http://example.com/api")
```

---

## 9. Coverage

Measure which lines are actually executed by your tests:

```bash
pip install pytest-cov
pytest --cov=src --cov-report=term-missing
```

Aim for high coverage on **business logic**, not boilerplate. 100% coverage doesn't mean bug-free.

---

## Quick Reference

```python
# Run tests
pytest                      # discover and run all
pytest -v                   # verbose output
pytest test_file.py         # specific file
pytest -k "keyword"         # filter by name
pytest --tb=short           # shorter tracebacks
pytest --cov=src            # with coverage

# Core patterns
assert value == expected
assert pytest.approx(0.3) == 0.1 + 0.2

with pytest.raises(SomeError):
    risky_call()

@pytest.fixture
def my_fixture(): return setup_value()

@pytest.mark.parametrize("x,y", [(1,2),(3,4)])
def test_func(x, y): ...

monkeypatch.setenv("KEY", "val")
monkeypatch.setattr(obj, "attr", mock_value)

mock = Mock()
mock.method.return_value = "result"
mock.method.assert_called_once_with(arg)

@patch("module.ClassName")
def test_it(MockClass): ...
```

---

## What's Next

Try the exercises in [`exercises/`](./exercises/) — write tests for real modules, use fixtures, parametrize, and mock external dependencies.

Next concept: [`04-design-patterns`](../04-design-patterns/)
