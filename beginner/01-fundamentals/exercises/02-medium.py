# =============================================================================
# Difficulty : Medium
# Topic      : Python Fundamentals - input(), f-strings & Type Conversion
# Description: Practice reading user input, converting types, performing
#              calculations, and formatting output with f-strings.
# =============================================================================


# -----------------------------------------------------------------------------
# Exercise 1 - Reading and displaying user input
# -----------------------------------------------------------------------------
# Ask the user for their first name and their age (as separate input() calls).
# Then print a greeting that includes both pieces of information.
#
# Remember: input() always returns a STRING, so convert age to int before
# doing any arithmetic.
#
# Example interaction:
#   Enter your name: Maria
#   Enter your age: 30
#
# Expected output (varies with input):
#   Hello, Maria! You are 30 years old.

# Write your code here


# -----------------------------------------------------------------------------
# Exercise 2 - Area of a rectangle
# -----------------------------------------------------------------------------
# Ask the user to enter the WIDTH and HEIGHT of a rectangle (floats allowed).
# Calculate the area (width * height) and the perimeter (2 * (width + height)).
# Display both results formatted to 2 decimal places using an f-string.
#
# Example interaction:
#   Enter the width : 5.5
#   Enter the height: 3.0
#
# Expected output (varies with input):
#   Area     : 16.50
#   Perimeter: 17.00

# Write your code here


# -----------------------------------------------------------------------------
# Exercise 3 - Type conversion practice
# -----------------------------------------------------------------------------
# Given the following values stored as STRINGS (do NOT change these lines):
str_integer = "42"
str_float   = "3.14"
str_bool    = "1"
#
# Convert each one to its appropriate numeric type (int, float, int->bool)
# and print the converted values together with their types.
#
# Expected output:
#   42   <class 'int'>
#   3.14 <class 'float'>
#   True <class 'bool'>

# Write your code here


# -----------------------------------------------------------------------------
# Exercise 4 - f-string formatting
# -----------------------------------------------------------------------------
# Create the following variables:
#   product = "Laptop"
#   price   = 999.9
#   stock   = 5
#
# Use a SINGLE print statement with an f-string to display:
#   Product : Laptop
#   Price   : $999.90
#   In stock: 5 unit(s)
#
# Hint: use :.2f inside the f-string to format the price with 2 decimal places.
#
# Expected output:
#   Product : Laptop
#   Price   : $999.90
#   In stock: 5 unit(s)

# Write your code here


# -----------------------------------------------------------------------------
# Exercise 5 - Tip calculator
# -----------------------------------------------------------------------------
# Ask the user for:
#   1. The total bill amount (float).
#   2. The tip percentage they want to leave (float, e.g. 15 means 15%).
#
# Calculate:
#   - The tip amount  = bill * (percentage / 100)
#   - The grand total = bill + tip amount
#
# Display everything formatted to 2 decimal places.
#
# Example interaction:
#   Enter the bill amount   : 85.50
#   Enter tip percentage (%) : 18
#
# Expected output (varies with input):
#   Bill total : $85.50
#   Tip (18.0%): $15.39
#   Grand total: $100.89

# Write your code here
