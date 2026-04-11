# ============================================================
# intermediate/04-error-handling/solutions/02-medium-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Temperature class with validation
# ----------------------------------------------------------
# APPROACH: Validate unit first (whitelist), then check Kelvin
# minimum. Conversion methods apply the standard formulas.

class Temperature:
    VALID_UNITS = {"C", "F", "K"}

    def __init__(self, value, unit="C"):
        if unit not in self.VALID_UNITS:
            raise ValueError(f"Invalid unit '{unit}'. Choose C, F, or K.")
        if unit == "K" and value < 0:
            raise ValueError("Kelvin cannot be negative.")
        self.value = value
        self.unit = unit

    def to_celsius(self):
        if self.unit == "C":
            return self.value
        if self.unit == "F":
            return (self.value - 32) * 5 / 9
        return self.value - 273.15   # Kelvin

    def to_fahrenheit(self):
        return self.to_celsius() * 9 / 5 + 32

    def __str__(self):
        return f"{self.value}{self.unit}"

t = Temperature(100, "C")
print(t.to_fahrenheit())   # 212.0

try:
    Temperature(-5, "K")
except ValueError as e:
    print(e)   # Kelvin cannot be negative

try:
    Temperature(50, "X")
except ValueError as e:
    print(e)   # Invalid unit 'X'


# ----------------------------------------------------------
# Exercise 2 — Custom Exception Hierarchy + Shop
# ----------------------------------------------------------
# APPROACH: Each custom exception stores its constructor args as
# attributes and overrides __str__ with a descriptive message.

class ShopError(Exception):
    pass

class ProductNotFoundError(ShopError):
    def __init__(self, product_name):
        self.product_name = product_name

    def __str__(self):
        return f"Product '{self.product_name}' does not exist in the shop."

class OutOfStockError(ShopError):
    def __init__(self, product_name, requested, available):
        self.product_name = product_name
        self.requested = requested
        self.available = available

    def __str__(self):
        return (f"'{self.product_name}' is out of stock: "
                f"requested {self.requested}, only {self.available} available.")

class PaymentError(ShopError):
    def __init__(self, amount, reason):
        self.amount = amount
        self.reason = reason

    def __str__(self):
        return f"Payment of R${self.amount:.2f} failed: {self.reason}."


PRICES = {"Notebook": 2500, "Mouse": 90, "Monitor": 1900}

class Shop:
    def __init__(self):
        self.inventory = {"Notebook": 3, "Mouse": 10, "Monitor": 1}

    def buy(self, product, quantity, payment):
        if product not in self.inventory:
            raise ProductNotFoundError(product)
        available = self.inventory[product]
        if quantity > available:
            raise OutOfStockError(product, quantity, available)
        total = PRICES[product] * quantity
        if payment < total:
            raise PaymentError(payment, f"total is R${total:.2f}")
        self.inventory[product] -= quantity
        return f"Receipt: {quantity}x {product} = R${total:.2f}. Change: R${payment - total:.2f}"


shop = Shop()

# Success
print("\n" + shop.buy("Mouse", 2, 200))

# ProductNotFoundError
try:
    shop.buy("Headset", 1, 300)
except ProductNotFoundError as e:
    print(e)

# OutOfStockError
try:
    shop.buy("Monitor", 5, 10000)
except OutOfStockError as e:
    print(e)

# PaymentError
try:
    shop.buy("Notebook", 1, 100)
except PaymentError as e:
    print(e)


# ----------------------------------------------------------
# Exercise 3 — Exception Chaining
# ----------------------------------------------------------
# APPROACH: Wrap low-level IOError/JSONDecodeError with `raise X from e`
# to preserve the original cause for debugging.

import json

def load_user_config(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError("Config missing") from e
    except json.JSONDecodeError as e:
        raise ValueError("Config corrupted") from e

def save_user_config(path, data):
    required = {"username", "theme", "font_size"}
    missing = required - data.keys()
    if missing:
        raise KeyError(f"Missing required keys: {missing}")
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        raise RuntimeError("Failed to write config") from e

# Missing file
try:
    load_user_config("nonexistent.json")
except RuntimeError as e:
    print(f"\nRuntimeError: {e}  (cause: {e.__cause__})")

# Bad JSON — create a temp file
import tempfile, os
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as tf:
    tf.write("{bad json")
    tf_path = tf.name
try:
    load_user_config(tf_path)
except ValueError as e:
    print(f"ValueError: {e}  (cause: {e.__cause__})")
finally:
    os.unlink(tf_path)

# Valid save
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as tf:
    cfg_path = tf.name
try:
    save_user_config(cfg_path, {"username": "Alice", "theme": "dark", "font_size": 14})
    loaded = load_user_config(cfg_path)
    print(f"Loaded config: {loaded}")
finally:
    os.unlink(cfg_path)


# ----------------------------------------------------------
# Exercise 4 — Robust CLI Input (demo version)
# ----------------------------------------------------------
# APPROACH: In a real CLI, we'd call input() in a while loop.
# For the solution demo, simulate valid/invalid inputs via a list.

from datetime import datetime, date, timedelta

def get_date_demo(inputs):
    """Simulates prompting with a sequence of pre-set inputs."""
    for attempt in inputs:
        try:
            parsed = datetime.strptime(attempt, "%d/%m/%Y").date()
            print(f"  Accepted: {parsed}")
            return parsed
        except ValueError:
            print(f"  Invalid format: '{attempt}' — expected DD/MM/YYYY")
        except Exception as e:
            print(f"  Unexpected error: {e}")
    return None

print("\n--- Date input simulation ---")
birth = get_date_demo(["32/01/2000", "not-a-date", "15/06/1995"])
if birth:
    today = date.today()
    try:
        next_bday = date(today.year, birth.month, birth.day)
    except ValueError:
        next_bday = date(today.year + 1, birth.month, birth.day)
    if next_bday < today:
        next_bday = date(today.year + 1, birth.month, birth.day)
    print(f"  Days until next birthday: {(next_bday - today).days}")


# ----------------------------------------------------------
# Exercise 5 — Retry
# ----------------------------------------------------------
# APPROACH: retry() wraps a callable with up to `times` attempts.
# Uses random.seed for reproducibility in the demo.

import random

def retry(func, times=3):
    for attempt in range(1, times + 1):
        try:
            return func()
        except Exception as e:
            print(f"  Attempt {attempt} failed: {e}")
    raise RuntimeError("All attempts failed")

random.seed(1)

def flaky():
    if random.random() < 0.6:
        raise ValueError("Simulated failure")
    return "Success!"

print("\n--- Retry demo ---")
try:
    result = retry(flaky, times=5)
    print(f"  Result: {result}")
except RuntimeError as e:
    print(f"  {e}")
