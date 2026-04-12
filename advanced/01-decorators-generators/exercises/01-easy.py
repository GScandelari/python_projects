# ============================================================
# advanced/01-decorators-generators/exercises/01-easy.py
# Topic: Decorators & Generators — basics
# Difficulty: Easy
# ============================================================

# Exercise 1 — Timer decorator
# ------------------------------
# Write a decorator called timer that measures how long a
# function takes to run and prints:
#   "slow_add took 0.0012s"
# Use functools.wraps so the original name/docstring is preserved.
#
# Expected:
#   @timer
#   def slow_add(a, b):
#       time.sleep(0.1)
#       return a + b
#
#   result = slow_add(3, 4)   → prints "slow_add took 0.10Xs"
#   print(result)             → 7
#   print(slow_add.__name__)  → slow_add

import functools
import time
# Write your code here


# Exercise 2 — Logger decorator
# ------------------------------
# Write a decorator called logger that prints a line before and
# after the function call with the function name and arguments:
#   Calling greet(name='Alice')
#   greet returned 'Hello, Alice!'
#
# Expected:
#   @logger
#   def greet(name):
#       return f"Hello, {name}!"
#
#   greet("Alice")

# Write your code here


# Exercise 3 — Simple generator (countdown)
# -------------------------------------------
# Write a generator function countdown(start) that yields
# integers from start down to 1.
#
# Expected:
#   for n in countdown(5):
#       print(n, end=" ")   → 5 4 3 2 1

# Write your code here


# Exercise 4 — Fibonacci generator
# ----------------------------------
# Write a generator function fibonacci() that yields the
# Fibonacci sequence indefinitely: 0, 1, 1, 2, 3, 5, 8, ...
# Then use it to print the first 10 values.
#
# Expected:
#   gen = fibonacci()
#   [next(gen) for _ in range(10)]  → [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Write your code here


# Exercise 5 — take() utility
# -----------------------------
# Write a generator function take(n, iterable) that yields
# the first n elements from any iterable (including infinite ones).
#
# Expected:
#   list(take(5, fibonacci()))   → [0, 1, 1, 2, 3]
#   list(take(3, range(100)))    → [0, 1, 2]

# Write your code here
