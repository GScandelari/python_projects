# solutions/myutils/strings.py

def reverse(text):
    """Return the reversed version of text."""
    return text[::-1]


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards (ignore case and spaces)."""
    clean = text.lower().replace(" ", "")
    return clean == clean[::-1]


def word_count(text):
    """Return a dict mapping each word (lowercase) to its frequency in text."""
    freq = {}
    for word in text.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq
