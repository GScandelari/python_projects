# ============================================================
# beginner/03-data-structures/solutions/02-medium-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Sum, average, min, max without built-ins
# ----------------------------------------------------------
# APPROACH: Manual scan with a running total and comparisons.
# Initialize min/max to the first element to handle negatives.

numbers = [4, 7, 2, 9, 1, 15, 3]

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
print(f"Sum    : {total}")
print(f"Average: {average:.2f}")
print(f"Min    : {minimum}")
print(f"Max    : {maximum}")


# ----------------------------------------------------------
# Exercise 2 — Merge two dicts, keep higher value on conflict
# ----------------------------------------------------------
# APPROACH: Start with a copy of dict1, then iterate dict2.
# On conflict, keep the higher value.

dict1 = {"a": 10, "b": 5,  "c": 8}
dict2 = {"b": 12, "c": 3, "d": 7}

merged = dict1.copy()
for key, value in dict2.items():
    if key in merged:
        merged[key] = max(merged[key], value)
    else:
        merged[key] = value

print(merged)   # {'a': 10, 'b': 12, 'c': 8, 'd': 7}


# ----------------------------------------------------------
# Exercise 3 — Character frequency using a dict
# ----------------------------------------------------------
# APPROACH: dict.get(key, 0) + 1 is the idiomatic counter.
# Skip spaces for cleaner output.

text = "hello world"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

for char, count in sorted(freq.items()):
    print(f"  {char!r}: {count}")


# ----------------------------------------------------------
# Exercise 4 — Common elements between two lists using sets
# ----------------------------------------------------------
# APPROACH: Convert both lists to sets, use & (intersection).
# Convert back to sorted list for deterministic output.

list_a = [1, 2, 3, 4, 5, 6]
list_b = [4, 5, 6, 7, 8, 9]

common = sorted(set(list_a) & set(list_b))
print(f"Common: {common}")   # [4, 5, 6]


# ----------------------------------------------------------
# Exercise 5 — Sort list of tuples by grade descending
# ----------------------------------------------------------
# APPROACH: sorted() with key=lambda t: t[1] and reverse=True.
# Enumerate for 1-based ranking.

students = [("Alice", 88), ("Bob", 72), ("Carol", 95), ("Dave", 85)]
ranked = sorted(students, key=lambda s: s[1], reverse=True)

print("\n=== Ranking ===")
for i, (name, grade) in enumerate(ranked, 1):
    print(f"  {i}. {name:<8} {grade}")
