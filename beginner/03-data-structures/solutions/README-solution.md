# Solutions — Data Structures (Easy)

> Back to the main repository: [README.md](../../../README.md)  
> Exercises file: [`exercises/01-easy.py`](../exercises/01-easy.py)  
> This file: [`solutions/01-easy-solution.py`](./01-easy-solution.py)

---

## What each exercise reinforces

### Exercise 1 — List indexing (positive and negative)

Lists are the most common sequence type in Python. This exercise builds the two indexing habits you will use constantly:

| Access pattern | Syntax | Notes |
|----------------|--------|-------|
| First element | `lst[0]` | Indices start at **0**, not 1 |
| Last element | `lst[-1]` | Negative indices count from the end |
| Nth from end | `lst[-n]` | `lst[-2]` is second-to-last, etc. |

Using `lst[-1]` is preferred over `lst[len(lst) - 1]` — it is shorter, always correct, and immediately signals "I want the last item".

---

### Exercise 2 — Mutating a list with `append` and `remove`

Lists are **mutable**: you can add, change, or remove items after creation. This exercise practises the two most common mutation methods:

| Method | What it does | Raises if … |
|--------|-------------|-------------|
| `.append(item)` | Adds `item` to the **end** | — (never raises) |
| `.remove(value)` | Removes the **first** occurrence of `value` | `ValueError` if not found |

Key point: both methods modify the list **in place** and return `None`. A common mistake is writing `fruits = fruits.append("grape")` — this replaces your list with `None`.

---

### Exercise 3 — Tuple creation and unpacking

Tuples are **immutable** sequences, ideal for fixed-size groups of related values (like coordinates, RGB colours, or database rows). This exercise introduces two core skills:

- **Creating** a tuple with parentheses: `point = (4, -2, 7)`
- **Unpacking** a tuple into named variables: `x, y, z = point`

Unpacking is more readable than index access (`point[0]`, `point[1]`, …) and self-documents what each position means.

---

### Exercise 4 — Dictionary creation and key-based access

Dictionaries map **keys** to **values**. They are the go-to structure whenever data has a label:

| Operation | Syntax | Notes |
|-----------|--------|-------|
| Create | `d = {"key": value}` | Keys are usually strings |
| Read | `d["key"]` | Raises `KeyError` if missing |
| Safe read | `d.get("key")` | Returns `None` if missing |
| Add/update | `d["key"] = value` | Creates or overwrites the key |
| Delete | `del d["key"]` | Raises `KeyError` if missing |

Since Python 3.7, dictionaries maintain **insertion order**, so iterating over them is predictable.

---

### Exercise 5 — Set deduplication

Sets store **unique** values only. They shine whenever you need to eliminate duplicates or run fast membership tests:

| Property | Detail |
|----------|--------|
| Duplicates | Silently discarded on construction or `.add()` |
| Order | **Unordered** — do not rely on print order |
| Membership | `value in my_set` is O(1) vs O(n) for lists |
| Indexing | **Not supported** — sets have no positional access |

Converting a list to a set and back (`list(set(lst))`) is the fastest one-liner for deduplication, though it does not preserve the original order.

---

## Data structure comparison table

| Feature | `list` | `tuple` | `dict` | `set` |
|---------|--------|---------|--------|-------|
| **Mutable** | Yes | No | Yes | Yes |
| **Ordered** | Yes | Yes | Yes (Python 3.7+) | No |
| **Allows duplicates** | Yes | Yes | Keys: No / Values: Yes | No |
| **Key-value pairs** | No | No | Yes | No |
| **Index access** | Yes (`lst[i]`) | Yes (`tup[i]`) | By key (`d[k]`) | No |
| **Typical use case** | Ordered, changeable sequence | Fixed record / multiple return value | Named data / fast lookup by key | Unique items / membership tests |
| **Literal syntax** | `[1, 2, 3]` | `(1, 2, 3)` | `{"a": 1}` | `{1, 2, 3}` |
| **Empty literal** | `[]` | `()` | `{}` | `set()` ← not `{}`! |

---

## Common beginner mistakes

### 1. Tuple with one element needs a trailing comma

```python
# WRONG — parentheses alone do NOT create a tuple
single = (42)
print(type(single))   # <class 'int'>

# CORRECT — add a trailing comma
single = (42,)
print(type(single))   # <class 'tuple'>

# Also valid — parentheses are optional for tuples
single = 42,
print(type(single))   # <class 'tuple'>
```

### 2. Dictionary keys must be hashable (immutable)

```python
# WRONG — lists are mutable and cannot be dict keys
d = {[1, 2]: "value"}   # raises TypeError: unhashable type: 'list'

# CORRECT — use a tuple instead (tuples are immutable and hashable)
d = {(1, 2): "value"}
print(d[(1, 2)])   # "value"
```

### 3. List index out of range

```python
fruits = ["apple", "banana", "cherry"]   # 3 items, indices 0-2

# WRONG — index 3 does not exist
print(fruits[3])    # raises IndexError: list index out of range

# CORRECT — last valid index is len(fruits) - 1, or use -1
print(fruits[2])    # "cherry"
print(fruits[-1])   # "cherry"
```

### 4. Modifying a list while iterating over it

```python
numbers = [1, 2, 3, 4, 5]

# WRONG — skips elements because removing shifts indices
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)   # modifies the list mid-loop — unpredictable!

print(numbers)   # [1, 3, 5] — looks right here, but often breaks

# CORRECT — iterate over a copy, or build a new list
numbers = [1, 2, 3, 4, 5]
numbers = [n for n in numbers if n % 2 != 0]   # list comprehension
print(numbers)   # [1, 3, 5]
```

### 5. Confusing `dict.keys()` with a list

```python
person = {"name": "Alice", "age": 30}

keys = person.keys()
print(type(keys))   # <class 'dict_keys'> — NOT a list

# WRONG — dict_keys does not support indexing
print(keys[0])      # raises TypeError: 'dict_keys' object is not subscriptable

# CORRECT — convert to a list first if you need indexing
keys_list = list(person.keys())
print(keys_list[0])   # "name"

# Or just iterate directly — dict_keys is iterable
for key in person.keys():
    print(key, "→", person[key])
```

### 6. Sets are unordered — no indexing

```python
colors = {"red", "green", "blue"}

# WRONG — sets have no positional index
print(colors[0])    # raises TypeError: 'set' object is not subscriptable

# CORRECT — convert to a sorted list if order matters
print(sorted(colors)[0])   # "blue" (alphabetical)

# Or simply iterate
for color in colors:
    print(color)
```

### 7. Empty set vs empty dict

```python
# WRONG — {} creates an empty DICT, not an empty set
empty = {}
print(type(empty))   # <class 'dict'>

# CORRECT — use set() with no arguments
empty_set = set()
print(type(empty_set))   # <class 'set'>
```

### 8. Forgetting that `list.append()` returns `None`

```python
fruits = ["apple", "banana"]

# WRONG — reassigning the return value of append()
fruits = fruits.append("cherry")
print(fruits)   # None  ← your list is gone!

# CORRECT — append() modifies in place; do not reassign
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)   # ['apple', 'banana', 'cherry']
```

---

## Key built-ins and methods introduced

| Built-in / Method | Purpose |
|-------------------|---------|
| `list.append(x)` | Add `x` to the end of the list |
| `list.remove(x)` | Remove first occurrence of `x` |
| `list.sort()` | Sort the list in place |
| `len(obj)` | Number of elements in any sequence or mapping |
| `dict.get(key, default)` | Safe key access (no KeyError) |
| `dict.keys()` | View of all keys |
| `dict.values()` | View of all values |
| `dict.items()` | View of all (key, value) pairs |
| `set.add(x)` | Add `x` to the set |
| `set.discard(x)` | Remove `x` if present (no error if missing) |
| `set.union(other)` | All elements from both sets (`\|`) |
| `set.intersection(other)` | Elements in both sets (`&`) |
| `set.difference(other)` | Elements only in this set (`-`) |

---

## Further reading

- [Python Docs — Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Docs — Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python Docs — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Docs — Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Real Python — Lists and Tuples](https://realpython.com/python-list/)
- [Real Python — Dictionaries](https://realpython.com/python-dicts/)
