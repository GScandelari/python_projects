# ============================================================
# advanced/03-testing/exercises/01-easy.py
# Topic: Testing with pytest — basics
# Difficulty: Easy
# ============================================================
#
# Run with: pytest exercises/01-easy.py -v
# Install:  pip install pytest
# ============================================================

import pytest

# --- Code under test (normally in a separate module) ---

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def clamp(value, lo, hi):
    return max(lo, min(hi, value))

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if not self._data:
            raise IndexError("peek at empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)


# ============================================================
# Exercise 1 — Test the add() function
# Write at least 4 test functions covering:
#   - Two positive numbers
#   - A negative number
#   - Zero
#   - Floating point (use pytest.approx)
# ============================================================

# Write your test functions here


# ============================================================
# Exercise 2 — Test divide() including exceptions
# Write tests for:
#   - Normal division
#   - Division by zero (use pytest.raises)
#   - Check the exception message contains "Cannot divide by zero"
# ============================================================

# Write your test functions here


# ============================================================
# Exercise 3 — Test is_palindrome()
# Write tests for at least 5 words/phrases:
#   "racecar", "hello", "A man a plan a canal Panama" (no spaces),
#   "level", "Python"
# ============================================================

# Write your test functions here


# ============================================================
# Exercise 4 — Test clamp()
# Write tests for:
#   - Value within range
#   - Value below lo
#   - Value above hi
#   - Value equal to lo (edge case)
#   - Value equal to hi (edge case)
# ============================================================

# Write your test functions here


# ============================================================
# Exercise 5 — Test the Stack class
# Write a pytest.fixture that returns a fresh Stack.
# Write tests for:
#   - push and peek
#   - push and pop
#   - pop from empty stack (IndexError)
#   - is_empty on new stack and after push
#   - size after multiple pushes
# ============================================================

# Write your fixture and test functions here
