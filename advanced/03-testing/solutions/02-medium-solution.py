# ============================================================
# advanced/03-testing/solutions/02-medium-solution.py
# Run: pytest solutions/02-medium-solution.py -v
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
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def save_config(path, data):
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
# ============================================================

@pytest.mark.parametrize("n, expected", [
    (1,  1),
    (2,  2),
    (3,  "Fizz"),
    (5,  "Buzz"),
    (9,  "Fizz"),
    (10, "Buzz"),
    (15, "FizzBuzz"),
    (30, "FizzBuzz"),
])
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected


# ============================================================
# Exercise 2 — Parametrize temperature conversion
# ============================================================

@pytest.mark.parametrize("celsius, fahrenheit", [
    (0,    32.0),
    (100,  212.0),
    (-40,  -40.0),
    (37,   98.6),
    (20,   68.0),
])
def test_celsius_to_fahrenheit(celsius, fahrenheit):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(fahrenheit, rel=1e-3)


# ============================================================
# Exercise 3 — Fixtures for BankAccount
# ============================================================

@pytest.fixture
def empty_account():
    return BankAccount("Alice", 0)

@pytest.fixture
def funded_account():
    return BankAccount("Bob", 1000)

def test_deposit_increases_balance(empty_account):
    empty_account.deposit(500)
    assert empty_account.balance() == 500

def test_withdraw_decreases_balance(funded_account):
    funded_account.withdraw(200)
    assert funded_account.balance() == 800

def test_deposit_zero_raises(empty_account):
    with pytest.raises(ValueError, match="positive"):
        empty_account.deposit(0)

def test_withdraw_negative_raises(funded_account):
    with pytest.raises(ValueError, match="positive"):
        funded_account.withdraw(-50)

def test_withdraw_insufficient_funds(empty_account):
    with pytest.raises(ValueError, match="Insufficient"):
        empty_account.withdraw(1)

def test_str_representation(funded_account):
    assert str(funded_account) == "Account[Bob]: R$1000.00"


# ============================================================
# Exercise 4 — File-based tests with tmp_path
# ============================================================

def test_save_and_load_config(tmp_path):
    config_path = tmp_path / "config.json"
    data = {"theme": "dark", "font_size": 14}
    save_config(config_path, data)
    loaded = load_config(config_path)
    assert loaded == data

def test_load_config_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_config(tmp_path / "nonexistent.json")

def test_load_config_invalid_json(tmp_path):
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("{not valid json", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        load_config(bad_file)

def test_save_config_creates_file(tmp_path):
    path = tmp_path / "settings.json"
    save_config(path, {"key": "value"})
    assert path.exists()


# ============================================================
# Exercise 5 — Module-scoped fixture
# ============================================================

@pytest.fixture(scope="module")
def many_accounts():
    return [BankAccount(f"User_{i}", balance=i * 100) for i in range(100)]

def test_total_balance(many_accounts):
    total = sum(acc.balance() for acc in many_accounts)
    # sum of 0..99 * 100 = 4950 * 100 = 495000
    assert total == 495_000

def test_accounts_above_threshold(many_accounts):
    rich = [acc for acc in many_accounts if acc.balance() >= 5000]
    assert len(rich) == 50   # balances 5000, 5100, ..., 9900

def test_account_count(many_accounts):
    assert len(many_accounts) == 100
