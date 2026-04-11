# Difficulty: Challenge
# Topic: Python Control Flow — for loops, while loops, if/elif/else, break, range()

# ============================================================
# Exercise 1 — Multiplication Table
# ============================================================
# Ask the user to enter a number N using input().
# Print the full multiplication table for N, from 1 x N to 10 x N.
#
# Use a for loop with range() to generate each row.
# Format each line as:  "N x i = result"
#
# Expected output (if the user enters 6):
#   6 x 1 = 6
#   6 x 2 = 12
#   6 x 3 = 18
#   6 x 4 = 24
#   6 x 5 = 30
#   6 x 6 = 36
#   6 x 7 = 42
#   6 x 8 = 48
#   6 x 9 = 54
#   6 x 10 = 60

# Write your code here


# ============================================================
# Exercise 2 — Number Guessing Game
# ============================================================
# A secret number is hardcoded below.
# Use a while loop to let the user keep guessing until they get it right.
# After each wrong guess, print either "Too high!" or "Too low!".
# When the user guesses correctly, print how many attempts it took.
#
# Expected output (example run):
#   Guess the number: 70
#   Too high!
#   Guess the number: 20
#   Too low!
#   Guess the number: 42
#   Correct! You got it in 3 attempts.
#
# Rules:
#   - Start an attempt counter at 0 and increment it each guess.
#   - Use int() to convert input to an integer.
#   - Do NOT change the value of secret_number.

secret_number = 42

# Write your code here


# ============================================================
# Exercise 3 — Right-Angle Triangle of Stars
# ============================================================
# Ask the user to enter a height N using input().
# Print a right-angle triangle made of "*" characters.
# Row 1 has 1 star, row 2 has 2 stars, ..., row N has N stars.
#
# Hint: Use a nested approach — an outer for loop for the row number
# and either string multiplication ("*" * count) or an inner loop
# to print the stars on each row.
#
# Expected output (if the user enters 5):
#   *
#   **
#   ***
#   ****
#   *****

# Write your code here
