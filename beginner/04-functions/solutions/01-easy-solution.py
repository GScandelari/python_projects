# ============================================================
# beginner/04-functions/solutions/01-easy-solution.py
# Solutions for exercises/01-easy.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — greet(name)
# Write a function that returns "Hello, {name}!"
# ----------------------------------------------------------
# APPROACH: Use an f-string to embed the parameter inside the
# return string. Note: we RETURN the value, not print it.

def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"

print(greet("Alice"))   # Hello, Alice!
print(greet("Bob"))     # Hello, Bob!


# ----------------------------------------------------------
# Exercise 2 — area_rectangle(width, height)
# Return the area of a rectangle.
# ----------------------------------------------------------
# APPROACH: Multiply width by height. The result is a number,
# so we return it directly.

def area_rectangle(width, height):
    """Return the area of a rectangle given its width and height."""
    return width * height

print(area_rectangle(5, 3))    # 15
print(area_rectangle(10, 2))   # 20


# ----------------------------------------------------------
# Exercise 3 — is_even(n)
# Return True if n is even, False otherwise.
# ----------------------------------------------------------
# APPROACH: Use the modulo operator (%). A number is even if
# n % 2 == 0. We can return the boolean expression directly.

def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False
print(is_even(0))   # True


# ----------------------------------------------------------
# Exercise 4 — celsius_to_fahrenheit(c)
# Convert Celsius to Fahrenheit using F = (C * 9/5) + 32
# ----------------------------------------------------------
# APPROACH: Apply the formula directly. Using 9/5 (not 9//5)
# ensures we get a float result.

def celsius_to_fahrenheit(c):
    """Convert a Celsius temperature to Fahrenheit."""
    return (c * 9 / 5) + 32

print(celsius_to_fahrenheit(0))     # 32.0
print(celsius_to_fahrenheit(100))   # 212.0
print(celsius_to_fahrenheit(37))    # 98.6


# ----------------------------------------------------------
# Exercise 5 — max_of_three(a, b, c)
# Return the largest of three numbers without max().
# ----------------------------------------------------------
# APPROACH: Start by assuming the first number is the largest.
# Then compare with the other two, updating if a larger one
# is found. This is the manual "scan" pattern.

def max_of_three(a, b, c):
    """Return the largest of three numbers without using built-in max()."""
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

print(max_of_three(3, 7, 5))    # 7
print(max_of_three(10, 2, 8))   # 10
print(max_of_three(1, 1, 1))    # 1