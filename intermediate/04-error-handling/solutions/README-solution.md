# Solutions Guide — 04-error-handling

---

## What Each Exercise Reinforces

### Easy 1 — `safe_divide`
**Concept:** Catching specific exceptions in order.  
Catch the most specific exception first. `ZeroDivisionError` is a subclass of `ArithmeticError` — catching `Exception` would also work but is too broad.

### Easy 2 — `get_positive_int`
**Concept:** Validation loop with `try/except`.  
The `while True` + `return` pattern is idiomatic for "keep asking until valid". Never use a flag variable like `valid = False` when `return` does the job.

### Easy 3 — `get_grade`
**Concept:** `KeyError` vs `dict.get()`.  
Both work, but catching `KeyError` is better when you want to do something specific on miss (log, raise, return a typed default). `dict.get(key, default)` is better for simple one-liners.

### Easy 4 — `try/except/else/finally`
**Concept:** The full `try` block.  
`else` is underused but valuable — it separates "what to do on success" from "what to do on error". `finally` is the guarantee clause — perfect for logging, cleanup, or releasing resources.

### Easy 5 — `parse_number`
**Concept:** Catching multiple exceptions in a tuple.  
`except (TypeError, ValueError)` is cleaner than two identical `except` clauses. Use it when both errors deserve the same treatment.

### Medium 1 — `Temperature` with `raise`
**Concept:** Input validation at construction time.  
Fail fast — raise in `__init__` so invalid objects never exist. A `Temperature(-5, "K")` that silently creates itself is far worse than one that immediately errors.

### Medium 2 — Custom Exception Hierarchy
**Concept:** Domain-specific exceptions with custom attributes.  
The hierarchy (`ShopError → ProductNotFoundError`) lets callers catch broadly (`except ShopError`) or narrowly (`except OutOfStockError`). Custom attributes (`e.available`, `e.requested`) give callers structured data, not just a message.

### Medium 3 — Exception Chaining
**Concept:** `raise X from Y`.  
Chaining preserves the original traceback. A caller that catches `RuntimeError("Config missing")` can still inspect `e.__cause__` to see the original `FileNotFoundError`. Never swallow the root cause.

### Challenge 3 — Context Manager
**Concept:** `__enter__` / `__exit__` protocol.  
`__exit__(self, exc_type, exc_val, exc_tb)` — if an exception occurred, these are non-None. Return `True` to suppress it, `False` (or `None`) to re-raise. Always re-raise unless you have a good reason not to.

---

## Exception Hierarchy (simplified)

```
BaseException
 └── Exception
      ├── ValueError          ← bad value, right type
      ├── TypeError           ← wrong type entirely
      ├── AttributeError      ← object has no such attribute
      ├── NameError           ← variable not defined
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError     ← list[99] on list of 3
      │    └── KeyError       ← dict["missing"]
      ├── OSError
      │    ├── FileNotFoundError
      │    └── PermissionError
      └── RuntimeError
           └── RecursionError
```

---

## Common Beginner Mistakes

### 1. Catching `Exception` (too broad)
```python
# Bug: catches everything including bugs in YOUR code
try:
    result = compute()
except Exception:
    pass   # silently swallows a bug!

# Fix: catch only what you expect
try:
    result = compute()
except ValueError as e:
    log(e)
```

### 2. Bare `except:` — catches even KeyboardInterrupt
```python
# Bug: user can't even Ctrl+C out
try:
    ...
except:
    pass

# Fix: always name the exception
try:
    ...
except Exception:
    pass
```

### 3. Raising string instead of exception
```python
raise "Something went wrong"   # TypeError: exceptions must be classes
raise ValueError("Something went wrong")   # correct
```

### 4. Using exceptions for flow control
```python
# Bug: using exceptions as if/else — slow and unreadable
try:
    value = my_dict[key]
except KeyError:
    value = "default"

# Fix for simple cases: use dict.get()
value = my_dict.get(key, "default")
```

### 5. Forgetting `from e` in exception chaining
```python
# Bug: original traceback is lost
except FileNotFoundError:
    raise RuntimeError("Config missing")   # __cause__ is None

# Fix:
except FileNotFoundError as e:
    raise RuntimeError("Config missing") from e
```

### 6. Mutating state before a risky operation
```python
# Bug: balance is already reduced when the error fires
def withdraw(self, amount):
    self._balance -= amount        # mutated first!
    if amount > self._balance:
        raise InsufficientFundsError(...)   # too late — damage done

# Fix: validate BEFORE mutating
def withdraw(self, amount):
    if amount > self._balance:
        raise InsufficientFundsError(self._balance, amount)
    self._balance -= amount
```
