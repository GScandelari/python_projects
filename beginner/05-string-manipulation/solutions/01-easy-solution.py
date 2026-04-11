# ============================================================
# beginner/05-string-manipulation/solutions/01-easy-solution.py
# Solutions for exercises/01-easy.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Indexing and slicing
# ----------------------------------------------------------
# APPROACH: Use bracket notation for indexing and [start:stop:step]
# for slicing. text[::-1] is the idiomatic Python reverse.

text = "Programming"
print(text[0])      # P    — first character (index 0)
print(text[-1])     # g    — last character (negative index)
print(text[::-1])   # gnimmargorP — reversed slice
print(text[::2])    # Pormmn — every other character starting at 0


# ----------------------------------------------------------
# Exercise 2 — Case and strip methods
# ----------------------------------------------------------
# APPROACH: String methods return a NEW string — chain them
# or store each step. strip() removes leading/trailing whitespace.

raw = "   hello, world!   "
print(raw.upper())    # HELLO, WORLD!   (whitespace preserved by upper)
print(raw.lower())    # hello, world!
print(raw.title())    # Hello, World!
print(raw.strip())    # hello, world!   (whitespace removed)


# ----------------------------------------------------------
# Exercise 3 — Count occurrences (case-insensitive)
# ----------------------------------------------------------
# APPROACH: Convert to lowercase first so 'A' and 'a' are treated
# the same, then use the built-in str.count() method.

sentence = "A banana a day keeps the doctor away"
count = sentence.lower().count("a")
print(count)   # 8


# ----------------------------------------------------------
# Exercise 4 — startswith / endswith
# ----------------------------------------------------------
# APPROACH: These methods return a boolean directly — no need
# for an if statement, just print the result.

filename = "my_script.py"
print(filename.endswith(".py"))    # True
print(filename.startswith("my"))  # True


# ----------------------------------------------------------
# Exercise 5 — replace + upper
# ----------------------------------------------------------
# APPROACH: replace() returns a new string with all occurrences
# swapped. Chain .upper() on the result in one expression.

phrase = "python is easy to learn"
print(phrase.replace(" ", "_").upper())   # PYTHON_IS_EASY_TO_LEARN
