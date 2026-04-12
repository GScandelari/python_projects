# ============================================================
# advanced/01-decorators-generators/exercises/02-medium.py
# Topic: Decorators & Generators — intermediate patterns
# Difficulty: Medium
# ============================================================

import functools
import time

# Exercise 1 — retry decorator with arguments
# --------------------------------------------
# Write a decorator factory retry(times=3, exceptions=(Exception,))
# that retries a function up to `times` times if it raises one
# of the given exception types. After all retries fail, raise
# the last exception. Use functools.wraps.
#
# Expected:
#   @retry(times=3, exceptions=(ValueError,))
#   def flaky():
#       ...   # raises ValueError 2 times then succeeds
#
#   result = flaky()   → succeeds on 3rd attempt

# Write your code here


# Exercise 2 — cache decorator (memoize)
# ----------------------------------------
# Write a decorator called memoize that caches a function's
# return value based on its arguments. Subsequent calls with
# the same arguments return the cached result without re-running
# the function.
#
# Expected:
#   @memoize
#   def slow_fib(n):
#       if n <= 1: return n
#       return slow_fib(n-1) + slow_fib(n-2)
#
#   slow_fib(35)   → fast (only computes each value once)
#   slow_fib.cache → {(0,): 0, (1,): 1, (2,): 1, ...}

# Write your code here


# Exercise 3 — Generator pipeline
# ---------------------------------
# Write three generator functions that form a pipeline:
#
#   read_numbers(data) — yields each integer from a list
#   filter_even(gen)   — yields only even numbers from gen
#   square(gen)        — yields the square of each value from gen
#
# Then chain them: squares of even numbers from [1..10]
#
# Expected:
#   list(pipeline) → [4, 16, 36, 64, 100]

# Write your code here


# Exercise 4 — Running average with send()
# -----------------------------------------
# Write a generator function running_average() that:
#   - Yields the current average each time a new value is sent
#   - Prime it with next() before sending values
#
# Expected:
#   gen = running_average()
#   next(gen)           # prime
#   print(gen.send(10)) → 10.0
#   print(gen.send(20)) → 15.0
#   print(gen.send(30)) → 20.0

# Write your code here


# Exercise 5 — Stacked decorators
# ---------------------------------
# Create two decorators:
#   uppercase  — converts the string return value to uppercase
#   exclaim    — appends "!!!" to the string return value
#
# Apply both to a function and verify that decorator order matters.
#
# Expected:
#   @exclaim
#   @uppercase
#   def greet(name): return f"hello, {name}"
#
#   greet("alice") → "HELLO, ALICE!!!"

# Write your code here
