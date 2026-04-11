# ============================================================
# intermediate/05-comprehensions/exercises/01-easy.py
# Topic: Comprehensions — list basics, filtering, transformation
# Difficulty: Easy
# ============================================================

# Exercise 1
# ----------
# Convert the loop below into a ONE-LINE list comprehension.
#
# words = ["hello", "world", "python", "code"]
#
# Loop version:
#   upper_words = []
#   for word in words:
#       upper_words.append(word.upper())
#
# Expected:
#   ['HELLO', 'WORLD', 'PYTHON', 'CODE']

words = ["hello", "world", "python", "code"]
# Write your code here


# Exercise 2
# ----------
# Using a list comprehension, generate the squares of all
# numbers from 1 to 10.
#
# Expected:
#   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Write your code here


# Exercise 3
# ----------
# Using a list comprehension with a filter, keep only the
# even numbers from the list below.
#
# numbers = [3, 8, 1, 6, 14, 5, 9, 12, 7, 2]
#
# Expected:
#   [8, 6, 14, 12, 2]

numbers = [3, 8, 1, 6, 14, 5, 9, 12, 7, 2]
# Write your code here


# Exercise 4
# ----------
# Using a list comprehension, extract only the strings
# (ignore non-strings) from the mixed list below.
#
# mixed = [1, "apple", 3.14, "banana", True, "cherry", 42]
#
# Expected:
#   ['apple', 'banana', 'cherry']

mixed = [1, "apple", 3.14, "banana", True, "cherry", 42]
# Write your code here


# Exercise 5
# ----------
# Using a dict comprehension, build a dictionary that maps
# each word to its length.
#
# fruits = ["apple", "kiwi", "watermelon", "fig", "mango"]
#
# Expected:
#   {'apple': 5, 'kiwi': 4, 'watermelon': 10, 'fig': 3, 'mango': 5}

fruits = ["apple", "kiwi", "watermelon", "fig", "mango"]
# Write your code here


# Exercise 6
# ----------
# Using a set comprehension, get the unique set of FIRST
# letters from the list below (lowercase).
#
# words = ["Python", "Pandas", "NumPy", "Pytest", "Flask", "FastAPI"]
#
# Expected (order may vary):
#   {'p', 'n', 'f'}

words = ["Python", "Pandas", "NumPy", "Pytest", "Flask", "FastAPI"]
# Write your code here
