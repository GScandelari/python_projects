# =============================================================================
# Difficulty : Challenge
# Topic      : Python Fundamentals - Putting It All Together
# Description: Build small, self-contained programs that combine variables,
#              type conversion, arithmetic, input(), and f-string formatting.
#              Each exercise should feel like a mini real-world tool.
# =============================================================================


# -----------------------------------------------------------------------------
# Exercise 1 - Command-line Calculator
# -----------------------------------------------------------------------------
# Build a simple two-operand calculator entirely with input() and print().
#
# Steps:
#   1. Ask the user for the FIRST number  (allow decimals -> float).
#   2. Ask the user for an OPERATOR: one of  +  -  *  /
#   3. Ask the user for the SECOND number (allow decimals -> float).
#   4. Compute the result based on the chosen operator.
#   5. Print the full expression and its result formatted to 4 decimal places.
#
# Edge case: if the operator is '/' and the second number is 0, print:
#   "Error: division by zero is not allowed."
# instead of calculating.
#
# Example interaction:
#   Enter the first number : 12
#   Enter an operator (+ - * /): *
#   Enter the second number: 7.5
#
# Expected output (varies with input):
#   12.0 * 7.5 = 90.0000
#
# Another example (division by zero):
#   Enter the first number : 9
#   Enter an operator (+ - * /): /
#   Enter the second number: 0
#   Error: division by zero is not allowed.
#
# Hint: you can use if / elif / else to branch on the operator.
#       No need to import anything - keep it to the fundamentals!

# Write your code here


# -----------------------------------------------------------------------------
# Exercise 2 - BMI Calculator
# -----------------------------------------------------------------------------
# Build a Body Mass Index (BMI) calculator.
#
# Formula: BMI = weight_kg / (height_m ** 2)
#
# Steps:
#   1. Ask the user for their weight in kilograms (float).
#   2. Ask the user for their height in meters    (float).
#   3. Calculate the BMI.
#   4. Print the BMI value rounded to 2 decimal places.
#   5. Print the corresponding WHO category based on these ranges:
#        BMI < 18.5              -> "Underweight"
#        18.5 <= BMI < 25.0      -> "Normal weight"
#        25.0 <= BMI < 30.0      -> "Overweight"
#        BMI >= 30.0             -> "Obese"
#
# Example interaction:
#   Enter your weight (kg): 70
#   Enter your height (m) : 1.75
#
# Expected output (varies with input):
#   Your BMI   : 22.86
#   Category   : Normal weight
#
# Hint: use elif chains to check the BMI ranges in order.

# Write your code here


# -----------------------------------------------------------------------------
# Exercise 3 - Temperature Converter
# -----------------------------------------------------------------------------
# Build an interactive temperature converter that works in BOTH directions:
#   Celsius -> Fahrenheit  and  Fahrenheit -> Celsius
#
# Conversion formulas:
#   C to F : F = (C * 9/5) + 32
#   F to C : C = (F - 32) * 5/9
#
# Steps:
#   1. Ask the user to choose a conversion direction by entering:
#        "1" for Celsius -> Fahrenheit
#        "2" for Fahrenheit -> Celsius
#   2. Ask the user for the temperature value (float).
#   3. Perform the correct conversion.
#   4. Print the original value and the converted value, both to 2 decimal
#      places, with the appropriate unit symbols (C or F).
#   5. If the user enters anything other than "1" or "2", print:
#        "Invalid choice. Please enter 1 or 2."
#
# Example interaction (choice 1):
#   Temperature converter
#   1 - Celsius to Fahrenheit
#   2 - Fahrenheit to Celsius
#   Your choice: 1
#   Enter temperature in Celsius: 100
#
# Expected output:
#   100.00 C = 212.00 F
#
# Example interaction (choice 2):
#   Your choice: 2
#   Enter temperature in Fahrenheit: 32
#
# Expected output:
#   32.00 F = 0.00 C

# Write your code here
