# ============================================================
# beginner/04-functions/solutions/03-challenge-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Recursive factorial
# ----------------------------------------------------------
# APPROACH: Classic recursion with a base case at 0.
# Guard negative input by returning None immediately.

def factorial(n):
    """Return n! for n >= 0, or None for negative input.

    Uses recursion: n! = n * (n-1)!  with base case 0! = 1.
    """
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(0))    # 1
print(factorial(1))    # 1
print(factorial(5))    # 120
print(factorial(10))   # 3628800
print(factorial(-1))   # None


# ----------------------------------------------------------
# Exercise 2 — Caesar cipher
# ----------------------------------------------------------
# APPROACH: For each character, determine its alphabet base
# (ord('A') or ord('a')), shift within the 26-letter range
# using modulo, then reconstruct the character.

def caesar_cipher(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shifted = (ord(ch) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(ch)
    return "".join(result)

print(caesar_cipher("Hello, World!", 3))   # Khoor, Zruog!
print(caesar_cipher("Python", 1))          # Qzuipo
print(caesar_cipher("Khoor, Zruog!", -3))  # Hello, World!


# ----------------------------------------------------------
# Exercise 3 — flatten (one level deep)
# ----------------------------------------------------------
# APPROACH: Iterate over each element. If it's a list, extend
# the result with its contents. Otherwise append it directly.
# This flattens exactly ONE level — nested lists inside the
# inner lists are kept as-is.

def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result

print(flatten([[1, 2], [3, 4], [5]]))    # [1, 2, 3, 4, 5]
print(flatten([[1, 2], 3, [4, 5]]))      # [1, 2, 3, 4, 5]
print(flatten([1, 2, 3]))               # [1, 2, 3]
print(flatten([[1, [2]], [3], 4]))       # [1, [2], 3, 4]
