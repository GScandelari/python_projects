# Error Handling

Errors are inevitable. Python's exception system lets you catch them gracefully, give useful feedback, and keep programs running when something unexpected happens.

## Table of Contents

- [Syntax Errors vs Exceptions](#1-syntax-errors-vs-exceptions)
- [try / except](#2-try--except)
- [else and finally](#3-else-and-finally)
- [Built-in Exception Types](#4-built-in-exception-types)
- [Raising Exceptions](#5-raising-exceptions)
- [Custom Exceptions](#6-custom-exceptions)
- [Exception Chaining](#7-exception-chaining)
- [Common Patterns](#8-common-patterns)
- [Quick Reference](#quick-reference)
- [What's Next](#whats-next)

---

## 1. Syntax Errors vs Exceptions

| Type | When | Example |
|---|---|---|
| **SyntaxError** | Before the program runs | `if x = 5:` |
| **Exception** | During execution (runtime) | `int("abc")` |

Exceptions can be caught and handled. Syntax errors cannot — fix them first.

---

## 2. try / except

Wrap risky code in `try`. Handle specific exceptions in `except`.

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### Catching multiple exceptions

```python
# Option 1 — separate handlers (different messages)
try:
    ...
except ValueError:
    print("Bad value")
except TypeError:
    print("Wrong type")

# Option 2 — same handler for multiple types
try:
    ...
except (ValueError, TypeError) as e:
    print(f"Input error: {e}")

# Option 3 — catch all exceptions (use sparingly)
try:
    ...
except Exception as e:
    print(f"Unexpected error: {type(e).__name__}: {e}")
```

### The `as e` clause

`as e` gives you access to the exception object:

```python
try:
    x = int("abc")
except ValueError as e:
    print(e)              # invalid literal for int() with base 10: 'abc'
    print(type(e))        # <class 'ValueError'>
    print(type(e).__name__)  # ValueError
```

---

## 3. else and finally

```python
try:
    result = 10 / int(input("Divisor: "))
except ValueError:
    print("Not a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    # runs ONLY if no exception was raised
    print(f"Success! Result: {result}")
finally:
    # runs ALWAYS — exception or not
    print("Calculation attempt finished.")
```

| Clause | Runs when |
|---|---|
| `except` | An exception matching the type was raised |
| `else` | No exception was raised in `try` |
| `finally` | Always — even if `return` or `break` is hit |

`finally` is used for cleanup: closing files, releasing resources, etc.

---

## 4. Built-in Exception Types

Python has a rich exception hierarchy. The most common:

| Exception | Cause |
|---|---|
| `ValueError` | Right type, wrong value — `int("abc")` |
| `TypeError` | Wrong type — `"2" + 2` |
| `ZeroDivisionError` | Division by zero |
| `IndexError` | List index out of range |
| `KeyError` | Dict key not found |
| `AttributeError` | Object has no such attribute |
| `FileNotFoundError` | File doesn't exist |
| `PermissionError` | No permission to access file |
| `StopIteration` | Iterator exhausted |
| `RuntimeError` | Generic runtime error |
| `NotImplementedError` | Abstract method not overridden |
| `OverflowError` | Number too large |
| `RecursionError` | Maximum recursion depth exceeded |

```python
# Hierarchy — broader exceptions catch narrower ones
# BaseException
#  └── Exception
#       ├── ValueError
#       ├── TypeError
#       ├── ArithmeticError
#       │    └── ZeroDivisionError
#       ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError
#       └── OSError
#            ├── FileNotFoundError
#            └── PermissionError
```

> **Rule:** Always catch the most specific exception first.

---

## 5. Raising Exceptions

Use `raise` to signal an error condition from your own code.

```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be an int, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"Age must be between 0 and 150, got {age}")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)   # Age must be between 0 and 150, got -5
```

### Re-raising

```python
def process(data):
    try:
        return int(data)
    except ValueError:
        print("Logging: bad input received")
        raise   # re-raises the original exception unchanged
```

---

## 6. Custom Exceptions

Create your own exception classes by inheriting from `Exception`.

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw R$ {amount:.2f} — balance is R$ {balance:.2f}"
        )


class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError(self._balance, amount)
        self._balance -= amount
        return amount


account = BankAccount(100)
try:
    account.withdraw(200)
except InsufficientFundsError as e:
    print(e)              # Cannot withdraw R$ 200.00 — balance is R$ 100.00
    print(e.balance)      # 100  — custom attributes accessible
    print(e.amount)       # 200
```

### Exception Hierarchy for a project

```python
# Base exception for your entire project
class AppError(Exception):
    pass

class ValidationError(AppError):
    pass

class DatabaseError(AppError):
    pass

class NetworkError(AppError):
    pass
```

---

## 7. Exception Chaining

Use `raise ... from ...` to attach context to a new exception.

```python
def load_config(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError(f"Config file '{path}' not found.") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"Config file '{path}' contains invalid JSON.") from e
```

The traceback will show both the original and the new exception, making debugging much easier.

---

## 8. Common Patterns

### Input validation loop

```python
def get_int(prompt, min_val=None, max_val=None):
    """Keep asking until the user enters a valid integer in range."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                raise ValueError(f"Must be >= {min_val}")
            if max_val is not None and value > max_val:
                raise ValueError(f"Must be <= {max_val}")
            return value
        except ValueError as e:
            print(f"  Invalid input: {e}. Try again.")

age = get_int("Enter your age: ", min_val=0, max_val=150)
```

### Safe file read

```python
def read_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except PermissionError:
        print(f"No permission to read: {path}")
        return None
```

### Safe dict access

```python
# Instead of:
value = my_dict[key]             # KeyError if missing

# Use:
value = my_dict.get(key)         # None if missing
value = my_dict.get(key, "default")  # default if missing

# Or explicitly:
try:
    value = my_dict[key]
except KeyError:
    value = "default"
```

### Context manager for cleanup

```python
# finally guarantees cleanup even if an exception occurs
def process_file(path):
    f = open(path)
    try:
        return f.read()
    finally:
        f.close()   # always runs — but 'with' is better
```

---

## Quick Reference

```python
# Basic structure
try:
    risky_code()
except SpecificError as e:
    handle(e)
except (Error1, Error2):
    handle_both()
else:
    runs_if_no_exception()
finally:
    always_runs()

# Raise
raise ValueError("message")
raise TypeError(f"Expected int, got {type(x).__name__}")
raise                          # re-raise current exception

# Custom exception
class MyError(Exception):
    def __init__(self, value):
        super().__init__(f"Bad value: {value}")
        self.value = value

# Exception chaining
raise NewError("msg") from original_error

# Most common exceptions
ValueError       # bad value
TypeError        # wrong type
KeyError         # missing dict key
IndexError       # list out of range
FileNotFoundError# file missing
AttributeError   # no such attribute
ZeroDivisionError# division by zero
```

---

## What's Next

Try the exercises in [`exercises/`](./exercises/).

Next: [`mini-projects/`](../mini-projects/) — build something that combines OOP, file handling, modules, and error handling.
