# ============================================================
# intermediate/02-modules-packages/solutions/02-medium-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Dice Roller with Statistics
# ----------------------------------------------------------
# APPROACH: Roll 1000 times, accumulate into a dict keyed by
# sum (2-12). Bar length = count // 10.

import random

random.seed(42)
freq = {k: 0 for k in range(2, 13)}
for _ in range(1000):
    freq[random.randint(1, 6) + random.randint(1, 6)] += 1

print("--- Dice Roll Frequency (1000 rolls) ---")
for total in range(2, 13):
    count = freq[total]
    bar = "#" * (count // 10)
    print(f"  {total:2}: {count:4}  {bar}")


# ----------------------------------------------------------
# Exercise 2 — Birthday Countdown
# ----------------------------------------------------------
# APPROACH: Parse DD/MM, try this year first. If the date has
# already passed, use next year. Use timedelta for day count
# and .strftime("%A") for weekday name.

from datetime import date, timedelta

# Demo with a hardcoded birthday to avoid interactive input()
birthday_str = "25/12"
day, month = int(birthday_str[:2]), int(birthday_str[3:])
today = date.today()
try:
    next_birthday = date(today.year, month, day)
except ValueError:
    next_birthday = date(today.year + 1, month, day)
if next_birthday < today:
    next_birthday = date(today.year + 1, month, day)

days_until = (next_birthday - today).days
weekday = next_birthday.strftime("%A")

print(f"\n--- Birthday Countdown ---")
print(f"  Next birthday : {next_birthday.strftime('%d/%m/%Y')}")
print(f"  Days until    : {days_until}")
print(f"  Day of week   : {weekday}")


# ----------------------------------------------------------
# Exercise 3 — Directory Explorer
# ----------------------------------------------------------
# APPROACH: Walk from the current file two levels up to reach the
# project root, then walk the "beginner" folder.
# os.walk yields (dirpath, dirnames, filenames).

import os

script_dir  = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.normpath(os.path.join(script_dir, "..", ".."))
beginner_dir = os.path.join(project_root, "beginner")

print(f"\n--- Directory tree: beginner/ ---")
for dirpath, dirnames, filenames in os.walk(beginner_dir):
    # Compute depth relative to beginner_dir
    rel = os.path.relpath(dirpath, project_root)
    depth = rel.count(os.sep)
    indent = "  " * depth
    print(f"{indent}{os.path.basename(dirpath)}/")
    for fname in filenames:
        if fname == ".gitkeep":
            continue
        print(f"{indent}  {fname}")
    # Prevent os.walk from recursing deeper than 2 extra levels
    if depth >= 2:
        dirnames.clear()


# ----------------------------------------------------------
# Exercise 4 — Config File with JSON
# ----------------------------------------------------------
# APPROACH: Write default → load → mutate → write → load and print.
# Use indent=2 for readable JSON.

import json

config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

default_config = {
    "theme": "light",
    "font_size": 12,
    "language": "en",
    "notifications": True,
}

# Save default
with open(config_path, "w", encoding="utf-8") as f:
    json.dump(default_config, f, indent=2)

# Load, update, save
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

config["theme"] = "dark"
config["font_size"] = 16

with open(config_path, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2)

# Final load and display
with open(config_path, "r", encoding="utf-8") as f:
    final = json.load(f)

print("\n--- Final config ---")
for key, value in final.items():
    print(f"  {key:<14}: {value}")

os.remove(config_path)   # cleanup


# ----------------------------------------------------------
# Exercise 5 — Module Inspection
# ----------------------------------------------------------
# APPROACH: Use dir() to list names and filter with conditions.
# .__doc__.split('\n')[0] gives the first docstring line.

import math
import sys

print("\n--- math names starting with lowercase ---")
print([name for name in dir(math) if name[0].islower()])

print("\n--- math.log first docstring line ---")
print(math.log.__doc__.split("\n")[0])

print("\n--- random names containing 'int' ---")
print([name for name in dir(random) if "int" in name.lower()])

print("\n--- Python version (first line) ---")
print(sys.version.split("\n")[0])
