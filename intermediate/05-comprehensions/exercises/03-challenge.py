# ============================================================
# intermediate/05-comprehensions/exercises/03-challenge.py
# Topic: Comprehensions — advanced patterns, generators
# Difficulty: Challenge
# ============================================================

# Exercise 1 — Pipeline of comprehensions
# ----------------------------------------
# Given the raw data below, produce a clean list of dicts using
# comprehensions ONLY (no explicit loops):
#   a) Strip whitespace from all string values
#   b) Convert "price" to float
#   c) Keep only products where price > 100
#   d) Add a new key "discounted" = price * 0.9 (rounded to 2 dec)
#
# raw = [
#     {"name": " Notebook ", "price": "2500.00", "stock": 10},
#     {"name": " Mouse    ", "price": "89.90",   "stock": 50},
#     {"name": " Monitor  ", "price": "1899.00", "stock": 5},
#     {"name": " Keyboard ", "price": "199.90",  "stock": 30},
#     {"name": " USB Hub  ", "price": "45.00",   "stock": 100},
# ]
#
# Expected:
#   [{'name': 'Notebook', 'price': 2500.0, 'stock': 10, 'discounted': 2250.0},
#    {'name': 'Monitor',  'price': 1899.0, 'stock': 5,  'discounted': 1709.1},
#    {'name': 'Keyboard', 'price': 199.9,  'stock': 30, 'discounted': 179.91}]

raw = [
    {"name": " Notebook ", "price": "2500.00", "stock": 10},
    {"name": " Mouse    ", "price": "89.90",   "stock": 50},
    {"name": " Monitor  ", "price": "1899.00", "stock": 5},
    {"name": " Keyboard ", "price": "199.90",  "stock": 30},
    {"name": " USB Hub  ", "price": "45.00",   "stock": 100},
]
# Write your code here


# Exercise 2 — Invert and group
# ------------------------------
# Given the dict below mapping student → list of subjects,
# invert it to map subject → list of students enrolled.
# Use comprehensions (you may use a helper set for unique subjects).
#
# enrollment = {
#     "Alice": ["Math", "Physics", "CS"],
#     "Bob":   ["Math", "Biology"],
#     "Carol": ["CS", "Biology", "Chemistry"],
#     "Dave":  ["Physics", "CS"],
# }
#
# Expected:
#   {
#     'Math':      ['Alice', 'Bob'],
#     'Physics':   ['Alice', 'Dave'],
#     'CS':        ['Alice', 'Carol', 'Dave'],
#     'Biology':   ['Bob', 'Carol'],
#     'Chemistry': ['Carol'],
#   }

enrollment = {
    "Alice": ["Math", "Physics", "CS"],
    "Bob":   ["Math", "Biology"],
    "Carol": ["CS", "Biology", "Chemistry"],
    "Dave":  ["Physics", "CS"],
}
# Write your code here


# Exercise 3 — Generator expression efficiency
# ---------------------------------------------
# Using GENERATOR EXPRESSIONS (not list comprehensions):
#   a) Find the first number in range(1, 1_000_000) divisible by 7, 11, and 13
#      Use next() with a generator expression.
#   b) Compute the sum of squares of all odd numbers from 1 to 999_999
#      using a generator expression (NOT a list — memory matters here).
#   c) Check if ALL words in the list below have length > 3,
#      using all() with a generator expression.
#      words = ["Python", "is", "cool"]  → False (because "is" has length 2)
#
# Print all three results.

words = ["Python", "is", "cool"]
# Write your code here
