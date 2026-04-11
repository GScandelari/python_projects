# List, Dict & Set Comprehensions

Comprehensions are a concise, Pythonic way to build collections from iterables. They replace many `for` loops that accumulate results into a list, dict, or set — in a single readable expression.

## Table of Contents

- [List Comprehension](#1-list-comprehension)
- [Filtering with if](#2-filtering-with-if)
- [if/else inside a comprehension](#3-ifelse-inside-a-comprehension)
- [Nested Comprehensions](#4-nested-comprehensions)
- [Dict Comprehensions](#5-dict-comprehensions)
- [Set Comprehensions](#6-set-comprehensions)
- [Generator Expressions](#7-generator-expressions)
- [When NOT to use comprehensions](#8-when-not-to-use-comprehensions)
- [Quick Reference](#quick-reference)
- [What's Next](#whats-next)

---

## 1. List Comprehension

**Syntax:** `[expression for item in iterable]`

```python
# Loop version
squares = []
for n in range(1, 6):
    squares.append(n ** 2)

# Comprehension version — same result, one line
squares = [n ** 2 for n in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]
```

Read it left to right: "give me `n ** 2` for every `n` in `range(1, 6)`".

```python
names = ["alice", "bob", "carol"]
upper = [name.upper() for name in names]
print(upper)   # ['ALICE', 'BOB', 'CAROL']

# Works with any iterable
lengths = [len(name) for name in names]
print(lengths)   # [5, 3, 5]
```

---

## 2. Filtering with if

**Syntax:** `[expression for item in iterable if condition]`

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [n for n in numbers if n % 2 == 0]
print(evens)   # [2, 4, 6, 8, 10]

# Combine transformation + filter
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)   # [4, 16, 36, 64, 100]
```

---

## 3. if/else inside a comprehension

When the `if` controls the **value** (not filtering), it goes *before* the `for`:

```python
# Syntax: [value_if_true if condition else value_if_false for item in iterable]
labels = ["even" if n % 2 == 0 else "odd" for n in range(1, 6)]
print(labels)   # ['odd', 'even', 'odd', 'even', 'odd']

# Combine both: transform with if/else, then filter
result = [n * 2 if n % 2 == 0 else n for n in range(1, 11) if n > 3]
print(result)   # [5, 12, 7, 16, 9, 20]
```

---

## 4. Nested Comprehensions

A second `for` clause handles nested iteration:

```python
# Flatten a 2D matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [val for row in matrix for val in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Cartesian product
pairs = [(x, y) for x in [1, 2, 3] for y in ["a", "b"]]
print(pairs)
# [(1,'a'), (1,'b'), (2,'a'), (2,'b'), (3,'a'), (3,'b')]

# Build a 3×3 multiplication table as a 2D list
table = [[row * col for col in range(1, 4)] for row in range(1, 4)]
for row in table:
    print(row)
# [1, 2, 3]
# [2, 4, 6]
# [3, 6, 9]
```

---

## 5. Dict Comprehensions

**Syntax:** `{key_expr: value_expr for item in iterable}`

```python
# Square each number, keyed by the number itself
squares = {n: n ** 2 for n in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Invert a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)   # {1: 'a', 2: 'b', 3: 'c'}

# Filter while building
words = ["hello", "world", "python", "hi"]
long_words = {w: len(w) for w in words if len(w) > 3}
print(long_words)   # {'hello': 5, 'world': 5, 'python': 6}

# Normalize keys (uppercase) from a list of strings
keys = ["Name", "AGE", "city"]
normalized = {k.lower(): None for k in keys}
print(normalized)   # {'name': None, 'age': None, 'city': None}
```

---

## 6. Set Comprehensions

**Syntax:** `{expression for item in iterable}`

```python
# Unique squared values
numbers = [1, -1, 2, -2, 3]
unique_squares = {n ** 2 for n in numbers}
print(unique_squares)   # {1, 4, 9}  (order may vary)

# Unique first characters
words = ["apple", "ant", "banana", "avocado", "cherry"]
first_chars = {w[0] for w in words}
print(first_chars)   # {'a', 'b', 'c'}

# Deduplicate while filtering
raw = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
unique_evens = {n for n in raw if n % 2 == 0}
print(unique_evens)   # {2, 4, 6}
```

---

## 7. Generator Expressions

Replace `[...]` with `(...)` to get a **generator** — lazy, memory-efficient. Use when you only need to iterate once and don't need a list.

```python
# List: builds the entire list in memory
total = sum([n ** 2 for n in range(1_000_000)])

# Generator: computes values on demand — same result, less memory
total = sum(n ** 2 for n in range(1_000_000))

# Works as argument to any function that accepts an iterable
words = ["Python", "is", "great"]
longest = max(words, key=lambda w: len(w))   # internally a generator

# all() / any() short-circuit with generators
nums = [2, 4, 6, 8, 10]
print(all(n % 2 == 0 for n in nums))   # True
print(any(n > 8 for n in nums))        # True
```

---

## 8. When NOT to use comprehensions

Comprehensions improve readability when **simple**. Avoid them when:

| Situation | Prefer instead |
|---|---|
| Logic requires 3+ lines per element | Regular `for` loop |
| Side effects needed (print, log, mutate) | Regular `for` loop |
| Multiple `if` conditions get complex | Regular `for` loop |
| Deeply nested (3+ levels) | Break into functions |
| You only need to iterate once | Generator expression |

```python
# Too complex — use a loop
result = [process(x) for x in items if condition1(x) if condition2(x) if condition3(x)]

# Better
result = []
for x in items:
    if condition1(x) and condition2(x) and condition3(x):
        result.append(process(x))
```

---

## Quick Reference

```python
# List comprehension
[expr for x in iterable]
[expr for x in iterable if cond]
[a if cond else b for x in iterable]

# Nested
[expr for x in outer for y in inner]
[[expr for y in inner] for x in outer]   # 2D list

# Dict comprehension
{k: v for x in iterable}
{k: v for x in iterable if cond}

# Set comprehension
{expr for x in iterable}

# Generator expression
(expr for x in iterable)
sum(expr for x in iterable)   # no extra parens needed as sole arg
```

---

## What's Next

Try the exercises in [`exercises/`](./exercises/) — convert loops to comprehensions, build dicts and sets from scratch.

Next concept: [`mini-projects/`](../mini-projects/)
