# ============================================================
# intermediate/04-error-handling/exercises/03-challenge.py
# Topic: Error Handling — advanced patterns
# Difficulty: Challenge
# ============================================================

import json
import csv
import os
from pathlib import Path
from datetime import datetime

EXERCISES_DIR = Path(os.path.dirname(__file__))


# Exercise 1 — Validated Data Class
# ------------------------------------
# Build a class Person with strict validation on every attribute:
#
#   name (str):  non-empty, only letters and spaces, title-cased
#   age (int):   0–150
#   email (str): must contain exactly one "@" and at least one "." after "@"
#   height (float): 0.0–3.0 meters
#
# Rules:
#   - Validate in __init__ — raise ValueError with specific messages
#   - Implement __str__ and __repr__
#   - Implement a class method from_dict(data) that:
#       * Takes a dict {"name":..., "age":..., "email":..., "height":...}
#       * Catches missing keys (KeyError) and wraps in ValueError
#       * Creates and returns a Person instance
#
# Demonstrate: valid person, 4 validation failures, from_dict with missing key.

# Write your code here


# Exercise 2 — Safe CSV Processor
# ---------------------------------
# Write a function process_grades_csv(input_path, output_path) that:
#   - Reads a CSV with columns: name, grade1, grade2, grade3
#   - For each row, computes the average of the three grades
#   - Handles per-row errors WITHOUT stopping the whole process:
#       * Missing columns → log warning, skip row
#       * Non-numeric grade → log warning, use 0 for that grade
#       * Grade out of range (0-10) → log warning, clamp to 0-10
#   - Writes valid processed rows to output_path with columns:
#     name, grade1, grade2, grade3, average, status (Pass/Fail, cutoff=6.0)
#   - Returns a summary dict: {processed, skipped, warnings}
#
# Create a test CSV with at least 2 good rows and 2 problematic rows,
# then call the function and print the summary.

# Write your code here


# Exercise 3 — Context Manager
# ------------------------------
# Implement a custom context manager class Timer that:
#   - Records the start time on __enter__
#   - Records the end time and computes elapsed time on __exit__
#   - Prints: "Elapsed: X.XXXs" on exit
#   - If an exception occurs inside the block, prints:
#     "Failed after X.XXXs — {ExceptionType}: {message}"
#     and does NOT suppress the exception (re-raises it)
#
# Usage:
#   with Timer():
#       result = some_slow_operation()
#
#   with Timer():
#       raise ValueError("something went wrong")
#
# Demonstrate with:
#   a) A loop that does 1_000_000 additions (successful)
#   b) A block that raises a ValueError (failed)

import time
# Write your code here
