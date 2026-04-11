# Solutions Guide — 02-modules-packages

---

## What Each Exercise Reinforces

### Easy 1 — math
**Concept:** Accessing module constants and functions via dot notation.  
`math.pow(2, 10)` always returns a float (`1024.0`). The `**` operator returns an int when both operands are int (`2**10 = 1024`). Know the difference.

### Easy 2 — random
**Concept:** Reproducibility with `seed()`, difference between `randint`, `sample`, and `shuffle`.  
`random.sample(population, k)` never repeats; `randint(a,b)` is inclusive on **both** ends (unlike `range`).

### Easy 3 — datetime
**Concept:** Date arithmetic with `timedelta`, formatting with `strftime`.  
Subtracting two `date` objects returns a `timedelta`. Access `.days` to get an integer.

### Easy 4 — os
**Concept:** OS-agnostic path building with `os.path.join`.  
Never concatenate paths with string `+` — use `os.path.join` so your code works on Windows and Unix.

### Easy 5 — json
**Concept:** `dumps`/`loads` (string) vs `dump`/`load` (file).  
Common mistake: `json.dumps` with no `indent` produces a compact single-line string. Add `indent=2` for readability.

### Medium 1 — Dice Roller
**Concept:** Using `random` for simulation + dict for frequency tracking.  
This is the **accumulator + dict** pattern from data-structures applied to a statistical simulation.

### Medium 2 — Birthday Countdown
**Concept:** `datetime.strptime` for parsing, `timedelta` for arithmetic.  
"Next birthday" requires checking if the birthday this year has already passed — if so, use next year's date.

### Challenge — myutils package
**Concept:** Package structure, `__init__.py` as public API, `__all__`, relative imports.  
The `__init__.py` using `from .strings import ...` (note the dot) is a **relative import** — it imports from within the same package. This is what makes packages self-contained.

---

## Import Styles Compared

```python
import math                  # math.sqrt(9)    — explicit, safe
import math as m             # m.sqrt(9)       — shorter alias
from math import sqrt        # sqrt(9)         — concise, possible clash
from math import sqrt, pi    # sqrt(9), pi     — selective import
from math import *           # sqrt(9), pi     — avoid! pollutes namespace
```

## Common Beginner Mistakes

### 1. Circular imports
```python
# a.py imports b.py, and b.py imports a.py → ImportError
# Fix: restructure so imports flow in one direction only
```

### 2. Missing `__name__` guard
```python
# utils.py — bad
result = expensive_function()   # runs on import!

# utils.py — good
def expensive_function(): ...

if __name__ == "__main__":
    result = expensive_function()
```

### 3. Relative import outside a package
```python
# Running a file inside a package directly breaks relative imports
# Fix: run from the package root with: python -m mypackage.module
```

### 4. Shadowing a built-in module name
```python
# Don't name your files math.py, random.py, os.py, etc.
# It will shadow the standard library module!
```

### 5. `json.dumps` vs `json.dump`
```python
json_str = json.dumps(data)        # → string
json.dump(data, file_object)       # → writes to file (no 's')
data = json.loads(json_str)        # ← from string
data = json.load(file_object)      # ← from file (no 's')
```

### 6. Mutable `__all__` confusion
```python
# __all__ controls `from module import *` only
# It does NOT prevent direct imports:
from myutils.numbers import factors   # always works, ignores __all__
```
