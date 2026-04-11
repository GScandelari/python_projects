# ============================================================
# intermediate/05-comprehensions/solutions/03-challenge-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Pipeline of comprehensions
# ----------------------------------------------------------
# APPROACH: Chain transformations inside a single dict comprehension.
# First convert and clean, then filter with if, then add the key.

raw = [
    {"name": " Notebook ", "price": "2500.00", "stock": 10},
    {"name": " Mouse    ", "price": "89.90",   "stock": 50},
    {"name": " Monitor  ", "price": "1899.00", "stock": 5},
    {"name": " Keyboard ", "price": "199.90",  "stock": 30},
    {"name": " USB Hub  ", "price": "45.00",   "stock": 100},
]

cleaned = [
    {
        "name":       item["name"].strip(),
        "price":      float(item["price"]),
        "stock":      item["stock"],
        "discounted": round(float(item["price"]) * 0.9, 2),
    }
    for item in raw
    if float(item["price"]) > 100
]

for product in cleaned:
    print(product)
# {'name': 'Notebook', 'price': 2500.0, 'stock': 10, 'discounted': 2250.0}
# {'name': 'Monitor',  'price': 1899.0, 'stock': 5,  'discounted': 1709.1}
# {'name': 'Keyboard', 'price': 199.9,  'stock': 30, 'discounted': 179.91}


# ----------------------------------------------------------
# Exercise 2 — Invert and group enrollment dict
# ----------------------------------------------------------
# APPROACH: First collect all unique subjects (set comprehension),
# then build the inverted dict (dict comprehension) by scanning
# all students for each subject.

enrollment = {
    "Alice": ["Math", "Physics", "CS"],
    "Bob":   ["Math", "Biology"],
    "Carol": ["CS", "Biology", "Chemistry"],
    "Dave":  ["Physics", "CS"],
}

all_subjects = {subject for subjects in enrollment.values() for subject in subjects}

inverted = {
    subject: [student for student, subjects in enrollment.items()
              if subject in subjects]
    for subject in sorted(all_subjects)
}

print()
for subject, students in inverted.items():
    print(f"  {subject:<12}: {students}")
# Math      : ['Alice', 'Bob']
# Physics   : ['Alice', 'Dave']
# CS        : ['Alice', 'Carol', 'Dave']
# Biology   : ['Bob', 'Carol']
# Chemistry : ['Carol']


# ----------------------------------------------------------
# Exercise 3 — Generator expressions
# ----------------------------------------------------------
# APPROACH:
#   a) next() pulls the first match lazily — no full list built.
#   b) sum() consumes a generator — never holds all squares in memory.
#   c) all() short-circuits on first False — efficient for long iterables.

print()

# a) First number divisible by 7, 11, and 13 (LCM = 1001)
first = next(n for n in range(1, 1_000_000) if n % 7 == 0 and n % 11 == 0 and n % 13 == 0)
print(f"First divisible by 7, 11 & 13: {first}")   # 1001

# b) Sum of squares of odd numbers 1–999_999
total = sum(n ** 2 for n in range(1, 1_000_000, 2))
print(f"Sum of squares (odd 1–999999): {total}")

# c) all words length > 3?
words = ["Python", "is", "cool"]
print(f"All words length > 3: {all(len(w) > 3 for w in words)}")   # False
