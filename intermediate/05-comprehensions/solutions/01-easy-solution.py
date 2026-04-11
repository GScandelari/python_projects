# ============================================================
# intermediate/05-comprehensions/solutions/01-easy-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — uppercase with list comprehension
# ----------------------------------------------------------
words = ["hello", "world", "python", "code"]
upper_words = [word.upper() for word in words]
print(upper_words)   # ['HELLO', 'WORLD', 'PYTHON', 'CODE']


# ----------------------------------------------------------
# Exercise 2 — squares 1–10
# ----------------------------------------------------------
squares = [n ** 2 for n in range(1, 11)]
print(squares)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# ----------------------------------------------------------
# Exercise 3 — filter evens
# ----------------------------------------------------------
numbers = [3, 8, 1, 6, 14, 5, 9, 12, 7, 2]
evens = [n for n in numbers if n % 2 == 0]
print(evens)   # [8, 6, 14, 12, 2]


# ----------------------------------------------------------
# Exercise 4 — extract only strings
# ----------------------------------------------------------
# APPROACH: isinstance(x, str) returns True for strings.
# Note: bool is a subclass of int in Python, so True/False pass
# an int check — but NOT a str check, which is what we want.

mixed = [1, "apple", 3.14, "banana", True, "cherry", 42]
strings_only = [x for x in mixed if isinstance(x, str)]
print(strings_only)   # ['apple', 'banana', 'cherry']


# ----------------------------------------------------------
# Exercise 5 — word → length dict comprehension
# ----------------------------------------------------------
fruits = ["apple", "kiwi", "watermelon", "fig", "mango"]
lengths = {fruit: len(fruit) for fruit in fruits}
print(lengths)
# {'apple': 5, 'kiwi': 4, 'watermelon': 10, 'fig': 3, 'mango': 5}


# ----------------------------------------------------------
# Exercise 6 — unique first letters (set comprehension)
# ----------------------------------------------------------
words = ["Python", "Pandas", "NumPy", "Pytest", "Flask", "FastAPI"]
first_letters = {word[0].lower() for word in words}
print(first_letters)   # {'p', 'n', 'f'}  (order may vary)
