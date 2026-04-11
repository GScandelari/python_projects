# ============================================================
# beginner/04-functions/exercises/02-medium.py
# Topic: Functions — default params, return tuples, lambda
# Difficulty: Medium
# ============================================================

# Exercise 1
# ----------
# Write a function called count_vowels(text) that counts and
# returns the number of vowels in a string (case-insensitive).
# Vowels: a, e, i, o, u
#
# Expected:
#   count_vowels("Hello World")  → 3
#   count_vowels("Python")       → 1
#   count_vowels("AEIOU")        → 5

# Write your code here


# Exercise 2
# ----------
# Write a function called calculator(a, b, operation="add")
# that performs arithmetic based on the operation string.
# Supported operations: "add", "sub", "mul", "div"
# Return None if the operation is unknown or division by zero.
#
# Expected:
#   calculator(10, 5)             → 15
#   calculator(10, 5, "sub")      → 5
#   calculator(10, 5, "mul")      → 50
#   calculator(10, 5, "div")      → 2.0
#   calculator(10, 0, "div")      → None
#   calculator(10, 5, "unknown")  → None

# Write your code here


# Exercise 3
# ----------
# Write a function called summarize(numbers) that receives a
# list of numbers and returns a TUPLE with four values:
# (minimum, maximum, total_sum, average)
# Do NOT use the built-in min() or max().
#
# Expected:
#   summarize([4, 7, 2, 9, 1])  → (1, 9, 23, 4.6)

# Write your code here


# Exercise 4
# ----------
# Write a function called fizzbuzz(n) that returns the FizzBuzz
# result for a SINGLE number n (no loop, no printing).
# Rules: divisible by 3 → "Fizz", by 5 → "Buzz",
#        by both → "FizzBuzz", otherwise → the number itself (int).
#
# Expected:
#   fizzbuzz(3)   → "Fizz"
#   fizzbuzz(5)   → "Buzz"
#   fizzbuzz(15)  → "FizzBuzz"
#   fizzbuzz(7)   → 7

# Write your code here


# Exercise 5
# ----------
# Define a lambda called `square` that squares a number.
# Define a lambda called `is_positive` that returns True if a number > 0.
# Then write a function called filter_and_square(numbers) that
# uses both lambdas to return a list of squared values of only
# the positive numbers in the input list.
#
# Expected:
#   filter_and_square([3, -1, 4, -2, 5])  → [9, 16, 25]
#   filter_and_square([-3, -1, -4])       → []

# Write your code here