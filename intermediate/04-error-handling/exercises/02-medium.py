# ============================================================
# intermediate/04-error-handling/exercises/02-medium.py
# Topic: Error Handling — raising, custom exceptions, chaining
# Difficulty: Medium
# ============================================================

# Exercise 1 — Input Validation with raise
# -----------------------------------------
# Write a class Temperature with:
#   - __init__(self, value, unit="C") — unit is "C", "F", or "K"
#   - Raise ValueError if unit is not one of those three
#   - Raise ValueError if Kelvin value < 0 (absolute zero)
#   - Method to_celsius() → converts to Celsius
#   - Method to_fahrenheit() → converts to Fahrenheit
#   - __str__ → "72.5°F"
#
# Formulas:
#   C to F: (C * 9/5) + 32
#   F to C: (F - 32) * 5/9
#   K to C: K - 273.15
#
# Expected:
#   t = Temperature(100, "C")
#   print(t.to_fahrenheit())   → 212.0
#   Temperature(-5, "K")       → ValueError: Kelvin cannot be negative
#   Temperature(50, "X")       → ValueError: Invalid unit 'X'

# Write your code here


# Exercise 2 — Custom Exception Hierarchy
# ----------------------------------------
# Create an exception hierarchy for a simple e-commerce system:
#
#   ShopError (base)
#     ├── ProductNotFoundError(product_name)
#     ├── OutOfStockError(product_name, requested, available)
#     └── PaymentError(amount, reason)
#
# Each custom exception should include a meaningful __str__ message
# that uses its attributes.
#
# Then write a class Shop with:
#   - Attribute: inventory = {"Notebook": 3, "Mouse": 10, "Monitor": 1}
#   - Method: buy(product, quantity, payment) that:
#       * Raises ProductNotFoundError if product not in inventory
#       * Raises OutOfStockError if quantity > available stock
#       * Raises PaymentError if payment < total cost (Notebook=2500, Mouse=90, Monitor=1900)
#       * Otherwise deducts stock and returns a receipt string
#
# Demonstrate all four cases (success + 3 error types).

# Write your code here


# Exercise 3 — Exception Chaining
# --------------------------------
# Write a function load_user_config(path) that:
#   - Tries to read and parse a JSON file
#   - If FileNotFoundError → raise RuntimeError("Config missing") from e
#   - If json.JSONDecodeError → raise ValueError("Config corrupted") from e
#   - Returns the parsed dict on success
#
# Then write save_user_config(path, data) that:
#   - Validates data has keys: "username", "theme", "font_size"
#   - Raises KeyError with a helpful message if any key is missing
#   - Saves to JSON file, chaining any IOError as RuntimeError
#
# Demonstrate with: a missing file, a bad JSON file, and a valid file.

import json
# Write your code here


# Exercise 4 — Robust CLI Input
# ------------------------------
# Write a function get_date(prompt) that:
#   - Asks the user to enter a date in DD/MM/YYYY format
#   - Parses it with datetime.strptime
#   - Catches ValueError for bad format and re-prompts
#   - Catches any other exception and re-prompts with "Unexpected error"
#   - Returns a date object when valid
#
# Then use it to ask for a birth date and print how many days
# until the user's next birthday.

from datetime import datetime, date, timedelta
# Write your code here


# Exercise 5 — Retry Decorator (intro)
# --------------------------------------
# Write a function retry(func, times=3) that:
#   - Calls func() up to `times` times
#   - If func() raises an exception, prints the error and tries again
#   - Returns the result if successful
#   - Raises RuntimeError("All attempts failed") if all retries fail
#
# Test it with a function that randomly raises ValueError
# (use random.random() < 0.6 to simulate 60% failure rate).
# With seed=1, it should succeed within a few tries.

import random
# Write your code here
