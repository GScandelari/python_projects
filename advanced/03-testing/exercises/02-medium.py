# ============================================================
# advanced/03-testing/exercises/02-medium.py
# Topic: Testing with pytest — parametrize, fixtures, tmp files
# Difficulty: Medium
# ============================================================
#
# Run with: pytest exercises/02-medium.py -v
# ============================================================

import pytest
import json
from pathlib import Path

# --- Code under test ---

def fizzbuzz(n):
    if n % 15 == 0: return "FizzBuzz"
    if n % 3 == 0:  return "Fizz"
    if n % 5 == 0:  return "Buzz"
    return n

def celsius_to_fahrenheit(c):
    return round(c * 9 / 5 + 32, 2)

def load_config(path):
    """Load a JSON config file. Returns dict or raises on error."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def save_config(path, data):
    """Save a dict as JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def balance(self):
        return self._balance

    def __str__(self):
        return f"Account[{self.owner}]: R${self._balance:.2f}"


# ============================================================
# Exercise 1 — Parametrize fizzbuzz
# Use @pytest.mark.parametrize to test fizzbuzz with at least
# 8 cases covering: regular numbers, multiples of 3, 5, and 15.
# ============================================================

# Write your code here


# ============================================================
# Exercise 2 — Parametrize temperature conversion
# Use @pytest.mark.parametrize to test celsius_to_fahrenheit with:
#   0°C → 32°F, 100°C → 212°F, -40°C → -40°F, 37°C → 98.6°F
# Use pytest.approx for floating point.
# ============================================================

# Write your code here


# ============================================================
# Exercise 3 — Fixtures for BankAccount
# Create two fixtures:
#   empty_account — BankAccount("Alice", 0)
#   funded_account — BankAccount("Bob", 1000)
# Write tests for:
#   - deposit increases balance
#   - withdraw decreases balance
#   - deposit of 0 raises ValueError
#   - withdraw more than balance raises ValueError
#   - __str__ output is correct
# ============================================================

# Write your code here


# ============================================================
# Exercise 4 — File-based tests using tmp_path
# Use pytest's built-in tmp_path fixture (a temporary Path object).
# Write tests for load_config and save_config:
#   - Save a config dict, load it back, verify contents
#   - Loading a non-existent file raises FileNotFoundError
#   - Loading a file with invalid JSON raises json.JSONDecodeError
# ============================================================

# Write your code here


# ============================================================
# Exercise 5 — Fixture with scope
# Create a module-scoped fixture that builds a list of 100
# BankAccount objects with varying balances.
# Write 2+ tests that use this shared fixture and verify
# statistics (total balance, count above threshold, etc.).
# ============================================================

# Write your code here
