# Easy Exercises — Solution Notes

## What each exercise reinforces

| # | Exercise | Core concept reinforced |
|---|----------|------------------------|
| 1 | Positive / negative / zero check | `if / elif / else` chain — mutually exclusive branches evaluated top-to-bottom |
| 2 | Print 1–10 with `for` + `range()` | Basic `for` loop; understanding that `range(start, stop)` excludes `stop` |
| 3 | Even numbers 1–20 with step | Using the **step** argument of `range()` to skip values instead of filtering inside the loop |
| 4 | Countdown with `while` | `while` loop lifecycle: initialise → test condition → body → update → repeat |
| 5 | Characters of "Python" | Strings are iterable sequences; `for` works directly on them without indexing |

### `range()` syntax variants

| Call | Generates | Notes |
|------|-----------|-------|
| `range(stop)` | `0, 1, …, stop-1` | Start defaults to `0` |
| `range(start, stop)` | `start, start+1, …, stop-1` | `stop` is **excluded** |
| `range(start, stop, step)` | Every `step`-th value from `start` up to (not including) `stop` | Step can be negative for countdowns |
| `range(5, 0, -1)` | `5, 4, 3, 2, 1` | Negative step — `stop` is still excluded |

---

## Common beginner mistakes

### 1. Using `=` instead of `==` in conditions

`=` is the **assignment** operator; `==` is the **equality comparison** operator.
Using `=` inside an `if` condition is a `SyntaxError` in Python (unlike some other languages).

```python
# Wrong
if number = 0:          # SyntaxError: invalid syntax
    print("zero")

# Correct
if number == 0:
    print("zero")
```

---

### 2. Off-by-one errors with `range()`

`range(stop)` stops **before** `stop`. Forgetting this produces loops that run
one iteration too few (or too many when the intention is reversed).

```python
# Wrong — prints 1 through 9, misses 10
for n in range(1, 10):
    print(n)

# Correct — prints 1 through 10
for n in range(1, 11):
    print(n)
```

---

### 3. Forgetting `break` and creating infinite loops

A `while` loop whose condition never becomes `False` (and has no `break`) runs
forever, hanging the program.

```python
# Wrong — counter is never decremented, loop never ends
counter = 5
while counter > 0:
    print(counter)
    # forgot: counter -= 1

# Correct
counter = 5
while counter > 0:
    print(counter)
    counter -= 1
```

Similarly, always ensure a `break` is reachable when you use `while True`:

```python
# Wrong — break condition is never True
while True:
    user_input = input("Enter 'quit' to stop: ")
    if user_input == "exit":   # typo: should be "quit"
        break

# Correct
while True:
    user_input = input("Enter 'quit' to stop: ")
    if user_input == "quit":
        break
```

---

### 4. Indentation errors in nested `if` / loops

Python uses indentation to define blocks. Misaligned lines either raise an
`IndentationError` or silently run code in the wrong scope.

```python
# Wrong — the print is outside the if block (no indentation)
for n in range(1, 6):
    if n % 2 == 0:
    print(n)             # IndentationError

# Wrong — the inner print runs every iteration, not just when n > 3
for n in range(1, 6):
    if n > 3:
        print("big")
        print("done")    # looks like it belongs to the if, but if
                         # indentation is one level less it runs always

# Correct
for n in range(1, 6):
    if n % 2 == 0:
        print(n)         # indented one level inside the if
```

---

### 5. Modifying the loop variable inside a `for` loop expecting it to change the iteration

Reassigning the loop variable inside a `for` loop body has no effect on which
values the loop visits next. The iterator controls the sequence; the variable
is simply overwritten at the start of each iteration.

```python
# Wrong — expects the loop to skip ahead, but it does not
for i in range(10):
    print(i)
    if i == 3:
        i = 7   # This does NOT make the next iteration start at 8

# Output is still: 0 1 2 3 4 5 6 7 8 9

# Correct approach — use continue or adjust the range / use while
for i in range(10):
    if i == 4 or i == 5 or i == 6:
        continue          # skip these values
    print(i)
```

---

### 6. Missing the `else` clause when needed

Beginners sometimes handle the "happy path" but forget to cover cases where
none of the `if`/`elif` conditions are True, leading to silent failures where
nothing is printed or done.

```python
# Wrong — if temperature is exactly 20, nothing happens
temperature = 20
if temperature > 25:
    print("It's hot.")
elif temperature < 15:
    print("It's cold.")
# No else — temperature == 20 produces no output at all

# Correct
temperature = 20
if temperature > 25:
    print("It's hot.")
elif temperature < 15:
    print("It's cold.")
else:
    print("It's comfortable.")   # catches everything not handled above
```
