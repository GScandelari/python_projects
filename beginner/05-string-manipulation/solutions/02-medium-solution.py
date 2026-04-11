# ============================================================
# beginner/05-string-manipulation/solutions/02-medium-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Split name and greet
# ----------------------------------------------------------
# APPROACH: strip() removes leading/trailing whitespace first,
# then split() divides at the space. .title() capitalises each part.

full_name = "  alice smith  "
parts = full_name.strip().split()
first, last = parts[0].title(), parts[1].title()
print(f"First: {first}")
print(f"Last: {last}")
print(f"Hello, {first} {last}! You have {len(first)} characters in your first name.")


# ----------------------------------------------------------
# Exercise 2 — CSV string → aligned table
# ----------------------------------------------------------
# APPROACH: split(",") breaks the CSV into a list. Iterate and
# use f-string right-alignment (:>12) for each field.

csv_line = "Alice,28,Engineer,São Paulo"
fields = csv_line.split(",")
print()
for field in fields:
    print(f"{field:>12}")


# ----------------------------------------------------------
# Exercise 3 — Palindrome check
# ----------------------------------------------------------
# APPROACH: Lower both the word and its reverse, then compare.
# word[::-1] is the idiomatic Python string reversal.

words = ["racecar", "Python", "level", "hello", "madam"]
print()
for word in words:
    lowered = word.lower()
    label = "palindrome" if lowered == lowered[::-1] else "not a palindrome"
    print(f"{word:<8} → {label}")


# ----------------------------------------------------------
# Exercise 4 — Word frequency (sorted alphabetically)
# ----------------------------------------------------------
# APPROACH: split() without argument handles multiple spaces.
# Use dict.get(key, 0) + 1 to count without defaultdict.

text = "the cat sat on the mat the cat sat"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1

print()
for word in sorted(freq):
    print(f"{word}: {freq[word]}")


# ----------------------------------------------------------
# Exercise 5 — Formatted student report
# ----------------------------------------------------------
# APPROACH: Print a fixed-width header with two f-string columns,
# then a separator, then each row using the same column widths.

students = [("Alice", 92), ("Bob", 78), ("Carol", 85), ("Dave", 91)]

print()
print(f"{'Name':<16}{'Score':>5}")
print("-" * 20)
for name, score in students:
    print(f"{name:<16}{score:>5}")
