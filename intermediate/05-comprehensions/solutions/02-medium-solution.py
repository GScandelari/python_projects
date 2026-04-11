# ============================================================
# intermediate/05-comprehensions/solutions/02-medium-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — ternary inside comprehension (even/odd labels)
# ----------------------------------------------------------
# APPROACH: The if/else goes BEFORE the for clause when it
# controls the output value (not filtering rows out).

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(labels)
# ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']


# ----------------------------------------------------------
# Exercise 2 — dict comprehension with computed value
# ----------------------------------------------------------
# APPROACH: sum(grades)/len(grades) gives the average inline.

students = [
    ("Alice", [8.0, 7.5, 9.0]),
    ("Bob",   [4.5, 5.0, 6.0]),
    ("Carol", [9.5, 8.0, 10.0]),
    ("Dave",  [3.0, 4.0, 5.0]),
]
results = {name: ("Pass" if sum(g)/len(g) >= 6.0 else "Fail")
           for name, g in students}
print(results)
# {'Alice': 'Pass', 'Bob': 'Pass', 'Carol': 'Pass', 'Dave': 'Fail'}


# ----------------------------------------------------------
# Exercise 3 — flatten 2D matrix with nested comprehension
# ----------------------------------------------------------
# APPROACH: Outer loop over rows, inner loop over values in each row.
# Read as: "val for row in matrix, val in row".

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [val for row in matrix for val in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# ----------------------------------------------------------
# Exercise 4 — Cartesian product with condition (x != y)
# ----------------------------------------------------------
pairs = [(x, y) for x in range(1, 5) for y in range(1, 5) if x != y]
print(pairs)
# [(1,2),(1,3),(1,4),(2,1),(2,3),(2,4),(3,1),(3,2),(3,4),(4,1),(4,2),(4,3)]


# ----------------------------------------------------------
# Exercise 5 — character frequency dict comprehension
# ----------------------------------------------------------
# APPROACH: Iterate over the unique characters (via a set) so each
# character appears as a key exactly once. Count with str.count().

sentence = "Hello World"
cleaned = sentence.lower().replace(" ", "")
freq = {ch: cleaned.count(ch) for ch in set(cleaned)}
print(dict(sorted(freq.items())))
# {'d': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1}


# ----------------------------------------------------------
# Exercise 6 — set comprehension with XOR-style filter
# ----------------------------------------------------------
# APPROACH: Divisible by 3 OR 7, but NOT both (i.e., not by 21).

result = {n for n in range(1, 51) if (n % 3 == 0) != (n % 7 == 0)}
print(sorted(result))
# [3, 6, 7, 9, 12, 14, 15, 18, 24, 27, 28, 30, 33, 35, 36, 39, 42 excluded, 45, 48, 49]
# 21 and 42 are excluded (divisible by both)
