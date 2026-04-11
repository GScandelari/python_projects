# beginner/03-data-structures/exercises/02-medium.py
# Topic: Lists, Tuples, Dictionaries, Sets — Medium Exercises
# Complete each exercise by replacing the placeholder with your code.
# Do NOT use built-in aggregate functions (sum, min, max, sorted) unless
# explicitly allowed by the exercise.

# =============================================================================
# Exercise 1 — Manual Aggregations (no built-ins)
# Given the list of numbers below, calculate and print:
#   - Total sum
#   - Average (sum / count)
#   - Minimum value
#   - Maximum value
# Use only loops and conditional statements — no sum(), min(), or max().
#
# numbers = [4, 17, 2, 9, 31, 8, 15, 6, 22, 11]
#
# Expected output:
#   Sum:     125
#   Average: 12.5
#   Min:     2
#   Max:     31
# =============================================================================

numbers = [4, 17, 2, 9, 31, 8, 15, 6, 22, 11]

# Write your code here


# =============================================================================
# Exercise 2 — Merge Dictionaries (keep higher value on conflict)
# Merge dict_a and dict_b into a single dictionary.
# When a key exists in both dicts, keep the higher value.
# Print the merged result.
#
# dict_a = {"x": 10, "y": 5,  "z": 8}
# dict_b = {"y": 12, "z": 3,  "w": 7}
#
# Expected output:
#   {'x': 10, 'y': 12, 'z': 8, 'w': 7}
# =============================================================================

dict_a = {"x": 10, "y": 5,  "z": 8}
dict_b = {"y": 12, "z": 3,  "w": 7}

# Write your code here


# =============================================================================
# Exercise 3 — Character Frequency Counter
# Given the string below, count how many times each character appears and
# store the result in a dictionary. Print the dictionary.
# Hint: iterate over the string; use dict.get() or check membership with `in`.
#
# text = "hello world"
#
# Expected output (order may vary):
#   {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
# =============================================================================

text = "hello world"

# Write your code here


# =============================================================================
# Exercise 4 — Set Intersection
# Find and print the elements that appear in BOTH list_a and list_b.
# Use sets to perform the intersection.
#
# list_a = [1, 3, 5, 7, 9, 11, 13]
# list_b = [3, 6, 9, 12, 13, 15]
#
# Expected output (order may vary):
#   Common elements: {3, 9, 13}
# =============================================================================

list_a = [1, 3, 5, 7, 9, 11, 13]
list_b = [3, 6, 9, 12, 13, 15]

# Write your code here


# =============================================================================
# Exercise 5 — Sort Tuples by Grade (descending)
# Given a list of (name, grade) tuples, sort them by grade from highest to
# lowest and print a numbered ranking.
# Hint: you may use the built-in sorted() with a key argument here.
#
# students = [
#     ("Alice", 88),
#     ("Bob",   72),
#     ("Carol", 95),
#     ("David", 88),
#     ("Eve",   61),
# ]
#
# Expected output:
#   1. Carol  — 95
#   2. Alice  — 88
#   3. David  — 88
#   4. Bob    — 72
#   5. Eve    — 61
# =============================================================================

students = [
    ("Alice", 88),
    ("Bob",   72),
    ("Carol", 95),
    ("David", 88),
    ("Eve",   61),
]

# Write your code here
