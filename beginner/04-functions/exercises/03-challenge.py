# ============================================================
# beginner/04-functions/exercises/03-challenge.py
# Topic: Functions — recursion, docstrings, advanced patterns
# Difficulty: Challenge
# ============================================================

# Exercise 1
# ----------
# Write a recursive function called factorial(n) that returns
# the factorial of n (n!). Include a proper docstring.
# Guard against negative input by returning None.
# Base case: factorial(0) = 1
#
# Expected:
#   factorial(0)   → 1
#   factorial(1)   → 1
#   factorial(5)   → 120
#   factorial(10)  → 3628800
#   factorial(-1)  → None

# Write your code here


# Exercise 2
# ----------
# Write a function called caesar_cipher(text, shift) that encodes
# a string by shifting each letter by `shift` positions in the alphabet.
# Rules:
#   - Wraps around (z + 1 → a)
#   - Preserves case (upper stays upper, lower stays lower)
#   - Non-letter characters are left unchanged
#
# Expected:
#   caesar_cipher("Hello, World!", 3)   → "Khoor, Zruog!"
#   caesar_cipher("Python", 1)          → "Qzuipo"
#   caesar_cipher("Khoor, Zruog!", -3)  → "Hello, World!"

# Write your code here


# Exercise 3
# ----------
# Write a function called flatten(nested_list) that takes a list
# which may contain nested lists (ONE level deep) and returns a
# completely flat list.
# Note: only flatten the first level of nesting.
#
# Expected:
#   flatten([[1, 2], [3, 4], [5]])       → [1, 2, 3, 4, 5]
#   flatten([[1, 2], 3, [4, 5]])         → [1, 2, 3, 4, 5]
#   flatten([1, 2, 3])                   → [1, 2, 3]
#   flatten([[1, [2]], [3], 4])          → [1, [2], 3, 4]

# Write your code here