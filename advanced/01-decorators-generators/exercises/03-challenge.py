# ============================================================
# advanced/01-decorators-generators/exercises/03-challenge.py
# Topic: Decorators & Generators — advanced patterns
# Difficulty: Challenge
# ============================================================

import functools
import time

# Exercise 1 — Class-based decorator with state
# -----------------------------------------------
# Write a class-based decorator RateLimit(calls, period) that:
#   - Allows at most `calls` calls within `period` seconds
#   - Raises RuntimeError("Rate limit exceeded") if the limit is hit
#   - Resets the count after `period` seconds have passed
#
# Use functools.update_wrapper to preserve the decorated function's metadata.
#
# Expected:
#   @RateLimit(calls=3, period=5)
#   def api_call(endpoint):
#       return f"Data from {endpoint}"
#
#   api_call("/users")   → "Data from /users"
#   api_call("/users")   → "Data from /users"
#   api_call("/users")   → "Data from /users"
#   api_call("/users")   → RuntimeError: Rate limit exceeded

# Write your code here


# Exercise 2 — yield from recursive flattener
# ---------------------------------------------
# Write a generator function deep_flatten(nested) that flattens
# a list of ARBITRARY depth using `yield from` recursion.
# Any non-list item is yielded directly.
#
# Expected:
#   deep_flatten([1, [2, [3, [4, 5]], 6], 7])
#   → [1, 2, 3, 4, 5, 6, 7]
#
#   deep_flatten([[[1]], [[2, 3]], 4])
#   → [1, 2, 3, 4]

# Write your code here


# Exercise 3 — Coroutine-based data pipeline
# --------------------------------------------
# Build a pipeline using coroutines (generators with send()):
#
#   broadcaster(targets) — receives values via send() and
#                          forwards each to all targets in the list
#   filter_gt(threshold, target) — receives values, forwards only
#                                   those > threshold to target
#   printer(prefix)     — receives values and prints "{prefix}: {value}"
#
# Demonstrate:
#   - Create two printers: "HIGH" (threshold 50) and "ALL"
#   - Feed the values [10, 60, 30, 80, 45] through the broadcaster
#
# Expected output (order may vary per printer):
#   ALL: 10
#   ALL: 60
#   HIGH: 60
#   ALL: 30
#   ALL: 80
#   HIGH: 80
#   ALL: 45

# Hint: use a helper `coroutine` decorator that primes (calls next()) automatically.

# Write your code here
