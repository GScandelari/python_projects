# Solutions Guide — 01-decorators-generators

---

## Key Concepts by Exercise

### Easy 1 — timer decorator
`time.perf_counter()` gives the highest-resolution clock available. Always use it over `time.time()` for measuring code performance. `@functools.wraps(func)` copies `__name__`, `__doc__`, and `__module__` from the original — without it, introspection and debugging break.

### Easy 2 — logger decorator
Building the argument string from `*args` and `**kwargs` requires two comprehensions joined with `+`. `repr(a)` gives a Python-literal representation (strings appear with quotes).

### Easy 3 — countdown generator
`yield` pauses the function and produces a value. The caller controls resumption via `next()` or a `for` loop. The generator maintains its own local state (the `start` variable) between calls.

### Easy 4 — fibonacci generator
`a, b = b, a + b` is a Python tuple swap — both right-hand values are evaluated before assignment, so no temporary variable is needed. The `while True` makes it infinite — callers control when to stop.

### Easy 5 — take()
`enumerate()` gives (index, value) pairs so we can stop after n items without consuming the whole iterable. This works on **any** iterable, including infinite generators — the hallmark of a good utility.

---

### Medium 1 — retry with arguments
Three levels of nesting: `retry(args)` → `decorator(func)` → `wrapper(*args, **kwargs)`. The outermost level closes over `times` and `exceptions`. Catching only the specified `exceptions` tuple is more correct than catching `Exception`.

### Medium 2 — memoize
The cache dict is attached directly to `wrapper` as an attribute (`wrapper.cache = {}`), making it inspectable from outside. Arguments must be hashable to use as dict keys — this is a limitation of this simple version (`functools.lru_cache` handles more edge cases).

### Medium 3 — generator pipeline
Each generator function is a transformation stage. `yield from data` delegates iteration cleanly. Chaining `square(filter_even(read_numbers(...)))` creates a lazy pipeline — nothing runs until the consumer pulls values.

### Medium 4 — running_average with send()
`value = yield current_value` does two things: yields `current_value` to the caller AND waits to receive a value via `send()`. The generator must be **primed** with `next()` before the first `send()` — otherwise it hasn't reached the `yield` yet.

### Medium 5 — stacked decorators
`@exclaim @uppercase def greet` is equivalent to `greet = exclaim(uppercase(greet))`. The inner decorator runs first: uppercase turns the string to uppercase, then exclaim appends "!!!". Reversing them would give `hello, alice!!!` uppercased to `HELLO, ALICE!!!` — same result here, but order matters when transformations interact.

---

### Challenge 1 — RateLimit class-based decorator
A class works as a decorator when it implements `__call__`. `functools.update_wrapper(self, func)` is the class equivalent of `@functools.wraps`. The rate window resets when `period` seconds have elapsed since `_window_start`. Using `time.monotonic()` (never goes backward) is safer than `time.time()` for interval measurement.

### Challenge 2 — deep_flatten with yield from
`yield from deep_flatten(item)` delegates to a recursive call — the outer generator transparently forwards all values from the inner one. This avoids manually iterating the inner generator with `for v in ...: yield v`.

### Challenge 3 — Coroutine pipeline
The `@coroutine` priming decorator automates the mandatory initial `next()` call. `broadcaster` fans out to multiple targets using `send()`. `filter_gt` is a transparent pass-through that only forwards values above the threshold. This pattern avoids threads while enabling concurrent-style data flow.

---

## Common Mistakes

### 1. Forgetting functools.wraps
```python
# Without wraps:
print(decorated.__name__)   # 'wrapper' — breaks logging, debuggers, help()

# Fix: always use @functools.wraps(func) inside the wrapper
```

### 2. Not priming coroutines
```python
gen = my_coroutine()
gen.send(42)   # TypeError: can't send non-None value to a just-started generator

# Fix: next(gen) or gen.send(None) before the first real send()
```

### 3. Returning a generator vs a list
```python
def pipeline(data):
    return (x * 2 for x in data)   # lazy — good for large data

# Callers who iterate twice get an empty result on second pass
result = pipeline([1, 2, 3])
list(result)   # [2, 4, 6]
list(result)   # []  ← already exhausted!

# Fix: return list(...) if multiple iteration is needed
```
