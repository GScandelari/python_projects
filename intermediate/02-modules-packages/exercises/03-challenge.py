# ============================================================
# intermediate/02-modules-packages/exercises/03-challenge.py
# Topic: Creating and using your own package
# Difficulty: Challenge
# ============================================================
#
# This exercise has TWO parts:
#
# PART 1 — Implement the myutils package
# ----------------------------------------
# Open the files inside the myutils/ folder and implement all functions:
#
#   myutils/strings.py:
#     - reverse(text)          → "Python" → "nohtyP"
#     - is_palindrome(text)    → "racecar" → True (ignore case + spaces)
#     - word_count(text)       → returns {word: count} dict
#
#   myutils/numbers.py:
#     - clamp(value, low, high) → clamp(150, 0, 100) → 100
#     - is_prime(n)             → is_prime(17) → True
#     - factors(n)              → factors(12) → [1, 2, 3, 4, 6, 12]
#
# PART 2 — Use the package here
# ----------------------------------------
# After implementing the functions, use them below to:
#
#   a) Import the package using: from myutils import ...
#      or: import myutils
#
#   b) Test each function with the expected outputs shown below
#
#   c) Build a small CLI tool that:
#      - Asks the user to choose: [1] String tools  [2] Number tools
#      - String tools: ask for a word → show reversed, palindrome check, word count
#      - Number tools: ask for a number → show if prime, its factors, clamped to 1-100
#
# Expected output (string tools, input="racecar"):
#   Reversed   : racecar
#   Palindrome : True
#   Word count : {'racecar': 1}
#
# Expected output (number tools, input=12):
#   Is prime   : False
#   Factors    : [1, 2, 3, 4, 6, 12]
#   Clamped(1-100): 12

# Write your code here (import and use myutils)
