# Decorators & Generators

Two of Python's most powerful features for writing expressive, reusable, and memory-efficient code.

## Table of Contents

- [Decorators](#decorators)
  - [What is a decorator?](#1-what-is-a-decorator)
  - [functools.wraps](#2-functoolswraps)
  - [Decorators with arguments](#3-decorators-with-arguments)
  - [Class-based decorators](#4-class-based-decorators)
  - [Stacking decorators](#5-stacking-decorators)
- [Generators](#generators)
  - [yield basics](#6-yield-basics)
  - [Generator expressions](#7-generator-expressions)
  - [send() and two-way communication](#8-send-and-two-way-communication)
  - [yield from and delegation](#9-yield-from-and-delegation)
  - [Infinite generators](#10-infinite-generators)
- [Quick Reference](#quick-reference)
- [What's Next](#whats-next)

---

## Decorators

### 1. What is a decorator?

A decorator is a function that **wraps another function**, adding behaviour before and/or after it runs — without modifying its source code.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Before
# Hello, Alice!
# After
```

`@my_decorator` above `greet` is syntactic sugar for `greet = my_decorator(greet)`.

---

### 2. functools.wraps

Without `@wraps`, the wrapper function replaces the original's `__name__` and `__doc__`. Always use it:

```python
import functools

def timer(func):
    @functools.wraps(func)          # preserves __name__, __doc__, __module__
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    """Return sum of 0..n."""
    return sum(range(n))

print(slow_sum(1_000_000))
print(slow_sum.__name__)   # slow_sum  (not 'wrapper')
print(slow_sum.__doc__)    # Return sum of 0..n.
```

---

### 3. Decorators with arguments

Add another layer of nesting — the outermost function receives the arguments:

```python
import functools

def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say(message):
    print(message)

say("Hello!")
# Hello!
# Hello!
# Hello!
```

---

### 4. Class-based decorators

Use a class with `__call__` when the decorator needs to maintain state:

```python
import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} called {self.count} time(s)")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    return f"Hello, {name}!"

greet("Alice")   # greet called 1 time(s)
greet("Bob")     # greet called 2 time(s)
print(greet.count)   # 2
```

---

### 5. Stacking decorators

Decorators apply **bottom-up** (innermost first):

```python
import functools, time

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"
    return wrapper

def upper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@bold      # applied second
@upper     # applied first
def greet(name):
    return f"hello, {name}"

print(greet("alice"))   # **HELLO, ALICE**
```

---

## Generators

### 6. yield basics

A generator function uses `yield` instead of `return`. It pauses and resumes, producing values one at a time:

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(3)
print(next(gen))   # 3
print(next(gen))   # 2
print(next(gen))   # 1
# next(gen) would raise StopIteration

# Use in a for loop — StopIteration handled automatically
for value in countdown(5):
    print(value, end=" ")   # 5 4 3 2 1
```

---

### 7. Generator expressions

Like list comprehensions but lazy — values computed on demand:

```python
import sys

squares_list = [n ** 2 for n in range(10_000)]
squares_gen  = (n ** 2 for n in range(10_000))

print(sys.getsizeof(squares_list))   # ~87,616 bytes
print(sys.getsizeof(squares_gen))    # ~104 bytes

# sum() consumes the generator without storing the list
total = sum(n ** 2 for n in range(1_000_000))
```

---

### 8. send() and two-way communication

`send(value)` resumes the generator AND sends a value back in — the `yield` expression evaluates to it:

```python
def accumulator():
    total = 0
    while True:
        value = yield total    # yield sends total out; receives next value
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)          # prime the generator (advance to first yield)
print(gen.send(10))   # 10
print(gen.send(20))   # 30
print(gen.send(5))    # 35
```

---

### 9. yield from and delegation

`yield from` delegates to a sub-generator, forwarding `next()`, `send()`, and `throw()` calls:

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)   # delegate recursively
        else:
            yield item

data = [1, [2, [3, 4], 5], [6, 7]]
print(list(flatten(data)))   # [1, 2, 3, 4, 5, 6, 7]
```

---

### 10. Infinite generators

Generators can run forever — pull only what you need:

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def take(n, iterable):
    """Return first n elements from an iterable."""
    for i, val in enumerate(iterable):
        if i >= n:
            return
        yield val

print(list(take(10, fibonacci())))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

## Quick Reference

```python
# Basic decorator
def deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper

# Decorator with arguments
def deco(arg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Generator function
def gen():
    yield value         # pause and produce
    value = yield      # pause, produce None, receive via send()
    yield from other   # delegate to sub-generator

# Useful generator patterns
next(gen)              # advance one step
gen.send(value)        # send value in, receive yielded value
list(gen)              # exhaust into a list
itertools.islice(gen, n)  # take first n values
```

---

## What's Next

Try the exercises in [`exercises/`](./exercises/) — build real decorators and generator pipelines.

Next concept: [`02-concurrency-async`](../02-concurrency-async/)
