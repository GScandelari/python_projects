# Solutions Guide — 03-testing

---

## Key Concepts by Exercise

### Easy 1-4 — Basic assertions
pytest rewrites `assert` statements at collection time, so failure messages show the actual values without any extra work. `pytest.approx()` uses a relative tolerance of 1e-6 by default — always use it for floats.

### Easy 5 — Stack with fixtures
A `@pytest.fixture` returning a fresh instance is the right approach — each test function gets its own `Stack`, preventing test interdependence. Two fixtures (`empty_stack` vs `stack_with_items`) keep test setup readable.

---

### Medium 1 — Parametrize
`@pytest.mark.parametrize("n, expected", [...])` generates one test case per tuple. pytest names them automatically: `test_fizzbuzz[3-Fizz]`. Use it whenever you'd otherwise copy-paste the same test body with different inputs.

### Medium 2 — Temperature with approx
`pytest.approx(98.6, rel=1e-3)` allows 0.1% relative tolerance. The `rel` parameter is safer than `abs` for values whose magnitude varies.

### Medium 3 — BankAccount fixtures
Two fixtures with different initial states cover complementary scenarios without duplicating setup. Each fixture creates a **new** object — pytest calls the fixture function for every test that requests it (default `function` scope).

### Medium 4 — tmp_path
`tmp_path` is a built-in pytest fixture providing a `pathlib.Path` to a temporary directory that is cleaned up after the test. It's better than writing to a fixed path because tests run in isolation and don't leave files behind.

### Medium 5 — Module scope
`scope="module"` creates the fixture once for the entire file. Use it when fixture setup is expensive (database connection, large data load) and tests only read, never mutate, the fixture state.

---

### Challenge 1 — Mocking SMTP
`Mock()` auto-creates any attribute/method accessed on it, returning another `Mock`. `.return_value` sets what the mock returns when called. `assert_called_once_with(...)` verifies both **that** the method was called and **with what arguments** — the most important assertion in mock-based tests.

### Challenge 2 — Monkeypatch
`monkeypatch.setenv` / `monkeypatch.delenv` modify `os.environ` only for the duration of the test and restore the original state afterward — unlike `os.environ["KEY"] = "val"` which leaks between tests.

### Challenge 3 — Mock HTTP responses
`make_mock_response()` is a helper that builds a consistent mock response object. This avoids repeating `Mock()` configuration in every test and makes the test body express intent, not setup mechanics.

### Challenge 4 — MagicMock
`MagicMock` extends `Mock` to also implement Python magic methods (`__len__`, `__iter__`, etc.). Use it when the code under test accesses dunder methods on the mock.

### Challenge 5 — AsyncMock
`AsyncMock` creates a mock that returns a coroutine when called — necessary for async functions. `await client.get(url)` requires `client.get` to be an async callable; a plain `Mock` would return a `Mock` (not awaitable), causing a `TypeError`.

---

## Common Testing Mistakes

### 1. Testing implementation, not behaviour
```python
# BAD — tests internal detail
assert account._balance == 500

# GOOD — tests public interface
assert account.balance() == 500
```

### 2. Non-isolated tests
```python
# BAD — shared mutable state leaks between tests
account = BankAccount("Alice", 1000)   # module-level

def test_deposit(): account.deposit(500)   # leaves balance at 1500
def test_withdraw(): account.withdraw(200) # assumes balance is still 1000 — wrong!

# GOOD — use fixtures
@pytest.fixture
def account(): return BankAccount("Alice", 1000)
```

### 3. Asserting too little
```python
# BAD — only checks it doesn't crash
def test_send_email(smtp_mock):
    service.send_welcome("a@b.com", "Alice")   # no assertion!

# GOOD — verify the mock was called correctly
smtp_mock.send.assert_called_once_with(to="a@b.com", subject="Welcome!", body=...)
```

### 4. Over-mocking
Mock only what crosses a system boundary (network, file system, clock, random). Don't mock your own classes just to avoid instantiating them — that tests the mock, not your code.
