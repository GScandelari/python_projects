# ============================================================
# advanced/01-decorators-generators/solutions/01-easy-solution.py
# ============================================================

import functools
import time

# ----------------------------------------------------------
# Exercise 1 — timer decorator
# ----------------------------------------------------------
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_add(a, b):
    """Add two numbers with a small delay."""
    time.sleep(0.1)
    return a + b

result = slow_add(3, 4)
print(result)              # 7
print(slow_add.__name__)   # slow_add  (not 'wrapper')
print(slow_add.__doc__)    # Add two numbers with a small delay.


# ----------------------------------------------------------
# Exercise 2 — logger decorator
# ----------------------------------------------------------
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arg_str = ", ".join(
            [repr(a) for a in args] +
            [f"{k}={v!r}" for k, v in kwargs.items()]
        )
        print(f"Calling {func.__name__}({arg_str})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@logger
def greet(name):
    return f"Hello, {name}!"

greet("Alice")
# Calling greet('Alice')
# greet returned 'Hello, Alice!'


# ----------------------------------------------------------
# Exercise 3 — countdown generator
# ----------------------------------------------------------
def countdown(start):
    while start > 0:
        yield start
        start -= 1

for n in countdown(5):
    print(n, end=" ")   # 5 4 3 2 1
print()


# ----------------------------------------------------------
# Exercise 4 — fibonacci generator
# ----------------------------------------------------------
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
first_ten = [next(gen) for _ in range(10)]
print(first_ten)   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# ----------------------------------------------------------
# Exercise 5 — take() utility
# ----------------------------------------------------------
def take(n, iterable):
    for i, val in enumerate(iterable):
        if i >= n:
            return
        yield val

print(list(take(5, fibonacci())))     # [0, 1, 1, 2, 3]
print(list(take(3, range(100))))      # [0, 1, 2]
