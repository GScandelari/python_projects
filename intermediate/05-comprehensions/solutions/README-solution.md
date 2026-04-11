# Solutions Guide — 05-comprehensions

---

## What Each Exercise Reinforces

### Easy 1 — uppercase
**Concept:** Basic list comprehension replacing `append` in a loop.  
`[expr for x in iterable]` is the canonical form. Any method call works as the expression.

### Easy 2 — squares
**Concept:** Arithmetic expression inside a comprehension.  
`range(1, 11)` is the idiomatic way to get 1–10 inclusive.

### Easy 3 — filter evens
**Concept:** `if` clause for filtering (drops elements that don't match).  
The `if` at the end of the comprehension acts as a filter gate — elements that fail never appear in the output.

### Easy 4 — extract strings
**Concept:** `isinstance()` as the filter predicate.  
Note that `bool` is a subclass of `int` but not of `str`, so `isinstance(True, str)` is `False`. This is exactly what we want here.

### Easy 5 — word → length dict
**Concept:** Dict comprehension `{k: v for x in iterable}`.  
`len()` as the value expression is a common pattern for building lookup tables.

### Easy 6 — unique first letters (set)
**Concept:** Set comprehension `{expr for x in iterable}`.  
Duplicates are automatically discarded — no need to track "already seen" state.

---

### Medium 1 — even/odd labels
**Concept:** Ternary `a if cond else b` before the `for` clause.  
The position matters: `[value_if_true if cond else value_if_false for x in it]` transforms every element. Compare with `[expr for x in it if cond]`, which filters.

### Medium 2 — student pass/fail
**Concept:** Computed expression as the value in a dict comprehension.  
Inline `sum(g)/len(g)` keeps everything in one expression. For more complex logic, extract a helper function first.

### Medium 3 — flatten matrix
**Concept:** Nested `for` clauses — `[val for row in matrix for val in row]`.  
Read left to right: outer loop `row in matrix`, then inner loop `val in row`. The order mirrors how you'd write the equivalent nested `for` loops.

### Medium 4 — Cartesian product
**Concept:** Two `for` clauses + `if` to exclude diagonal.  
Multiple `for` clauses create a Cartesian product. The `if x != y` filter is applied after both variables are bound.

### Medium 5 — character frequency
**Concept:** Using `set()` inside a comprehension to deduplicate keys.  
Iterating over `set(cleaned)` ensures each character is a key exactly once. `.count()` does the counting for each key.

### Medium 6 — XOR divisibility (set comprehension)
**Concept:** Boolean XOR via `!=` on two conditions.  
`(n % 3 == 0) != (n % 7 == 0)` is True when exactly one condition is True — clean alternative to `(a or b) and not (a and b)`.

---

### Challenge 1 — Pipeline comprehension
**Concept:** Chaining transformation and filtering in one expression.  
Float conversion is computed twice (`float(item["price"])`) to keep it as a single comprehension. If that were expensive, you'd use a walrus operator (`:=`, Python 3.8+) or split into two steps.

### Challenge 2 — Invert and group
**Concept:** Two comprehensions composing: a set comprehension to collect unique subjects, then a dict comprehension to invert.  
The inner list comprehension `[student for student, subjects in enrollment.items() if subject in subjects]` is a nested comprehension inside the outer dict comprehension.

### Challenge 3 — Generator expressions
**Concept:** Lazy evaluation, memory efficiency, short-circuit evaluation.  
- `next(gen)` pulls exactly one value — ideal for "find first".  
- `sum(gen)` never materializes the full list.  
- `all(gen)` stops at the first `False` — no need to check the rest.

---

## Common Mistakes

### 1. Confusing filter `if` vs ternary `if`

```python
# FILTER — items that don't match are removed entirely
[n for n in range(10) if n % 2 == 0]   # [0, 2, 4, 6, 8]

# TERNARY — every item remains, value changes
["even" if n % 2 == 0 else "odd" for n in range(5)]
# ['even', 'odd', 'even', 'odd', 'even']

# Both — ternary value + filter
[n * 2 if n > 3 else n for n in range(6) if n != 0]
# [1, 2, 3, 8, 10]
```

### 2. Nested comprehension order

```python
# Reading order: outer loop first, then inner loop
[val for row in matrix for val in row]
# NOT: for val in row for row in matrix  ← NameError (row not defined yet)
```

### 3. Building a list when a generator suffices

```python
# Wastes memory — builds full list just to sum it
total = sum([n ** 2 for n in range(1_000_000)])

# Use a generator expression instead
total = sum(n ** 2 for n in range(1_000_000))
```

### 4. Overusing comprehensions

```python
# Hard to read — use a regular loop instead
result = [complex_func(x) for x in data
          if condition1(x) if condition2(x) if condition3(x)]
```

---

## Comprehension vs Loop Cheat Sheet

| Pattern | Comprehension | Loop |
|---|---|---|
| Transform all | `[f(x) for x in it]` | append in for |
| Filter | `[x for x in it if cond]` | if + append |
| Transform + filter | `[f(x) for x in it if cond]` | if + append(f(x)) |
| Ternary value | `[a if c else b for x in it]` | if/else + append |
| Flatten | `[v for r in matrix for v in r]` | nested for |
| Dict build | `{k: v for x in it}` | dict[k] = v |
| Set dedup | `{f(x) for x in it}` | set.add |
| Lazy / one-shot | `(f(x) for x in it)` | — |
