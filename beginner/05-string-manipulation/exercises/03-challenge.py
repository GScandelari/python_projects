# ============================================================
# beginner/05-string-manipulation/exercises/03-challenge.py
# Topic: Strings — advanced patterns, no imports
# Difficulty: Challenge
# ============================================================

# Exercise 1
# ----------
# Write a function called title_case(text) that converts a string
# to title case WITHOUT using .title() or .capitalize().
# Rules: capitalize the first letter of every word, lowercase the rest.
# Punctuation attached to words should be handled naturally.
#
# Expected:
#   title_case("hello world")          → "Hello World"
#   title_case("the QUICK brown FOX")  → "The Quick Brown Fox"
#   title_case("python is great!")     → "Python Is Great!"

# Write your code here


# Exercise 2
# ----------
# Write a function called compress(text) that performs basic
# run-length encoding: consecutive repeated characters are
# replaced with the character followed by the count.
# If the count is 1, omit the number.
#
# Expected:
#   compress("aabbbcccc")   → "a2b3c4"
#   compress("hello")       → "hel2o"
#   compress("aaabbaaa")    → "a3b2a3"
#   compress("abc")         → "abc"

# Write your code here


# Exercise 3
# ----------
# Write a function called word_stats(text) that receives a
# paragraph and prints a full statistical summary:
#   - Total characters (with and without spaces)
#   - Total words
#   - Total sentences (count '.' '!' '?')
#   - Longest word
#   - Most frequent word (case-insensitive)
#   - Average word length (rounded to 2 decimal places)
#
# Use this text:
paragraph = (
    "Python is an amazing language. "
    "Python makes programming fun and easy! "
    "Many developers love Python. "
    "Is Python the best language?"
)
#
# Expected output (approximate):
#   Characters (total): 114
#   Characters (no spaces): 95
#   Words: 20
#   Sentences: 4
#   Longest word: programming
#   Most frequent word: python (4)
#   Average word length: 4.75

# Write your code here
