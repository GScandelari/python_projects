# myutils/__init__.py
# Expose a clean public API for the myutils package.

from .strings import reverse, is_palindrome, word_count
from .numbers import clamp, is_prime, factors

__all__ = ["reverse", "is_palindrome", "word_count", "clamp", "is_prime", "factors"]
