# ============================================================
# intermediate/04-error-handling/exercises/01-easy.py
# Topic: Error Handling — try/except, common exceptions
# Difficulty: Easy
# ============================================================

# Exercise 1 — Safe Division
# --------------------------
# Write a function safe_divide(a, b) that:
#   - Returns a / b if b != 0
#   - Catches ZeroDivisionError and returns None
#   - Catches TypeError (non-numeric inputs) and returns None
#   - Prints a descriptive message for each error type
#
# Expected:
#   safe_divide(10, 2)   → 5.0
#   safe_divide(10, 0)   → None  (prints: "Error: division by zero")
#   safe_divide("a", 2)  → None  (prints: "Error: invalid types")

# Write your code here


# Exercise 2 — Safe Integer Input
# --------------------------------
# Write a function get_positive_int(prompt) that:
#   - Keeps asking the user until they enter a positive integer
#   - Catches ValueError for non-numeric input
#   - Prints "Please enter a positive whole number." on bad input
#   - Returns the valid integer
#
# Expected interaction:
#   Enter a number: hello   → Please enter a positive whole number.
#   Enter a number: -5      → Please enter a positive whole number.
#   Enter a number: 7       → returns 7

# Write your code here


# Exercise 3 — Safe Dictionary Access
# -------------------------------------
# Given the dict below, write a function get_grade(students, name) that:
#   - Returns the grade if the name exists
#   - Catches KeyError and returns "Student not found"
#   - Is case-insensitive (convert name to title case before lookup)
#
# students = {"Alice": 92, "Bob": 78, "Carol": 85}
#
# Expected:
#   get_grade(students, "alice")   → 92
#   get_grade(students, "Dave")    → "Student not found"
#   get_grade(students, "BOB")     → 78

students = {"Alice": 92, "Bob": 78, "Carol": 85}
# Write your code here


# Exercise 4 — try / except / else / finally
# -------------------------------------------
# Write a function read_first_line(filepath) that:
#   - Tries to open and read the first line of a file
#   - On FileNotFoundError: prints "File not found: {path}" and returns None
#   - On PermissionError: prints "Cannot read: {path}" and returns None
#   - else: prints "Read successfully." and returns the first line (stripped)
#   - finally: always prints "Attempted to read: {path}"
#
# Test it with a file that exists (e.g. this file) and one that doesn't.

import os
THIS_FILE = __file__
MISSING_FILE = os.path.join(os.path.dirname(__file__), "missing.txt")
# Write your code here


# Exercise 5 — Catching Multiple Exceptions
# ------------------------------------------
# Write a function parse_number(value) that:
#   - Tries to convert value to float
#   - If value is None → catches TypeError, returns 0.0
#   - If value is a string that can't convert → catches ValueError, returns 0.0
#   - Otherwise returns the float
#
# Expected:
#   parse_number("3.14")   → 3.14
#   parse_number("hello")  → 0.0
#   parse_number(None)     → 0.0
#   parse_number(42)       → 42.0

# Write your code here
