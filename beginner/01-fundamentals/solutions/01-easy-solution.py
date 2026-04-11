# =============================================================================
# Difficulty : Easy  —  SOLUTIONS
# Topic      : Python Fundamentals - Variables & Data Types
# Description: Full solutions for all 5 easy exercises with approach comments.
# =============================================================================


# -----------------------------------------------------------------------------
# Exercise 1 - Creating variables of each basic type
# -----------------------------------------------------------------------------
# PROMPT:
#   Create four variables:
#     - an integer named 'age' with the value 25
#     - a float named 'height' with the value 1.75
#     - a string named 'name' with the value "Alice"
#     - a boolean named 'is_student' with the value True
#   Then print each variable on its own line.
#
# Expected output:
#   25
#   1.75
#   Alice
#   True

# APPROACH:
#   Simply assign a literal value to each variable name. Python infers the type
#   automatically from the literal used (25 → int, 1.75 → float, "..." → str,
#   True/False → bool). Each print() call converts the value to its string
#   representation before displaying it.

age        = 25
height     = 1.75
name       = "Alice"
is_student = True

print(age)
print(height)
print(name)
print(is_student)


# -----------------------------------------------------------------------------
# Exercise 2 - Checking data types with type()
# -----------------------------------------------------------------------------
# PROMPT:
#   Using the variables from Exercise 1 (or create new ones), print the TYPE of
#   each variable using the built-in type() function.
#
# Expected output:
#   <class 'int'>
#   <class 'float'>
#   <class 'str'>
#   <class 'bool'>

# APPROACH:
#   type(x) returns a type object describing x's class. Passing it directly to
#   print() displays the canonical "<class 'name'>" representation. No import or
#   extra conversion is needed — this is a built-in function available
#   everywhere in Python.

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))


# -----------------------------------------------------------------------------
# Exercise 3 - Basic arithmetic operators
# -----------------------------------------------------------------------------
# PROMPT:
#   Create two integer variables: a = 18 and b = 5.
#   Then print the result of each operation below, one per line:
#     - Addition       (a + b)
#     - Subtraction    (a - b)
#     - Multiplication (a * b)
#     - Division       (a / b)   <- produces a float
#     - Floor division (a // b)  <- integer part only
#     - Modulo         (a % b)   <- remainder
#     - Exponentiation (a ** b)  <- a to the power of b
#
# Expected output:
#   23
#   13
#   90
#   3.6
#   3
#   3
#   1889568

# APPROACH:
#   Python's arithmetic operators mirror standard maths, with two important
#   extras: '//' (floor division) always truncates toward negative infinity and
#   returns an int when both operands are ints; '%' gives the remainder after
#   floor division. Note that plain '/' always produces a float, even when the
#   result is a whole number (e.g., 10 / 2 → 5.0).

a = 18
b = 5

print(a + b)    # Addition       → 23
print(a - b)    # Subtraction    → 13
print(a * b)    # Multiplication → 90
print(a / b)    # Division       → 3.6  (always float)
print(a // b)   # Floor division → 3
print(a % b)    # Modulo         → 3
print(a ** b)   # Exponentiation → 1 889 568


# -----------------------------------------------------------------------------
# Exercise 4 - String basics
# -----------------------------------------------------------------------------
# PROMPT:
#   Create a variable 'greeting' that holds the string "Hello, World!".
#   Then print:
#     1. The full string.
#     2. The number of characters using len().
#     3. The string in ALL UPPER CASE using .upper().
#     4. The string in all lower case using .lower().
#
# Expected output:
#   Hello, World!
#   13
#   HELLO, WORLD!
#   hello, world!

# APPROACH:
#   Strings in Python are objects that come with many useful methods built in.
#   len() is a standalone function that works on any sequence (strings, lists,
#   etc.), while .upper() and .lower() are string-specific methods. None of
#   these modify the original string — strings are immutable in Python; they
#   always return a new string.

greeting = "Hello, World!"

print(greeting)           # Full string
print(len(greeting))      # Character count (spaces and punctuation included)
print(greeting.upper())   # Every letter capitalised
print(greeting.lower())   # Every letter in lower case


# -----------------------------------------------------------------------------
# Exercise 5 - Simple expressions and variable reassignment
# -----------------------------------------------------------------------------
# PROMPT:
#   Start with a variable 'score' equal to 10.
#   Perform the following steps IN ORDER and print 'score' after each step:
#     1. Add 5 to score.
#     2. Multiply score by 2.
#     3. Subtract 7 from score.
#     4. Divide score by 3.  (use regular division /)
#
# Expected output:
#   15
#   30
#   23
#   7.666666666666667

# APPROACH:
#   Each augmented assignment operator (+=, *=, -=, /=) updates the variable
#   in place: "score += 5" is exactly equivalent to "score = score + 5". This
#   is more concise and considered idiomatic Python. After step 4 the result
#   becomes a float because regular division (/) always returns float, even
#   when both operands are integers.

score = 10

score += 5      # 10 + 5  = 15
print(score)

score *= 2      # 15 * 2  = 30
print(score)

score -= 7      # 30 - 7  = 23
print(score)

score /= 3      # 23 / 3  = 7.666... (float)
print(score)
