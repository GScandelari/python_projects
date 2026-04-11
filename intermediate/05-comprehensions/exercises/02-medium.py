# ============================================================
# intermediate/05-comprehensions/exercises/02-medium.py
# Topic: Comprehensions — conditionals, nested, dict/set patterns
# Difficulty: Medium
# ============================================================

# Exercise 1
# ----------
# Using a list comprehension with if/else (ternary inside),
# label each number in the list as "even" or "odd".
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# Expected:
#   ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Write your code here


# Exercise 2
# ----------
# Given a list of students with their grades, use a dict
# comprehension to build a dict {name: "Pass"/"Fail"}.
# Pass threshold: average grade >= 6.0.
#
# students = [
#     ("Alice", [8.0, 7.5, 9.0]),
#     ("Bob",   [4.5, 5.0, 6.0]),
#     ("Carol", [9.5, 8.0, 10.0]),
#     ("Dave",  [3.0, 4.0, 5.0]),
# ]
#
# Expected:
#   {'Alice': 'Pass', 'Bob': 'Pass', 'Carol': 'Pass', 'Dave': 'Fail'}

students = [
    ("Alice", [8.0, 7.5, 9.0]),
    ("Bob",   [4.5, 5.0, 6.0]),
    ("Carol", [9.5, 8.0, 10.0]),
    ("Dave",  [3.0, 4.0, 5.0]),
]
# Write your code here


# Exercise 3
# ----------
# Flatten the 2D matrix into a single list using a nested
# list comprehension (one expression, no helper variables).
#
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# Expected:
#   [1, 2, 3, 4, 5, 6, 7, 8, 9]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Write your code here


# Exercise 4
# ----------
# Using a list comprehension, generate all (x, y) pairs where
# x is from 1 to 4, y is from 1 to 4, and x != y.
#
# Expected (first few):
#   [(1,2),(1,3),(1,4),(2,1),(2,3),(2,4),(3,1),(3,2),(3,4),(4,1),(4,2),(4,3)]

# Write your code here


# Exercise 5
# ----------
# Given a sentence, use a dict comprehension to count the
# frequency of each CHARACTER (ignore spaces, case-insensitive).
#
# sentence = "Hello World"
#
# Expected:
#   {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
# Note: build this in one expression (hint: use a set for unique chars).

sentence = "Hello World"
# Write your code here


# Exercise 6
# ----------
# Using a set comprehension, find all numbers from 1–50
# that are divisible by EITHER 3 OR 7 (but NOT both).
#
# Expected (sorted for display):
#   [3, 6, 7, 9, 12, 14, 15, 18, 21 is excluded (3&7), ...]

# Write your code here — print sorted(result) to verify
