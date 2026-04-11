# String Manipulation in Python

Strings are one of the most used data types in Python. Mastering string methods and formatting unlocks a huge range of practical tasks — from cleaning user input to building reports.

## Table of Contents

- [String Basics](#1-string-basics)
- [Indexing and Slicing](#2-indexing-and-slicing)
- [Common String Methods](#3-common-string-methods)
- [String Formatting](#4-string-formatting)
- [Searching and Replacing](#5-searching-and-replacing)
- [Splitting and Joining](#6-splitting-and-joining)
- [Common Patterns](#7-common-patterns)
- [Quick Reference](#quick-reference)
- [What's Next](#whats-next)

---

## 1. String Basics

Strings are **immutable** sequences of characters. You can use single or double quotes — they are equivalent.

```python
name = "Python"
also_name = 'Python'

# Multi-line strings use triple quotes
poem = """Roses are red,
Violets are blue."""

# Escape characters
tab = "column1\tcolumn2"
newline = "line1\nline2"
quote = "She said \"hello\""
backslash = "C:\\Users\\scand"

# Raw strings — backslashes are literal
path = r"C:\Users\scand\file.txt"
```

**Strings are immutable** — you cannot change a character in place:

```python
word = "Hello"
# word[0] = "h"   # TypeError!
word = "h" + word[1:]   # create a new string instead
print(word)   # hello
```

---

## 2. Indexing and Slicing

```python
text = "Python"
#       P  y  t  h  o  n
# idx   0  1  2  3  4  5
# neg  -6 -5 -4 -3 -2 -1
```

### Indexing

```python
print(text[0])    # P  — first character
print(text[-1])   # n  — last character
print(text[2])    # t
```

### Slicing `[start:stop:step]`

| Slice | Result | Meaning |
|---|---|---|
| `text[0:3]` | `"Pyt"` | index 0 up to (not including) 3 |
| `text[2:]` | `"thon"` | from index 2 to end |
| `text[:4]` | `"Pyth"` | from start up to 4 |
| `text[::2]` | `"Pto"` | every 2nd character |
| `text[::-1]` | `"nohtyP"` | reversed |

```python
text = "Python"
print(text[1:4])    # yth
print(text[::-1])   # nohtyP  — handy reverse trick
print(len(text))    # 6
```

---

## 3. Common String Methods

Strings have dozens of built-in methods. Here are the most essential:

### Case Methods

```python
s = "hello world"
print(s.upper())        # HELLO WORLD
print(s.lower())        # hello world
print(s.capitalize())   # Hello world
print(s.title())        # Hello World
print(s.swapcase())     # HELLO WORLD → hello world
```

### Strip (remove whitespace)

```python
s = "   hello   "
print(s.strip())    # "hello"    — both sides
print(s.lstrip())   # "hello   " — left only
print(s.rstrip())   # "   hello" — right only

# Strip specific characters
print("***hello***".strip("*"))   # hello
```

### Check Methods (return `bool`)

```python
print("hello".startswith("he"))   # True
print("hello".endswith("lo"))     # True
print("123".isdigit())            # True
print("abc".isalpha())            # True
print("abc123".isalnum())         # True
print("   ".isspace())            # True
print("Hello World".istitle())    # True
```

### Replace

```python
s = "I love cats and cats love me"
print(s.replace("cats", "dogs"))         # I love dogs and dogs love me
print(s.replace("cats", "dogs", 1))      # I love dogs and cats love me (only first)
```

---

## 4. String Formatting

### f-strings (recommended — Python 3.6+)

```python
name = "Alice"
age = 28
score = 95.678

print(f"Name: {name}, Age: {age}")          # Name: Alice, Age: 28
print(f"Score: {score:.2f}")                # Score: 95.68
print(f"{'centered':^20}")                  # '       centered       '
print(f"{42:05d}")                          # 00042
print(f"{1_000_000:,}")                     # 1,000,000
```

### Format Specifiers

| Specifier | Meaning | Example |
|---|---|---|
| `:.2f` | 2 decimal places | `f"{3.14159:.2f}"` → `"3.14"` |
| `:d` | integer | `f"{42:d}"` → `"42"` |
| `:05d` | zero-padded int | `f"{7:05d}"` → `"00007"` |
| `:>10` | right-align, width 10 | `f"{'hi':>10}"` → `"        hi"` |
| `:<10` | left-align | `f"{'hi':<10}"` → `"hi        "` |
| `:^10` | center | `f"{'hi':^10}"` → `"    hi    "` |
| `:,` | thousands separator | `f"{1000000:,}"` → `"1,000,000"` |

---

## 5. Searching and Replacing

```python
text = "the quick brown fox jumps over the lazy dog"

# Finding substrings
print("fox" in text)              # True
print(text.find("fox"))           # 16  — index of first match
print(text.find("cat"))           # -1  — not found
print(text.index("fox"))          # 16  — like find() but raises ValueError if not found
print(text.count("the"))          # 2

# Replace
clean = text.replace("fox", "cat")
print(clean)   # the quick brown cat jumps over the lazy dog
```

---

## 6. Splitting and Joining

### `split()` — string → list

```python
sentence = "one two three four"
words = sentence.split()          # splits on any whitespace
print(words)   # ['one', 'two', 'three', 'four']

csv = "Alice,28,Engineer"
fields = csv.split(",")
print(fields)   # ['Alice', '28', 'Engineer']

# Split with maxsplit
print("a:b:c:d".split(":", 2))   # ['a', 'b', 'c:d']
```

### `join()` — list → string

```python
words = ["Python", "is", "awesome"]
print(" ".join(words))     # Python is awesome
print("-".join(words))     # Python-is-awesome
print("".join(words))      # Pythonisawesome

# Common pattern: split → process → join
sentence = "hello world python"
titled = " ".join(word.capitalize() for word in sentence.split())
print(titled)   # Hello World Python
```

---

## 7. Common Patterns

### Check if palindrome

```python
def is_palindrome(text):
    clean = text.lower().replace(" ", "")
    return clean == clean[::-1]

print(is_palindrome("racecar"))      # True
print(is_palindrome("A man a plan a canal Panama".replace(" ", "")))  # True
print(is_palindrome("hello"))        # False
```

### Count word frequency

```python
text = "the cat sat on the mat the cat"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)   # {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}
```

### Clean and validate input

```python
raw = "  Alice Smith  "
name = raw.strip().title()
print(name)   # Alice Smith

email = "USER@EXAMPLE.COM"
normalized = email.lower().strip()
print(normalized)   # user@example.com
```

### Build a table with f-strings

```python
data = [("Alice", 88), ("Bob", 72), ("Carol", 95)]
print(f"{'Name':<10} {'Score':>6}")
print("-" * 18)
for name, score in data:
    print(f"{name:<10} {score:>6}")
```

Output:
```
Name        Score
------------------
Alice          88
Bob            72
Carol          95
```

---

## Quick Reference

```python
# Basics
s = "Hello, World!"
len(s)               # 13
s[0]                 # 'H'
s[-1]                # '!'
s[7:12]              # 'World'
s[::-1]              # '!dlroW ,olleH'

# Case
s.upper() / s.lower() / s.title() / s.capitalize()

# Strip
s.strip() / s.lstrip() / s.rstrip()

# Search
s.find("World")      # 7   (-1 if not found)
s.count("l")         # 3
"World" in s         # True

# Modify (returns new string)
s.replace("World", "Python")
s.split(", ")        # ['Hello', 'World!']
", ".join(["a","b"]) # 'a, b'

# Check
s.startswith("He")   # True
s.endswith("!")      # True
"123".isdigit()      # True
"abc".isalpha()      # True

# Format
f"{name!r}"          # repr
f"{score:.2f}"       # 2 decimal places
f"{value:>10}"       # right-align width 10
```

---

## What's Next

Practice in the [`exercises/`](./exercises/) folder — try all three levels before checking solutions.

Next concept: [`../mini-projects/`](../mini-projects/)
