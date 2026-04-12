# ============================================================
# advanced/01-decorators-generators/solutions/03-challenge-solution.py
# ============================================================

import functools
import time

# ----------------------------------------------------------
# Exercise 1 — RateLimit class-based decorator
# ----------------------------------------------------------
class RateLimit:
    def __init__(self, calls, period):
        self.calls  = calls
        self.period = period

    def __call__(self, func):
        functools.update_wrapper(self, func)
        self._func   = func
        self._count  = 0
        self._window_start = None

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.monotonic()
            if self._window_start is None or now - self._window_start >= self.period:
                self._window_start = now
                self._count = 0
            if self._count >= self.calls:
                raise RuntimeError(
                    f"Rate limit exceeded: max {self.calls} calls per {self.period}s"
                )
            self._count += 1
            return func(*args, **kwargs)
        return wrapper

@RateLimit(calls=3, period=5)
def api_call(endpoint):
    return f"Data from {endpoint}"

print("--- RateLimit demo ---")
for i in range(3):
    print(api_call("/users"))

try:
    api_call("/users")
except RuntimeError as e:
    print(f"RuntimeError: {e}")


# ----------------------------------------------------------
# Exercise 2 — deep_flatten with yield from
# ----------------------------------------------------------
def deep_flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from deep_flatten(item)
        else:
            yield item

print("\n--- deep_flatten demo ---")
print(list(deep_flatten([1, [2, [3, [4, 5]], 6], 7])))   # [1,2,3,4,5,6,7]
print(list(deep_flatten([[[1]], [[2, 3]], 4])))           # [1,2,3,4]


# ----------------------------------------------------------
# Exercise 3 — Coroutine pipeline with send()
# ----------------------------------------------------------
def coroutine(func):
    """Decorator that primes a coroutine automatically."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper

@coroutine
def printer(prefix):
    while True:
        value = yield
        print(f"{prefix}: {value}")

@coroutine
def filter_gt(threshold, target):
    while True:
        value = yield
        if value > threshold:
            target.send(value)

@coroutine
def broadcaster(targets):
    while True:
        value = yield
        for t in targets:
            t.send(value)

print("\n--- coroutine pipeline demo ---")

all_printer  = printer("ALL")
high_printer = printer("HIGH")
high_filter  = filter_gt(50, high_printer)
broadcast    = broadcaster([all_printer, high_filter])

for value in [10, 60, 30, 80, 45]:
    broadcast.send(value)
# ALL: 10 / ALL: 60 / HIGH: 60 / ALL: 30 / ALL: 80 / HIGH: 80 / ALL: 45
