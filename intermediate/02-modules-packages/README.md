# Modules and Packages

A **module** is any `.py` file. A **package** is a folder of modules with an `__init__.py`. They let you split code across files, reuse logic across projects, and tap into Python's vast standard library.

## Table of Contents

- [Importing Modules](#1-importing-modules)
- [Built-in Modules](#2-built-in-modules)
- [Creating Your Own Module](#3-creating-your-own-module)
- [Packages](#4-packages)
- [The `__name__` Guard](#5-the-__name__-guard)
- [Exploring with `dir()` and `help()`](#6-exploring-with-dir-and-help)
- [Quick Reference](#quick-reference)
- [What's Next](#whats-next)

---

## 1. Importing Modules

```python
import math                        # import entire module
import math as m                   # import with alias
from math import sqrt, pi          # import specific names
from math import *                 # import everything (avoid — pollutes namespace)
```

| Style | Usage | Pros / Cons |
|---|---|---|
| `import math` | `math.sqrt(9)` | Explicit, no collisions |
| `import math as m` | `m.sqrt(9)` | Shorter alias |
| `from math import sqrt` | `sqrt(9)` | Concise, but name could clash |
| `from math import *` | `sqrt(9)` | Avoid — unclear where names come from |

---

## 2. Built-in Modules

Python ships with over 200 modules. Here are the most useful for everyday work:

### `math`

```python
import math

print(math.pi)            # 3.141592653589793
print(math.e)             # 2.718281828459045
print(math.sqrt(144))     # 12.0
print(math.ceil(4.2))     # 5
print(math.floor(4.8))    # 4
print(math.log(100, 10))  # 2.0
print(math.factorial(6))  # 720
print(math.pow(2, 10))    # 1024.0
```

### `random`

```python
import random

print(random.randint(1, 10))           # random int 1–10 (inclusive)
print(random.random())                 # float 0.0 ≤ x < 1.0
print(random.choice(["a", "b", "c"])) # random element
print(random.sample(range(100), 5))   # 5 unique random ints

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)                # shuffle in-place
print(numbers)

random.seed(42)                        # reproducible results
print(random.randint(1, 100))          # always 53 with seed 42
```

### `datetime`

```python
from datetime import datetime, date, timedelta

today = date.today()
now = datetime.now()

print(today)                              # 2026-04-11
print(now.strftime("%d/%m/%Y %H:%M"))     # 11/04/2026 14:30
print(datetime.strptime("25/12/2025", "%d/%m/%Y"))

birthday = date(1990, 7, 15)
age = (today - birthday).days // 365
print(f"Age: {age} years")

next_week = today + timedelta(days=7)
print(next_week)
```

### `os` and `os.path`

```python
import os

print(os.getcwd())                        # current working directory
print(os.listdir("."))                    # list files/folders
print(os.path.join("folder", "file.txt"))# folder/file.txt (OS-aware)
print(os.path.exists("README.md"))        # True / False
print(os.path.basename("/a/b/file.txt"))  # file.txt
print(os.path.dirname("/a/b/file.txt"))   # /a/b
name, ext = os.path.splitext("script.py")# ('script', '.py')
```

### `json`

```python
import json

# Python dict → JSON string
data = {"name": "Alice", "age": 28, "scores": [90, 85, 92]}
json_str = json.dumps(data, indent=2)
print(json_str)

# JSON string → Python dict
parsed = json.loads(json_str)
print(parsed["name"])   # Alice

# Write to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read from file
with open("data.json") as f:
    loaded = json.load(f)
```

### `sys`

```python
import sys

print(sys.version)           # Python version string
print(sys.platform)          # 'win32', 'linux', 'darwin'
print(sys.argv)              # command-line arguments list
sys.exit(0)                  # exit the script with code 0
```

---

## 3. Creating Your Own Module

Any `.py` file is a module. Put reusable functions there and import them anywhere.

**`mathutils.py`** (your module):
```python
PI = 3.14159

def circle_area(radius):
    """Return the area of a circle."""
    return PI * radius ** 2

def is_prime(n):
    """Return True if n is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

**`main.py`** (using your module):
```python
import mathutils

print(mathutils.circle_area(5))   # 78.53975
print(mathutils.is_prime(17))     # True

from mathutils import is_prime
print(is_prime(4))                # False
```

### `__all__` — control what `from module import *` exposes

```python
# mathutils.py
__all__ = ["circle_area", "is_prime"]   # PI is hidden from import *
```

---

## 4. Packages

A **package** is a directory that contains an `__init__.py` file (can be empty):

```
mypackage/
├── __init__.py        ← marks it as a package
├── strings.py
└── numbers.py
```

```python
# mypackage/strings.py
def reverse(text):
    return text[::-1]

# mypackage/numbers.py
def clamp(value, low, high):
    return max(low, min(high, value))
```

```python
# main.py — importing from your package
from mypackage.strings import reverse
from mypackage import numbers

print(reverse("Python"))         # nohtyP
print(numbers.clamp(150, 0, 100))  # 100
```

**`__init__.py`** can expose a clean public API:
```python
# mypackage/__init__.py
from .strings import reverse
from .numbers import clamp

__all__ = ["reverse", "clamp"]
```

Now users can do:
```python
from mypackage import reverse, clamp
```

---

## 5. The `__name__` Guard

Every module has a `__name__` attribute. When a file is **run directly**, `__name__` is `"__main__"`. When it is **imported**, `__name__` is the module name.

```python
# mathutils.py
def is_prime(n):
    ...

if __name__ == "__main__":
    # This block ONLY runs when you run: python mathutils.py
    # It is SKIPPED when someone does: import mathutils
    print(is_prime(17))   # quick sanity test
```

**Always use this guard** to separate reusable code from script code.

---

## 6. Exploring with `dir()` and `help()`

```python
import math

print(dir(math))          # list all names in the module
print(help(math.sqrt))    # full docstring for sqrt
print(math.__file__)      # where the module file lives
print(math.__doc__[:80])  # module docstring (first 80 chars)
```

---

## Quick Reference

```python
# Import styles
import module
import module as alias
from module import name
from module import name1, name2

# Useful built-ins
import math        # math.sqrt, math.pi, math.ceil, math.factorial
import random      # random.randint, random.choice, random.shuffle
import os          # os.getcwd, os.listdir, os.path.join
import json        # json.dumps, json.loads, json.dump, json.load
import sys         # sys.argv, sys.exit, sys.platform
from datetime import datetime, date, timedelta

# __name__ guard
if __name__ == "__main__":
    main()

# Package structure
mypackage/
├── __init__.py
└── module.py
```

---

## What's Next

Try the exercises in [`exercises/`](./exercises/).

Next concept: [`03-file-handling`](../03-file-handling/)
