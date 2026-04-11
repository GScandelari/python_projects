# Solutions Guide — 05-string-manipulation

---

## What Each Exercise Reinforces

### Exercise 1 — Indexing and Slicing
**Concept:** String indexing and the `[start:stop:step]` slice syntax.  
The reverse trick `[::-1]` and step-based slices like `[::2]` are used constantly in practice. Remember: strings are zero-indexed and slices never raise an `IndexError` for out-of-range boundaries.

### Exercise 2 — Case and Strip Methods
**Concept:** Non-destructive string methods.  
Every string method returns a **new string** — the original is unchanged (strings are immutable). Chaining works because each method returns a string: `raw.strip().title()`.

### Exercise 3 — Counting (case-insensitive)
**Concept:** Normalizing before searching.  
Always convert to a consistent case before counting or comparing: `s.lower().count("a")`. This pattern applies to search, sort, and deduplication tasks.

### Exercise 4 — `startswith` / `endswith`
**Concept:** Predicate methods that return `bool`.  
Both accept a tuple of prefixes/suffixes: `filename.endswith((".py", ".txt"))` — useful for file-type checks.

### Exercise 5 — `replace` + Method Chaining
**Concept:** Transforming strings with chained methods.  
`str.replace(old, new)` replaces ALL occurrences by default. Pass a third argument to limit: `s.replace(" ", "_", 2)` replaces only the first 2.

---

## Slice Syntax Reference

```
text[start : stop : step]
```

| Expression | Result on `"Python"` | Meaning |
|---|---|---|
| `text[0]` | `'P'` | first character |
| `text[-1]` | `'n'` | last character |
| `text[2:5]` | `'tho'` | index 2 up to (not incl.) 5 |
| `text[:3]` | `'Pyt'` | from start to 3 |
| `text[3:]` | `'hon'` | from 3 to end |
| `text[::2]` | `'Pto'` | every 2nd character |
| `text[::-1]` | `'nohtyP'` | reversed |

---

## Common Beginner Mistakes

### 1. Treating strings as mutable
```python
word = "Hello"
word[0] = "h"   # TypeError: 'str' object does not support item assignment

# Fix: create a new string
word = "h" + word[1:]
```

### 2. Forgetting that methods return new strings
```python
s = "  hello  "
s.strip()        # does nothing to s — result is discarded
print(s)         # "  hello  "  — unchanged!

# Fix: assign the result
s = s.strip()
```

### 3. Off-by-one in slices
```python
text = "Python"
print(text[0:3])   # "Pyt" — stop index is EXCLUSIVE
print(text[1:4])   # "yth"
```

### 4. `find()` vs `index()` — silent failure vs exception
```python
s = "hello"
print(s.find("z"))    # -1  — not found, no error
print(s.index("z"))   # ValueError: substring not found

# Use find() when absence is expected; index() when it must be present
```

### 5. Case-sensitive comparisons
```python
"Python" == "python"         # False
"Python".lower() == "python" # True — always normalize first
```

### 6. Joining non-string items
```python
parts = [1, 2, 3]
", ".join(parts)   # TypeError: sequence item 0: expected str instance, int found

# Fix: convert each item to str first
", ".join(str(p) for p in parts)   # "1, 2, 3"
```

---

## Further Reading

- [README](../README.md) — Full concept explanations  
- [Exercises](../exercises/01-easy.py) — Try before looking here  
- [Solutions](./01-easy-solution.py) — Annotated working code
