# Python Basics — Interview Questions

## Types and Mutability

**Q: What is the difference between mutable and immutable types?**

Immutable objects cannot be changed after creation. Mutating them creates a new object.

| Immutable | Mutable |
|---|---|
| `int`, `float`, `complex` | `list`, `dict`, `set` |
| `str`, `bytes` | `bytearray` |
| `tuple`, `frozenset` | custom objects (usually) |

```python
# Immutable — reassignment creates a new object
a = 'hello'
id_before = id(a)
a += ' world'
id(a) == id_before   # False — new object

# Mutable — modified in place
lst = [1, 2, 3]
id_before = id(lst)
lst.append(4)
id(lst) == id_before   # True — same object
```

**Why it matters:** Immutable objects are hashable (can be dict keys / set members). Mutable default arguments cause a classic bug:

```python
# BUG — default list is shared across all calls
def append_to(item, lst=[]):
    lst.append(item)
    return lst

# FIX
def append_to(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

---

**Q: What is the difference between `==` and `is`?**

- `==` compares **value** (calls `__eq__`)
- `is` compares **identity** (same object in memory)

```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b   # True  — same values
a is b   # False — different objects

# is used correctly:
x is None    # check for None (not x == None)
x is True    # check for singleton True
```

---

**Q: What is Python's GIL?**

The **Global Interpreter Lock** ensures only one thread executes Python bytecode at a time, even on multi-core machines.

- Released during I/O operations → `threading` still helps for I/O-bound tasks
- Never released for CPU work → use `multiprocessing` for CPU-bound parallelism
- Not an issue for `asyncio` (single-threaded by design)

---

## Scoping (LEGB)

**Q: Explain Python's scoping rules.**

Python resolves names in this order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in.

```python
x = 'global'

def outer():
    x = 'enclosing'

    def inner():
        x = 'local'
        print(x)   # 'local'
    inner()
    print(x)       # 'enclosing'

outer()
print(x)           # 'global'

# global / nonlocal — modify outer scope
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
```

---

## Memory and References

**Q: How does Python manage memory?**

- **Reference counting** — each object tracks how many references point to it; freed when count hits 0.
- **Cycle collector** — handles circular references that reference counting misses.
- **Memory pools** (`pymalloc`) — small objects (< 512 bytes) are allocated from pre-allocated pools for speed.

```python
import sys
x = [1, 2, 3]
sys.getrefcount(x)   # always at least 1 (the temporary arg adds 1 too)
```

**Q: What is a shallow copy vs deep copy?**

```python
import copy

original = [[1, 2], [3, 4]]

shallow = original.copy()        # or list(original) / original[:]
deep    = copy.deepcopy(original)

original[0].append(99)
print(shallow[0])   # [1, 2, 99] — inner list shared
print(deep[0])      # [1, 2]     — independent copy
```

---

## Iterators and Generators

**Q: What is the difference between an iterable and an iterator?**

- **Iterable**: has `__iter__()` returning an iterator (lists, tuples, dicts, generators).
- **Iterator**: has both `__iter__()` and `__next__()`; remembers position; raises `StopIteration` when exhausted.

```python
lst = [1, 2, 3]         # iterable
it  = iter(lst)         # iterator
next(it)                # 1
next(it)                # 2
```

**Q: What are the advantages of generators?**

1. **Memory efficient** — produce values one at a time, never build the full list.
2. **Lazy evaluation** — compute only what is consumed.
3. **Infinite sequences** — can represent streams with no end.

```python
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fib()
[next(gen) for _ in range(8)]   # [0, 1, 1, 2, 3, 5, 8, 13]
```

---

## Decorators

**Q: What is a decorator? How do you preserve metadata?**

A decorator is a callable that takes a function and returns a replacement function, adding behaviour before/after the original.

```python
import functools

def timer(func):
    @functools.wraps(func)   # copies __name__, __doc__, __module__
    def wrapper(*args, **kwargs):
        import time
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        print(f'{func.__name__} took {time.perf_counter()-start:.4f}s')
        return result
    return wrapper

@timer
def slow():
    """Sleeps briefly."""
    import time; time.sleep(0.1)

slow.__name__   # 'slow' (not 'wrapper', thanks to @wraps)
slow.__doc__    # 'Sleeps briefly.'
```

---

## Common Gotchas

| Gotcha | Explanation |
|---|---|
| Mutable default argument | Default evaluated once at definition time |
| Late-binding closure | Loop variable captured by reference, not value |
| `x += 1` in nested scope | Creates local, shadows outer — use `nonlocal` |
| `==` vs `is` for None | Always use `is None`, never `== None` |
| Modifying a list while iterating | Iterate over a copy: `for x in lst[:]` |
| `dict.keys()` returns a view | Convert to `list()` if you need a snapshot |

```python
# Late-binding closure — classic bug
funcs = [lambda: i for i in range(3)]
[f() for f in funcs]   # [2, 2, 2] — all see i=2

# Fix — capture at definition time
funcs = [lambda i=i: i for i in range(3)]
[f() for f in funcs]   # [0, 1, 2]
```
