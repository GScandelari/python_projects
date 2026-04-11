# Solutions — Python Fundamentals (Easy)

> Back to the main repository: [README.md](../../../README.md)  
> Exercises file: [`exercises/01-easy.py`](../exercises/01-easy.py)  
> This file: [`solutions/01-easy-solution.py`](./01-easy-solution.py)

---

## What each exercise reinforces

### Exercise 1 — Variable assignment and the five core types

Practising the literal syntax for every primitive type Python offers:

| Type | Literal example | Notes |
|------|----------------|-------|
| `int` | `25` | Whole numbers, no quotes, no decimal point |
| `float` | `1.75` | Decimal point required |
| `str` | `"Alice"` | Single or double quotes — both are valid |
| `bool` | `True` / `False` | Capital first letter; these are keywords |
| `NoneType` | `None` | Represents "no value"; also a keyword |

The key insight is that Python **infers** the type from the literal. You never write `int age = 25` as you would in Java or C.

---

### Exercise 2 — Inspecting types with `type()`

`type(x)` is one of Python's most useful debugging tools. It answers "what kind of thing is this variable holding right now?". Notice that:

- `type(True)` returns `<class 'bool'>`, not `<class 'int'>` — even though booleans are technically a subclass of `int` in CPython.
- The return value of `type()` is itself a type object, not a string. `print()` calls its `__repr__` to display the familiar `<class '...'>` format.

---

### Exercise 3 — The seven arithmetic operators

| Operator | Symbol | Gotcha |
|----------|--------|--------|
| Addition | `+` | Also concatenates strings |
| Subtraction | `-` | |
| Multiplication | `*` | Also repeats strings |
| Division | `/` | **Always** returns `float` |
| Floor division | `//` | Truncates toward −∞, not toward zero |
| Modulo | `%` | Also used for old-style string formatting |
| Exponentiation | `**` | Right-associative: `2**3**2` == `2**9` |

---

### Exercise 4 — String methods and `len()`

Strings expose a rich method API. The critical distinction to remember:

- **Methods** like `.upper()` and `.lower()` are called *on* the string object using dot notation.
- **Functions** like `len()` are standalone and accept the string as an argument.

Both return a **new** value — strings are **immutable**, so the original variable is never changed unless you explicitly reassign it.

---

### Exercise 5 — Augmented assignment operators

`score += 5` is shorthand for `score = score + 5`. This pattern extends to all arithmetic operators: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.

Pay attention to the type change in step 4: `score` starts as an `int` but becomes a `float` the moment you use `/=`, because plain division always returns `float`.

---

## Common beginner mistakes

### 1. Forgetting `str()` when concatenating a number with a string

```python
# WRONG — raises TypeError: can only concatenate str (not "int") to str
age = 25
print("I am " + age + " years old.")

# CORRECT — convert the number first
print("I am " + str(age) + " years old.")

# BETTER — use an f-string instead
print(f"I am {age} years old.")
```

### 2. Confusing `=` (assignment) with `==` (comparison)

```python
x = 10      # assigns the value 10 to x
x == 10     # evaluates to True (a bool); does NOT change x
```

### 3. Using `/` when you want an integer result

```python
print(7 / 2)    # 3.5  — float, always
print(7 // 2)   # 3    — floor division, stays int
```

### 4. Case sensitivity in booleans and None

```python
# WRONG — Python raises NameError
is_valid = true
result = none

# CORRECT — keywords are capitalised
is_valid = True
result = None
```

### 5. Calling `type()` and expecting a string

```python
x = 42
t = type(x)       # t is <class 'int'>, not the string "int"

# To compare types, use isinstance() — it also handles subclasses
if isinstance(x, int):
    print("x is an integer")

# Or compare directly with the type
if type(x) == int:
    print("x is exactly int (not a subclass)")
```

### 6. `print()` vs returning a value

`print()` **displays** something to the terminal and returns `None`. It does **not** produce a value you can store or reuse:

```python
result = print("hello")   # displays "hello"
print(result)             # displays None  <-- probably not what you wanted
```

---

## Key built-ins introduced in these exercises

| Built-in | Purpose |
|----------|---------|
| `print()` | Display output to stdout |
| `type()` | Return the type of an object |
| `len()` | Return the number of items in a sequence |
| `str()` | Convert a value to string |
| `int()` | Convert a value to integer (truncates floats) |
| `float()` | Convert a value to float |
| `bool()` | Convert a value to bool (falsy/truthy rules apply) |

---

## Further reading

- [Python Docs — Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Python Docs — Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Real Python — Variables in Python](https://realpython.com/python-variables/)
- [PEP 8 — Variable naming conventions](https://peps.python.org/pep-0008/#naming-conventions)
