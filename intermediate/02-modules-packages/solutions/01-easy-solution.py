# ============================================================
# intermediate/02-modules-packages/solutions/01-easy-solution.py
# ============================================================

import math
import random
import os
import json
from datetime import date, datetime, timedelta

print("=" * 50)
print("Exercise 1 — math")
print("=" * 50)
# APPROACH: Import the module once, then access its attributes and functions.
# math.pow returns float; ** operator returns int when both operands are int.

print(f"pi = {math.pi:.5f}")
print(f"sqrt(256) = {math.sqrt(256)}")
print(f"ceil(7.2) = {math.ceil(7.2)} | floor(7.8) = {math.floor(7.8)}")
print(f"2^16 = {math.pow(2, 16)}")
print(f"10! = {math.factorial(10)}")


print("\n" + "=" * 50)
print("Exercise 2 — random")
print("=" * 50)
# APPROACH: seed() makes randomness reproducible — useful for testing.
# sample() guarantees uniqueness; randint is inclusive on both ends.

random.seed(99)
print(f"Random int 1-100: {random.randint(1, 100)}")
print(f"Choice: {random.choice(['rock', 'paper', 'scissors'])}")
print(f"5 unique ints 1-50: {sorted(random.sample(range(1, 51), 5))}")

numbers = list(range(1, 11))
random.shuffle(numbers)
print(f"Shuffled 1-10: {numbers}")


print("\n" + "=" * 50)
print("Exercise 3 — datetime")
print("=" * 50)
# APPROACH: date.today() returns a date object. strftime() formats it.
# timedelta allows arithmetic on dates.

today = date.today()
print(f"Today: {today.strftime('%d/%m/%Y')}")
print(f"Day: {today.strftime('%A')}")
print(f"In 100 days: {(today + timedelta(days=100)).strftime('%d/%m/%Y')}")

new_year_2027 = date(2027, 1, 1)
days_left = (new_year_2027 - today).days
print(f"Days until 2027: {days_left}")


print("\n" + "=" * 50)
print("Exercise 4 — os")
print("=" * 50)
# APPROACH: os.path.join builds paths correctly for any OS (uses \ on Windows, / on Unix).
# os.listdir returns all entries; filter with endswith for file types.

print(f"cwd: {os.getcwd()}")
py_files = [f for f in os.listdir(".") if f.endswith(".py")]
print(f".py files: {py_files}")
print(f"path: {os.path.join('projects', 'python', 'exercises', '01-easy.py')}")
readme_path = os.path.join("..", "README.md")
print(f"README exists: {os.path.exists(readme_path)}")


print("\n" + "=" * 50)
print("Exercise 5 — json")
print("=" * 50)
# APPROACH: json.dumps → Python to string. json.loads → string to Python.
# indent= makes the output human-readable.

data = {
    "name": "Python Projects",
    "language": "Python",
    "level": "intermediate",
    "topics": ["modules", "packages", "imports"]
}
json_str = json.dumps(data, indent=2)
print(json_str)

parsed = json.loads(json_str)
print(f"Topics: {parsed['topics']}")
