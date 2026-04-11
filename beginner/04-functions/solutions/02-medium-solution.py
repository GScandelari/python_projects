# ============================================================
# beginner/04-functions/solutions/02-medium-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — count_vowels
# ----------------------------------------------------------
# APPROACH: Iterate over each character in the lowered string.
# Check membership in the vowel set — O(1) lookup.

def count_vowels(text):
    vowels = set("aeiou")
    return sum(1 for ch in text.lower() if ch in vowels)

print(count_vowels("Hello World"))  # 3
print(count_vowels("Python"))       # 1
print(count_vowels("AEIOU"))        # 5


# ----------------------------------------------------------
# Exercise 2 — calculator with default parameter
# ----------------------------------------------------------
# APPROACH: Use a dict of operation strings to keep branching minimal.
# Guard division-by-zero before performing the operation.

def calculator(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        if b == 0:
            return None
        return a / b
    return None

print(calculator(10, 5))             # 15
print(calculator(10, 5, "sub"))      # 5
print(calculator(10, 5, "mul"))      # 50
print(calculator(10, 5, "div"))      # 2.0
print(calculator(10, 0, "div"))      # None
print(calculator(10, 5, "unknown"))  # None


# ----------------------------------------------------------
# Exercise 3 — summarize (returns tuple)
# ----------------------------------------------------------
# APPROACH: Single pass through the list. Keep running total,
# and track min/max manually. Return all four values as a tuple.

def summarize(numbers):
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]
    for n in numbers:
        total += n
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n
    average = total / len(numbers)
    return (minimum, maximum, total, average)

print(summarize([4, 7, 2, 9, 1]))  # (1, 9, 23, 4.6)


# ----------------------------------------------------------
# Exercise 4 — fizzbuzz (single number, no loop)
# ----------------------------------------------------------
# APPROACH: Check the combined condition (% 15) first, then
# each individually. Return the int if none match.

def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return n

print(fizzbuzz(3))   # Fizz
print(fizzbuzz(5))   # Buzz
print(fizzbuzz(15))  # FizzBuzz
print(fizzbuzz(7))   # 7


# ----------------------------------------------------------
# Exercise 5 — lambdas + filter_and_square
# ----------------------------------------------------------
# APPROACH: Define lambdas first, then use them inside the
# function: filter with is_positive, map with square.

square      = lambda x: x ** 2
is_positive = lambda x: x > 0

def filter_and_square(numbers):
    return [square(n) for n in numbers if is_positive(n)]

print(filter_and_square([3, -1, 4, -2, 5]))  # [9, 16, 25]
print(filter_and_square([-3, -1, -4]))        # []
