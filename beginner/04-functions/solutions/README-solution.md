# Solutions Guide — 04-functions

This document explains the concepts behind each exercise and highlights common mistakes beginners make with functions.

---

## What Each Exercise Reinforces

### Exercise 1 — `greet(name)`
**Concept:** Basic function definition and `return`.  
The key distinction here is **returning vs printing**. A function that returns a value is reusable — its result can be stored, passed to another function, or used in an expression. A function that only prints is a dead end.

### Exercise 2 — `area_rectangle(width, height)`
**Concept:** Multiple parameters, numeric return value.  
Functions can accept any number of parameters. Here both are required (no defaults). The return value is a number that can be used in further calculations.

### Exercise 3 — `is_even(n)`
**Concept:** Boolean return, modulo operator.  
`n % 2 == 0` is already a boolean expression — you can return it directly without an `if/else`. This is cleaner than:
```python
# Verbose (unnecessary)
if n % 2 == 0:
    return True
else:
    return False
```

### Exercise 4 — `celsius_to_fahrenheit(c)`
**Concept:** Formula-based functions, float division.  
Using `9/5` (not `9//5`) ensures float division, giving precise results. Integer division `9//5 = 1` would silently produce wrong answers.

### Exercise 5 — `max_of_three(a, b, c)`
**Concept:** Manual comparison pattern (scan algorithm).  
The "assume first is largest, compare the rest" pattern is the foundation of many algorithms. It avoids built-ins and shows how comparisons work under the hood.

---

## `def` vs `lambda` — Side-by-Side Reference

| Feature | `def` | `lambda` |
|---|---|---|
| Syntax | `def name(params): ...` | `lambda params: expression` |
| Body | Multiple statements | Single expression only |
| Has docstring | Yes | No |
| Has a name | Yes | Anonymous (can assign to variable) |
| Best for | Any reusable function | Short, throwaway functions |

```python
# Equivalent definitions
def square(x):
    return x * x

square = lambda x: x * x
```

---

## Common Beginner Mistakes

### 1. Forgetting `return` (function silently returns `None`)
```python
# Bug: no return
def add(a, b):
    a + b          # result is computed but thrown away

result = add(3, 4)
print(result)      # None  ← not 7!

# Fix:
def add(a, b):
    return a + b
```

### 2. Printing instead of returning
```python
# Bug: prints inside, can't use the result elsewhere
def double(n):
    print(n * 2)   # you can't do math with None

result = double(5) + 1   # TypeError: unsupported operand type(s)

# Fix: return the value, let the caller decide whether to print
def double(n):
    return n * 2
```

### 3. Mutable default argument
```python
# Bug: the list is created ONCE and reused across all calls
def append_item(item, lst=[]):
    lst.append(item)
    return lst

print(append_item(1))   # [1]
print(append_item(2))   # [1, 2]  ← unexpected!

# Fix: use None as default, create inside the function
def append_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

### 4. Confusing local and global scope
```python
x = 10

def change_x():
    x = 99    # creates a NEW local variable, does not touch global x

change_x()
print(x)      # 10 — global x unchanged
```

### 5. Calling a function before defining it
```python
# Bug: greet is not yet defined at the point of the call
result = greet("Alice")   # NameError

def greet(name):
    return f"Hello, {name}!"

# Fix: define functions before calling them (or use a main guard)
```

### 6. Forgetting parentheses when calling a function
```python
def greet(name):
    return f"Hello, {name}!"

# Bug: refers to the function object, doesn't call it
print(greet)           # <function greet at 0x...>

# Fix:
print(greet("Alice"))  # Hello, Alice!
```

---

## Further Reading

- [README](../README.md) — Full concept explanations
- [Exercises](../exercises/01-easy.py) — Try before looking here
- [Solutions](./01-easy-solution.py) — Annotated working code
