# ============================================================
# intermediate/04-error-handling/solutions/03-challenge-solution.py
# ============================================================

import csv
import json
import os
import time
from pathlib import Path
from datetime import datetime

SOLUTIONS_DIR = Path(os.path.dirname(os.path.abspath(__file__)))


# ----------------------------------------------------------
# Exercise 1 — Validated Person data class
# ----------------------------------------------------------
# APPROACH: Each attribute is validated individually in __init__
# before assignment, raising ValueError with a specific message.
# from_dict() wraps KeyError into ValueError.

class Person:
    def __init__(self, name, age, email, height):
        # name
        stripped = str(name).strip()
        if not stripped:
            raise ValueError("name must be non-empty.")
        if not all(ch.isalpha() or ch == " " for ch in stripped):
            raise ValueError("name must contain only letters and spaces.")
        self.name = stripped.title()

        # age
        if not isinstance(age, int) or not (0 <= age <= 150):
            raise ValueError(f"age must be an int between 0 and 150, got {age!r}.")
        self.age = age

        # email
        if email.count("@") != 1:
            raise ValueError("email must contain exactly one '@'.")
        _, domain = email.split("@")
        if "." not in domain:
            raise ValueError("email must have at least one '.' after '@'.")
        self.email = email

        # height
        h = float(height)
        if not (0.0 <= h <= 3.0):
            raise ValueError(f"height must be between 0.0 and 3.0 metres, got {h}.")
        self.height = h

    def __str__(self):
        return f"Person({self.name!r}, age={self.age}, email={self.email!r}, height={self.height}m)"

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age}, email={self.email!r}, height={self.height})"

    @classmethod
    def from_dict(cls, data):
        try:
            return cls(data["name"], data["age"], data["email"], data["height"])
        except KeyError as e:
            raise ValueError(f"Missing required field: {e}") from e


# Demonstrate
print(Person("Alice Smith", 30, "alice@email.com", 1.65))

for bad in [
    lambda: Person("", 30, "a@b.com", 1.70),          # empty name
    lambda: Person("Alice123", 30, "a@b.com", 1.70),   # bad name chars
    lambda: Person("Alice", 200, "a@b.com", 1.70),     # bad age
    lambda: Person("Alice", 30, "notanemail", 1.70),   # bad email
    lambda: Person("Alice", 30, "a@b.com", 5.0),       # bad height
    lambda: Person.from_dict({"name": "Bob", "age": 25}),  # missing keys
]:
    try:
        bad()
    except ValueError as e:
        print(f"  ValueError: {e}")


# ----------------------------------------------------------
# Exercise 2 — Safe CSV Processor
# ----------------------------------------------------------
# APPROACH: Read row by row with a try/except. Track per-row
# warnings without stopping the loop. Clamp out-of-range grades.

input_csv  = SOLUTIONS_DIR / "grades_input.csv"
output_csv = SOLUTIONS_DIR / "grades_output.csv"

# Build test CSV
test_rows = [
    "name,grade1,grade2,grade3",
    "Alice,8.5,9.0,7.5",             # good
    "Bob,6.0,5.5,7.0",               # good
    "Carol,abc,8.0,7.0",             # non-numeric
    "Dave,12,8.0,7.0",               # out of range
    "Eve",                            # missing columns
]
input_csv.write_text("\n".join(test_rows), encoding="utf-8")

def clamp(value, lo, hi):
    return max(lo, min(hi, value))

def process_grades_csv(input_path, output_path):
    summary = {"processed": 0, "skipped": 0, "warnings": 0}
    out_rows = []

    with open(input_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                name = row["name"]
                g1   = row["grade1"]
                g2   = row["grade2"]
                g3   = row["grade3"]
            except KeyError:
                print(f"  WARNING: row missing columns, skipping: {row}")
                summary["warnings"] += 1
                summary["skipped"] += 1
                continue

            grades = []
            for label, raw in [("grade1", g1), ("grade2", g2), ("grade3", g3)]:
                try:
                    g = float(raw)
                except (ValueError, TypeError):
                    print(f"  WARNING: {name} — non-numeric {label}='{raw}', using 0.")
                    summary["warnings"] += 1
                    g = 0.0
                if not (0.0 <= g <= 10.0):
                    print(f"  WARNING: {name} — {label}={g} out of range, clamping.")
                    summary["warnings"] += 1
                    g = clamp(g, 0.0, 10.0)
                grades.append(g)

            avg    = sum(grades) / 3
            status = "Pass" if avg >= 6.0 else "Fail"
            out_rows.append({
                "name": name,
                "grade1": grades[0],
                "grade2": grades[1],
                "grade3": grades[2],
                "average": round(avg, 2),
                "status": status,
            })
            summary["processed"] += 1

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        fields = ["name", "grade1", "grade2", "grade3", "average", "status"]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(out_rows)

    return summary

print("\n--- Safe CSV Processor ---")
result = process_grades_csv(input_csv, output_csv)
print(f"  Summary: {result}")


# ----------------------------------------------------------
# Exercise 3 — Timer context manager
# ----------------------------------------------------------
# APPROACH: __enter__ records start time. __exit__ always
# computes elapsed. If an exception occurred (exc_type is not
# None), print the failure message and return False (re-raise).

class Timer:
    def __enter__(self):
        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self._start
        if exc_type is None:
            print(f"  Elapsed: {elapsed:.3f}s")
        else:
            print(f"  Failed after {elapsed:.3f}s — {exc_type.__name__}: {exc_val}")
        return False   # do not suppress the exception

print("\n--- Timer: successful block ---")
with Timer():
    total = sum(range(1_000_000))

print("\n--- Timer: failing block ---")
try:
    with Timer():
        raise ValueError("something went wrong")
except ValueError:
    pass

# Cleanup
for p in [input_csv, output_csv]:
    p.unlink(missing_ok=True)
