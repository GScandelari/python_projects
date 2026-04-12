# ============================================================
# advanced/01-decorators-generators/solutions/02-medium-solution.py
# ============================================================

import functools
import time
import random

# ----------------------------------------------------------
# Exercise 1 — retry decorator with arguments
# ----------------------------------------------------------
def retry(times=3, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exc = e
                    print(f"  Attempt {attempt}/{times} failed: {e}")
            raise last_exc
        return wrapper
    return decorator

random.seed(42)
call_count = 0

@retry(times=5, exceptions=(ValueError,))
def flaky():
    global call_count
    call_count += 1
    if random.random() < 0.6:
        raise ValueError("Random failure")
    return "Success!"

print("\n--- retry demo ---")
result = flaky()
print(f"Result: {result}  (took {call_count} attempt(s))")


# ----------------------------------------------------------
# Exercise 2 — memoize decorator
# ----------------------------------------------------------
def memoize(func):
    @functools.wraps(func)
    def wrapper(*args):
        if args not in wrapper.cache:
            wrapper.cache[args] = func(*args)
        return wrapper.cache[args]
    wrapper.cache = {}
    return wrapper

@memoize
def slow_fib(n):
    if n <= 1:
        return n
    return slow_fib(n - 1) + slow_fib(n - 2)

print("\n--- memoize demo ---")
start = time.perf_counter()
print(slow_fib(35))   # 9227465 — fast because each value cached
elapsed = time.perf_counter() - start
print(f"Computed in {elapsed:.4f}s")
print(f"Cache size: {len(slow_fib.cache)} entries")


# ----------------------------------------------------------
# Exercise 3 — Generator pipeline
# ----------------------------------------------------------
def read_numbers(data):
    yield from data

def filter_even(gen):
    for n in gen:
        if n % 2 == 0:
            yield n

def square(gen):
    for n in gen:
        yield n ** 2

print("\n--- generator pipeline ---")
pipeline = square(filter_even(read_numbers(range(1, 11))))
print(list(pipeline))   # [4, 16, 36, 64, 100]


# ----------------------------------------------------------
# Exercise 4 — running_average with send()
# ----------------------------------------------------------
def running_average():
    total = 0
    count = 0
    while True:
        value = yield (total / count if count else 0.0)
        if value is None:
            return
        total += value
        count += 1

print("\n--- running_average demo ---")
gen = running_average()
next(gen)   # prime
print(gen.send(10))   # 10.0
print(gen.send(20))   # 15.0
print(gen.send(30))   # 20.0


# ----------------------------------------------------------
# Exercise 5 — stacked decorators
# ----------------------------------------------------------
def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

def exclaim(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!!!"
    return wrapper

@exclaim
@uppercase
def greet(name):
    return f"hello, {name}"

print("\n--- stacked decorators ---")
print(greet("alice"))   # HELLO, ALICE!!!
