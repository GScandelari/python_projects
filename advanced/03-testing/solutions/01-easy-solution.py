# ============================================================
# advanced/03-testing/solutions/01-easy-solution.py
# Run: pytest solutions/01-easy-solution.py -v
# ============================================================

import pytest

# --- Code under test (copied from exercises/01-easy.py) ---

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def clamp(value, lo, hi):
    return max(lo, min(hi, value))

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if not self._data:
            raise IndexError("peek at empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)


# ============================================================
# Exercise 1 — add()
# ============================================================

def test_add_two_positives():
    assert add(2, 3) == 5

def test_add_with_negative():
    assert add(-1, 4) == 3

def test_add_with_zero():
    assert add(0, 7) == 7

def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)

def test_add_both_negative():
    assert add(-5, -3) == -8


# ============================================================
# Exercise 2 — divide()
# ============================================================

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_float_result():
    assert divide(7, 2) == pytest.approx(3.5)

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_divide_by_zero_message():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(5, 0)

def test_divide_negative():
    assert divide(-6, 2) == -3.0


# ============================================================
# Exercise 3 — is_palindrome()
# ============================================================

def test_palindrome_simple():
    assert is_palindrome("racecar") is True

def test_not_palindrome():
    assert is_palindrome("hello") is False

def test_palindrome_case_insensitive():
    assert is_palindrome("Level") is True

def test_palindrome_with_spaces():
    # "amanaplanacanalpanama" → palindrome
    assert is_palindrome("A man a plan a canal Panama") is True

def test_palindrome_single_char():
    assert is_palindrome("a") is True

def test_not_palindrome_python():
    assert is_palindrome("Python") is False


# ============================================================
# Exercise 4 — clamp()
# ============================================================

def test_clamp_within_range():
    assert clamp(5, 0, 10) == 5

def test_clamp_below_lo():
    assert clamp(-5, 0, 10) == 0

def test_clamp_above_hi():
    assert clamp(15, 0, 10) == 10

def test_clamp_at_lo_boundary():
    assert clamp(0, 0, 10) == 0

def test_clamp_at_hi_boundary():
    assert clamp(10, 0, 10) == 10


# ============================================================
# Exercise 5 — Stack
# ============================================================

@pytest.fixture
def empty_stack():
    return Stack()

@pytest.fixture
def stack_with_items():
    s = Stack()
    for item in [1, 2, 3]:
        s.push(item)
    return s

def test_new_stack_is_empty(empty_stack):
    assert empty_stack.is_empty() is True

def test_push_makes_non_empty(empty_stack):
    empty_stack.push(42)
    assert empty_stack.is_empty() is False

def test_peek_returns_top(stack_with_items):
    assert stack_with_items.peek() == 3

def test_pop_returns_and_removes(stack_with_items):
    assert stack_with_items.pop() == 3
    assert stack_with_items.size() == 2

def test_pop_empty_raises(empty_stack):
    with pytest.raises(IndexError):
        empty_stack.pop()

def test_peek_empty_raises(empty_stack):
    with pytest.raises(IndexError):
        empty_stack.peek()

def test_size_after_pushes(empty_stack):
    for i in range(5):
        empty_stack.push(i)
    assert empty_stack.size() == 5

def test_stack_lifo_order(empty_stack):
    for i in [1, 2, 3]:
        empty_stack.push(i)
    assert empty_stack.pop() == 3
    assert empty_stack.pop() == 2
    assert empty_stack.pop() == 1
