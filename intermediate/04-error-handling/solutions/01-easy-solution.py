# ============================================================
# intermediate/04-error-handling/solutions/01-easy-solution.py
# ============================================================
import os


# ----------------------------------------------------------
# Exercise 1 — safe_divide
# ----------------------------------------------------------
# APPROACH: Catch specific exceptions in order. TypeError can
# happen when Python tries to do the division itself (e.g. "a" / 2).

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        return None
    except TypeError:
        print("Error: invalid types")
        return None

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # None
print(safe_divide("a", 2))   # None


# ----------------------------------------------------------
# Exercise 2 — get_positive_int
# ----------------------------------------------------------
# APPROACH: while True loop + try/except. The loop only exits
# via return, so invalid input just re-prompts.

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("must be positive")
            return value
        except ValueError:
            print("Please enter a positive whole number.")

# Uncomment to test interactively:
# age = get_positive_int("Enter your age: ")
# print(f"Age: {age}")


# ----------------------------------------------------------
# Exercise 3 — get_grade
# ----------------------------------------------------------
# APPROACH: Normalize with .title() first, then access the dict.
# Catching KeyError is cleaner than checking 'if key in dict' first.

def get_grade(students, name):
    try:
        return students[name.title()]
    except KeyError:
        return "Student not found"

students = {"Alice": 92, "Bob": 78, "Carol": 85}
print(get_grade(students, "alice"))   # 92
print(get_grade(students, "Dave"))    # Student not found
print(get_grade(students, "BOB"))     # 78


# ----------------------------------------------------------
# Exercise 4 — read_first_line (try/except/else/finally)
# ----------------------------------------------------------
# APPROACH: else runs only on success — perfect for the
# "return the value" logic. finally always runs — good for logging.

def read_first_line(filepath):
    try:
        f = open(filepath, encoding="utf-8")
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except PermissionError:
        print(f"Cannot read: {filepath}")
        return None
    else:
        first_line = f.readline().strip()
        f.close()
        print("Read successfully.")
        return first_line
    finally:
        print(f"Attempted to read: {filepath}")

THIS_FILE = __file__
MISSING_FILE = os.path.join(os.path.dirname(__file__), "missing.txt")

print(read_first_line(THIS_FILE))
print(read_first_line(MISSING_FILE))


# ----------------------------------------------------------
# Exercise 5 — parse_number
# ----------------------------------------------------------
# APPROACH: Catch both exception types with a tuple — same
# default behavior for both, so one handler is cleaner.

def parse_number(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0

print(parse_number("3.14"))   # 3.14
print(parse_number("hello"))  # 0.0
print(parse_number(None))     # 0.0
print(parse_number(42))       # 42.0
