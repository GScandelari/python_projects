# 03 — Data Structures

So far you have worked with single values: one number, one string, one boolean.
Real programs need to manage **collections** of data — a shopping list, a
phonebook, a set of unique tags. Python provides four built-in structures for
this: **lists**, **tuples**, **dictionaries**, and **sets**.

No imports are needed for anything on this page. Every code block is ready to
run as-is.

---

## Table of Contents

1. [Lists](#1-lists)
   - 1.1 [Creating a List](#11-creating-a-list)
   - 1.2 [Indexing and Slicing](#12-indexing-and-slicing)
   - 1.3 [Mutability](#13-mutability)
   - 1.4 [Common Methods](#14-common-methods)
   - 1.5 [List as a Stack and Queue](#15-list-as-a-stack-and-queue)
2. [Tuples](#2-tuples)
   - 2.1 [Creating a Tuple](#21-creating-a-tuple)
   - 2.2 [Indexing and Immutability](#22-indexing-and-immutability)
   - 2.3 [When to Use Tuples over Lists](#23-when-to-use-tuples-over-lists)
   - 2.4 [Packing, Unpacking, and the Swap Idiom](#24-packing-unpacking-and-the-swap-idiom)
3. [Dictionaries](#3-dictionaries)
   - 3.1 [Creating a Dictionary](#31-creating-a-dictionary)
   - 3.2 [Accessing, Updating, and Deleting](#32-accessing-updating-and-deleting)
   - 3.3 [Common Methods](#33-common-methods)
   - 3.4 [Iterating over a Dictionary](#34-iterating-over-a-dictionary)
4. [Sets](#4-sets)
   - 4.1 [Creating a Set](#41-creating-a-set)
   - 4.2 [Adding and Removing Elements](#42-adding-and-removing-elements)
   - 4.3 [Set Operations](#43-set-operations)
   - 4.4 [Use Cases](#44-use-cases)
5. [Choosing the Right Structure](#5-choosing-the-right-structure)
6. [Quick Reference](#quick-reference)
7. [What's Next](#whats-next)

---

## 1. Lists

A **list** is an ordered, mutable collection of items. Items can be of any type,
and duplicates are allowed.

### 1.1 Creating a List

Use square brackets `[]`. Separate items with commas.

```python
# A list of strings
fruits = ["apple", "banana", "cherry"]

# A list of numbers
scores = [88, 72, 95, 60, 84]

# A mixed list (allowed, but uncommon in practice)
mixed = [42, "hello", True, 3.14]

# An empty list
empty = []

print(fruits)   # ['apple', 'banana', 'cherry']
print(scores)   # [88, 72, 95, 60, 84]
print(len(fruits))  # 3  — number of items
```

### 1.2 Indexing and Slicing

Lists are **zero-indexed**: the first item is at index `0`.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexes (count from the left, starting at 0)
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[4])   # elderberry

# Negative indexes (count from the right, starting at -1)
print(fruits[-1])  # elderberry  — last item
print(fruits[-2])  # date        — second-to-last
```

**Slicing** extracts a portion of the list using the syntax `list[start:stop:step]`.
The `stop` index is **not** included in the result.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[1:3])    # ['banana', 'cherry']  — indexes 1 and 2
print(fruits[:3])     # ['apple', 'banana', 'cherry']  — from the start
print(fruits[2:])     # ['cherry', 'date', 'elderberry']  — to the end
print(fruits[::2])    # ['apple', 'cherry', 'elderberry']  — every other item
print(fruits[::-1])   # reversed list
```

### 1.3 Mutability

Unlike strings, lists can be changed after creation. You can replace, add, or
remove items at any time.

```python
colors = ["red", "green", "blue"]

# Replace an item
colors[1] = "yellow"
print(colors)  # ['red', 'yellow', 'blue']

# Replace a slice
colors[0:2] = ["pink", "purple"]
print(colors)  # ['pink', 'purple', 'blue']
```

### 1.4 Common Methods

Python lists come with many built-in methods. Here are the ones you will use most.

| Method | What it does |
|--------|-------------|
| `append(x)` | Add `x` to the end |
| `extend(iterable)` | Add all items from another list (or any iterable) to the end |
| `insert(i, x)` | Insert `x` at index `i` |
| `remove(x)` | Remove the **first** occurrence of `x` (raises `ValueError` if not found) |
| `pop(i)` | Remove and **return** the item at index `i` (default: last item) |
| `sort()` | Sort the list in place (ascending by default) |
| `reverse()` | Reverse the list in place |
| `len(list)` | Return the number of items (built-in function, not a method) |
| `count(x)` | Return how many times `x` appears |
| `index(x)` | Return the index of the **first** occurrence of `x` |

```python
# append — add one item to the end
cart = ["milk", "eggs"]
cart.append("bread")
print(cart)  # ['milk', 'eggs', 'bread']

# extend — merge another list in
cart.extend(["butter", "cheese"])
print(cart)  # ['milk', 'eggs', 'bread', 'butter', 'cheese']

# insert — add at a specific position
cart.insert(1, "yogurt")
print(cart)  # ['milk', 'yogurt', 'eggs', 'bread', 'butter', 'cheese']

# remove — delete the first matching item
cart.remove("eggs")
print(cart)  # ['milk', 'yogurt', 'bread', 'butter', 'cheese']

# pop — remove and return (default: last item)
last = cart.pop()
print(last)  # cheese
print(cart)  # ['milk', 'yogurt', 'bread', 'butter']

# pop at a specific index
first = cart.pop(0)
print(first)  # milk
print(cart)   # ['yogurt', 'bread', 'butter']
```

```python
# sort — sorts the list in place (modifies the original)
numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()
print(numbers)  # [1, 2, 3, 5, 8, 9]

numbers.sort(reverse=True)
print(numbers)  # [9, 8, 5, 3, 2, 1]

# reverse — reverses in place
numbers.reverse()
print(numbers)  # [1, 2, 3, 5, 8, 9]
```

```python
# count and index
votes = ["Alice", "Bob", "Alice", "Carol", "Alice", "Bob"]

print(votes.count("Alice"))  # 3
print(votes.count("Bob"))    # 2
print(votes.index("Carol"))  # 3  — position of first "Carol"
```

> **Tip:** `sort()` and `reverse()` modify the list in place and return `None`.
> If you need a new sorted list without changing the original, use the built-in
> `sorted()` function instead: `new_list = sorted(original)`.

### 1.5 List as a Stack and Queue

**Stack (Last In, First Out — LIFO):** use `append()` to push and `pop()` to pop.

```python
stack = []
stack.append("first")
stack.append("second")
stack.append("third")

print(stack.pop())  # third   — last item comes out first
print(stack.pop())  # second
print(stack.pop())  # first
```

**Queue (First In, First Out — FIFO):** use `append()` to enqueue and `pop(0)`
to dequeue. (For large queues, `collections.deque` is more efficient, but
`pop(0)` is fine for learning.)

```python
queue = []
queue.append("Alice")    # Alice joins the queue
queue.append("Bob")
queue.append("Carol")

print(queue.pop(0))  # Alice  — first in, first out
print(queue.pop(0))  # Bob
print(queue.pop(0))  # Carol
```

---

## 2. Tuples

A **tuple** is an ordered, **immutable** collection. Once created, it cannot be
changed. Tuples use parentheses `()` instead of square brackets.

### 2.1 Creating a Tuple

```python
# A tuple of coordinates
point = (3, 7)

# A tuple of RGB values
color = (255, 128, 0)

# A tuple of strings
directions = ("north", "south", "east", "west")

# A single-item tuple — note the trailing comma (required!)
single = (42,)
print(type(single))   # <class 'tuple'>

# Without the comma it is just parentheses around a number
not_a_tuple = (42)
print(type(not_a_tuple))  # <class 'int'>

# An empty tuple
empty = ()
```

### 2.2 Indexing and Immutability

Tuples support the same indexing and slicing as lists.

```python
point = (10, 20, 30)

print(point[0])    # 10
print(point[-1])   # 30
print(point[1:])   # (20, 30)
```

Trying to change a tuple raises a `TypeError`:

```python
point = (10, 20, 30)
# point[0] = 99   # TypeError: 'tuple' object does not support item assignment
```

### 2.3 When to Use Tuples over Lists

| Situation | Use |
|-----------|-----|
| The data should not change (e.g. a coordinate, a date) | Tuple |
| You want to communicate "this is fixed" to other programmers | Tuple |
| You need to use it as a dictionary key | Tuple (lists cannot be keys) |
| The collection will grow, shrink, or be modified | List |

```python
# Coordinates should not change — a tuple makes that intent clear
origin = (0, 0)
screen_resolution = (1920, 1080)

# Use a tuple as a dictionary key (a list would cause a TypeError)
distances = {
    (0, 0): 0,
    (3, 4): 5,
    (6, 8): 10,
}
print(distances[(3, 4)])  # 5
```

### 2.4 Packing, Unpacking, and the Swap Idiom

**Packing** — combining values into a tuple:

```python
person = ("Alice", 30, "engineer")   # packed into one tuple
```

**Unpacking** — extracting values into separate variables:

```python
person = ("Alice", 30, "engineer")
name, age, job = person

print(name)  # Alice
print(age)   # 30
print(job)   # engineer
```

The number of variables on the left must match the number of items in the tuple
(unless you use `*` to capture extras).

```python
# Capturing extras with *
first, *rest = (1, 2, 3, 4, 5)
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

*start, last = (1, 2, 3, 4, 5)
print(start)  # [1, 2, 3, 4]
print(last)   # 5
```

**The swap idiom** — swap two variables without a temporary helper:

```python
a = "hello"
b = "world"

a, b = b, a   # Python packs the right side into a tuple, then unpacks it

print(a)  # world
print(b)  # hello
```

---

## 3. Dictionaries

A **dictionary** (or `dict`) stores data as **key–value pairs**. Look up a value
instantly by its key, just like looking up a word in a real dictionary.
Dictionaries are mutable and, since Python 3.7, maintain insertion order.

### 3.1 Creating a Dictionary

Use curly braces `{}` with `key: value` pairs separated by commas.

```python
# A simple phonebook
phonebook = {
    "Alice": "555-1234",
    "Bob":   "555-5678",
    "Carol": "555-8765",
}

# Keys and values can be of different types
profile = {
    "name": "Alice",
    "age":  30,
    "active": True,
}

# An empty dictionary
empty = {}

print(phonebook)         # {'Alice': '555-1234', 'Bob': '555-5678', ...}
print(len(phonebook))    # 3
```

> **Rules for keys:** Keys must be of an **immutable** type (strings, numbers,
> tuples). Lists cannot be keys. Each key in a dictionary must be **unique** —
> if you repeat a key, the second value overwrites the first.

### 3.2 Accessing, Updating, and Deleting

**Accessing a value:**

```python
phonebook = {"Alice": "555-1234", "Bob": "555-5678"}

print(phonebook["Alice"])   # 555-1234
# print(phonebook["Dave"])  # KeyError — "Dave" is not in the dictionary
```

**Updating an existing key or adding a new one:**

```python
profile = {"name": "Alice", "age": 30}

profile["age"] = 31              # update existing key
profile["city"] = "New York"     # add a new key

print(profile)  # {'name': 'Alice', 'age': 31, 'city': 'New York'}
```

**Deleting a key:**

```python
profile = {"name": "Alice", "age": 31, "city": "New York"}

del profile["city"]
print(profile)  # {'name': 'Alice', 'age': 31}
```

**Checking if a key exists:**

```python
phonebook = {"Alice": "555-1234", "Bob": "555-5678"}

print("Alice" in phonebook)   # True
print("Dave" in phonebook)    # False
```

### 3.3 Common Methods

| Method | What it does |
|--------|-------------|
| `keys()` | Return a view of all keys |
| `values()` | Return a view of all values |
| `items()` | Return a view of all `(key, value)` pairs |
| `get(key, default)` | Return the value for `key`, or `default` if the key is missing (no error) |
| `pop(key)` | Remove and return the value for `key` (raises `KeyError` if missing) |
| `update(other)` | Merge another dictionary in (overwrites duplicate keys) |

```python
scores = {"Alice": 88, "Bob": 75, "Carol": 92}

print(list(scores.keys()))    # ['Alice', 'Bob', 'Carol']
print(list(scores.values()))  # [88, 75, 92]
print(list(scores.items()))   # [('Alice', 88), ('Bob', 75), ('Carol', 92)]
```

```python
# get — safe lookup with a fallback value
scores = {"Alice": 88, "Bob": 75}

print(scores.get("Alice"))          # 88
print(scores.get("Dave"))           # None   — no error
print(scores.get("Dave", 0))        # 0      — custom default
```

```python
# pop — remove a key and return its value
scores = {"Alice": 88, "Bob": 75, "Carol": 92}

alice_score = scores.pop("Alice")
print(alice_score)  # 88
print(scores)       # {'Bob': 75, 'Carol': 92}
```

```python
# update — merge dictionaries
defaults = {"theme": "light", "font_size": 14, "language": "en"}
user_prefs = {"theme": "dark", "font_size": 18}

defaults.update(user_prefs)
print(defaults)
# {'theme': 'dark', 'font_size': 18, 'language': 'en'}
```

### 3.4 Iterating over a Dictionary

```python
population = {"Brazil": 215_000_000, "Germany": 84_000_000, "Japan": 125_000_000}

# Iterate over keys (default behaviour)
for country in population:
    print(country)

# Iterate over values
for pop in population.values():
    print(pop)

# Iterate over key–value pairs (most common)
for country, pop in population.items():
    print(f"{country}: {pop:,}")
```

Output:
```
Brazil: 215,000,000
Germany: 84,000,000
Japan: 125,000,000
```

```python
# Build a frequency counter using a dictionary
sentence = "to be or not to be"
word_count = {}

for word in sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}
```

---

## 4. Sets

A **set** is an **unordered** collection of **unique** items. It is written with
curly braces `{}`, but without key–value pairs. Sets are mutable, but their
items must be immutable (just like dictionary keys).

### 4.1 Creating a Set

```python
# A set of tags
tags = {"python", "beginner", "tutorial"}

# Duplicates are automatically removed
numbers = {1, 2, 3, 2, 1, 4}
print(numbers)  # {1, 2, 3, 4}  — order may vary

# An empty set — must use set(), not {} (that creates an empty dict!)
empty = set()
print(type(empty))  # <class 'set'>

# Create a set from a list
letters = set(["a", "b", "c", "a", "b"])
print(letters)  # {'a', 'b', 'c'}
```

> **Sets are unordered.** When you print a set you may see the items in any
> order. Do not rely on position — there are no indexes in a set.

### 4.2 Adding and Removing Elements

```python
permissions = {"read", "write"}

# add — insert a single item
permissions.add("execute")
print(permissions)  # {'read', 'write', 'execute'}  (order may vary)

# Adding a duplicate has no effect
permissions.add("read")
print(permissions)  # {'read', 'write', 'execute'}  — no change

# remove — raises a KeyError if the item is not present
permissions.remove("write")
print(permissions)  # {'read', 'execute'}

# discard — like remove, but does NOT raise an error if the item is missing
permissions.discard("admin")   # 'admin' is not there — no error

# Check membership with in
print("read" in permissions)   # True
print("write" in permissions)  # False
```

### 4.3 Set Operations

Sets shine when comparing collections. These operations mirror mathematical set
theory.

| Operation | Operator | Method | Result |
|-----------|----------|--------|--------|
| Union | `\|` | `.union()` | All items from both sets |
| Intersection | `&` | `.intersection()` | Items present in **both** sets |
| Difference | `-` | `.difference()` | Items in A but **not** in B |
| Symmetric difference | `^` | `.symmetric_difference()` | Items in one set but **not** both |

```python
python_students = {"Alice", "Bob", "Carol", "Dave"}
java_students   = {"Bob", "Dave", "Eve", "Frank"}

# Union — who studies at least one of the two?
print(python_students | java_students)
# {'Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank'}

# Intersection — who studies both?
print(python_students & java_students)
# {'Bob', 'Dave'}

# Difference — who studies Python but not Java?
print(python_students - java_students)
# {'Alice', 'Carol'}

# Symmetric difference — who studies exactly one of the two?
print(python_students ^ java_students)
# {'Alice', 'Carol', 'Eve', 'Frank'}
```

You can also use the method forms, which work the same way:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))                  # {1, 2, 3, 4, 5, 6}
print(a.intersection(b))           # {3, 4}
print(a.difference(b))             # {1, 2}
print(a.symmetric_difference(b))   # {1, 2, 5, 6}
```

### 4.4 Use Cases

**Deduplication** — remove duplicates from a list in one step:

```python
responses = ["yes", "no", "yes", "maybe", "no", "yes"]
unique_responses = list(set(responses))
print(unique_responses)   # ['maybe', 'no', 'yes']  (order may vary)
```

**Fast membership testing** — checking `x in set` is much faster than
`x in list` for large collections:

```python
banned_words = {"spam", "scam", "phishing"}

message = "this is a spam message"
words = message.split()

for word in words:
    if word in banned_words:
        print(f"Warning: banned word found — '{word}'")
```

**Finding common or unique items:**

```python
monday_visitors    = {"Alice", "Bob", "Carol", "Dave"}
tuesday_visitors   = {"Carol", "Dave", "Eve"}

# Who came both days?
both_days = monday_visitors & tuesday_visitors
print(f"Returned: {both_days}")   # {'Carol', 'Dave'}

# Who came only on Monday?
monday_only = monday_visitors - tuesday_visitors
print(f"Monday only: {monday_only}")   # {'Alice', 'Bob'}
```

---

## 5. Choosing the Right Structure

When you face a new problem, use this table to pick the right container.

| Structure | Mutable? | Ordered? | Duplicates allowed? | Key–value pairs? | Typical use case |
|-----------|----------|----------|---------------------|------------------|-----------------|
| `list` | Yes | Yes | Yes | No | Sequence of items that may change |
| `tuple` | No | Yes | Yes | No | Fixed record; safe as a dict key |
| `dict` | Yes | Yes (3.7+) | Keys: No / Values: Yes | Yes | Lookup table, named data |
| `set` | Yes | No | No | No | Uniqueness checks, set math |

**In plain English:**

- Need to keep a **sequence** you can add to or sort? → **list**
- Have a **fixed record** that should not change (e.g. a coordinate, an RGB
  value)? → **tuple**
- Need to look something up **by name** or associate data with labels? →
  **dict**
- Need to guarantee **uniqueness** or compare groups of items? → **set**

```python
# list — a playlist that changes over time
playlist = ["Song A", "Song B", "Song C"]
playlist.append("Song D")

# tuple — an immutable point on a map
location = (48.8566, 2.3522)   # Paris, latitude and longitude

# dict — a student record with named fields
student = {"name": "Alice", "grade": "A", "score": 95}

# set — unique categories assigned to an article
tags = {"python", "tutorial", "beginner"}
tags.add("python")   # already there — no change
```

---

## Quick Reference

```python
# ── LISTS ────────────────────────────────────────────────────────
lst = [1, 2, 3]
lst[0]            # index — first item
lst[-1]           # index — last item
lst[1:3]          # slice — items at index 1 and 2
lst.append(4)     # add to end
lst.extend([5,6]) # merge another list
lst.insert(0, 0)  # insert at position
lst.remove(2)     # remove first match
lst.pop()         # remove and return last item
lst.pop(0)        # remove and return item at index 0
lst.sort()        # sort in place
lst.reverse()     # reverse in place
len(lst)          # number of items
lst.count(1)      # occurrences of 1
lst.index(3)      # index of first 3

# ── TUPLES ───────────────────────────────────────────────────────
tup = (1, 2, 3)
tup[0]            # index
a, b, c = tup     # unpack
a, b = b, a       # swap two variables

# ── DICTIONARIES ─────────────────────────────────────────────────
d = {"key": "value"}
d["key"]              # access (KeyError if missing)
d.get("key", default) # safe access with fallback
d["new_key"] = 99     # add / update
del d["key"]          # delete
"key" in d            # membership test
d.keys()              # view of keys
d.values()            # view of values
d.items()             # view of (key, value) pairs
d.pop("key")          # remove and return
d.update(other_dict)  # merge

# ── SETS ─────────────────────────────────────────────────────────
s = {1, 2, 3}
s.add(4)          # add one item
s.remove(2)       # remove (KeyError if missing)
s.discard(99)     # remove (no error if missing)
x in s            # membership test
a | b             # union
a & b             # intersection
a - b             # difference
a ^ b             # symmetric difference
list(set(lst))    # deduplicate a list
```

---

## What's Next

Head over to the **[exercises](./exercises/)** folder. The exercises are grouped
by structure — lists first, then tuples, dictionaries, and sets — and increase
in difficulty within each group.

Try to solve every challenge on your own before looking anything up. Typing the
code yourself, making mistakes, and correcting them is how these patterns become
second nature.

After you are comfortable with these four structures, continue to
**`04-functions/`** where you will learn how to bundle logic into reusable
blocks — and how data structures and functions work together to solve bigger
problems.

Good luck!