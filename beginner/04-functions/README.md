# Functions in Python

Functions let you package a block of code under a name so you can reuse it, test it independently, and give it a clear purpose. They are the primary tool for avoiding repetition and making programs readable.

## Table of Contents

- [Defining and Calling Functions](#1-defining-and-calling-functions)
- [Parameters and Arguments](#2-parameters-and-arguments)
- [Return Values](#3-return-values)
- [Scope](#4-scope)
- [Lambda Functions](#5-lambda-functions)
- [Docstrings](#6-docstrings)
- [Common Patterns](#7-common-patterns)
- [Quick Reference](#quick-reference)
- [What's Next](#whats-next)

---

## 1. Defining and Calling Functions

Use the `def` keyword followed by the function name, parentheses, and a colon. The body must be indented.

```python
def greet(name):
    return f"Hello, {name}!"

# calling the function
message = greet("Alice")
print(message)   # Hello, Alice!
```

**`return` vs `print`** — this is the most important distinction for beginners:

```python
def add_print(a, b):
    print(a + b)       # outputs 7, but returns None

def add_return(a, b):
    return a + b       # returns 7, caller decides what to do with it

result = add_return(3, 4)
print(result * 2)      # 14 — only possible because we returned the value

result2 = add_print(3, 4)   # prints 7
print(result2)              # None — nothing to work with
```

> **Rule:** Prefer `return` over `print` inside functions. Print at the boundary, not in the middle.

---

## 2. Parameters and Arguments

| Term | Meaning |
|---|---|
| **Parameter** | Variable in the function definition |
| **Argument** | Value passed when calling the function |

### Positional Arguments

Matched by order — first argument goes to first parameter.

```python
def power(base, exponent):
    return base ** exponent

print(power(2, 10))   # 1024 — base=2, exponent=10
print(power(10, 2))   # 100 — base=10, exponent=2
```

### Keyword Arguments

Matched by name — order does not matter.

```python
print(power(exponent=3, base=5))   # 125
```

### Default Values

Use `=` in the definition to set a default. Parameters with defaults must come **after** those without.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Bob"))               # Hello, Bob!
print(greet("Bob", "Good morning"))  # Good morning, Bob!
```

> **Warning:** Never use a mutable object (list, dict) as a default value — it is created once and shared across all calls. Use `None` instead:
>
> ```python
> # Bug
> def add_item(item, lst=[]):
>     lst.append(item)
>     return lst
>
> # Fix
> def add_item(item, lst=None):
>     if lst is None:
>         lst = []
>     lst.append(item)
>     return lst
> ```

---

## 3. Return Values

### Single Value

```python
def square(n):
    return n ** 2

print(square(7))   # 49
```

### Multiple Values (as a tuple)

```python
def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return smallest, largest   # returns a tuple

low, high = min_max([4, 7, 1, 9, 3])   # tuple unpacking
print(f"Min: {low}, Max: {high}")       # Min: 1, Max: 9
```

### Returning `None`

A function with no `return` statement (or a bare `return`) implicitly returns `None`.

```python
def do_nothing():
    pass

print(do_nothing())   # None
```

---

## 4. Scope

**Local scope:** variables created inside a function exist only there.  
**Global scope:** variables created outside any function.

```python
x = 100   # global

def show():
    x = 42   # local — different variable, shadows the global
    print(f"Inside: {x}")

show()
print(f"Outside: {x}")   # still 100
```

### The `global` Keyword

Allows modifying a global variable from inside a function. Avoid this — it creates hidden dependencies.

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)   # 1
```

> **Best practice:** Pass values as arguments and return results instead of using `global`.

---

## 5. Lambda Functions

A `lambda` is a compact anonymous function limited to a single expression.

```python
# Syntax: lambda parameters: expression

square = lambda x: x ** 2
print(square(5))   # 25
```

Lambdas shine when used inline as arguments:

```python
students = [("Alice", 88), ("Bob", 72), ("Carol", 95)]

# Sort by grade descending
ranked = sorted(students, key=lambda s: s[1], reverse=True)
print(ranked)   # [('Carol', 95), ('Alice', 88), ('Bob', 72)]
```

**When to use `lambda` vs `def`:**

| | `def` | `lambda` |
|---|---|---|
| Multiple statements | Yes | No |
| Docstring | Yes | No |
| Best for | Any reusable function | Short inline callbacks |

---

## 6. Docstrings

A docstring is a string placed as the first statement in a function. It documents purpose, parameters, and return values. Access it with `help()` or `.__doc__`.

```python
def celsius_to_fahrenheit(c):
    """Convert a temperature from Celsius to Fahrenheit.

    Args:
        c (float): Temperature in Celsius.

    Returns:
        float: Equivalent temperature in Fahrenheit.

    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return (c * 9 / 5) + 32

help(celsius_to_fahrenheit)
print(celsius_to_fahrenheit(37))   # 98.6
```

---

## 7. Common Patterns

### Pure Functions

A pure function always returns the same output for the same input and has no side effects. Prefer these — they are easy to test and reason about.

```python
# Pure — no side effects
def add(a, b):
    return a + b

# Impure — side effect (print)
def add_and_log(a, b):
    result = a + b
    print(f"Adding {a} + {b} = {result}")   # side effect
    return result
```

### Functions as Arguments

Functions can be passed to other functions:

```python
def apply(func, value):
    return func(value)

print(apply(square, 6))          # 36
print(apply(lambda x: x + 1, 9))  # 10
```

### Recursion

A function that calls itself. Requires a **base case** to stop.

```python
def factorial(n):
    """Return n! — the product of all integers from 1 to n."""
    if n < 0:
        return None
    if n == 0:          # base case
        return 1
    return n * factorial(n - 1)   # recursive call

print(factorial(5))   # 120  → 5 * 4 * 3 * 2 * 1
```

---

## Quick Reference

```python
# Define
def name(param1, param2="default"):
    """Docstring."""
    return value

# Call
result = name(arg1)              # positional
result = name(param2=val)        # keyword

# Multiple return
def f(): return 1, 2
a, b = f()

# Lambda
fn = lambda x, y: x + y

# Scope
x = 10              # global
def f():
    x = 5           # local (does not affect global)

# Recursion pattern
def recurse(n):
    if n == 0:      # base case
        return ...
    return recurse(n - 1)
```

---

## What's Next

Head to the [`exercises/`](./exercises/) folder and try the problems — easy through challenge — before looking at the solutions.

Next concept: [`05-string-manipulation`](../05-string-manipulation/)