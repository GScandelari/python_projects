# solutions/myutils/numbers.py

def clamp(value, low, high):
    """Return value constrained to the range [low, high]."""
    return max(low, min(high, value))


def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factors(n):
    """Return a sorted list of all positive factors of n."""
    return [i for i in range(1, n + 1) if n % i == 0]
