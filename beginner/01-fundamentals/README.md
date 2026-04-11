# 01 — Python Fundamentals

Welcome! This is the starting point of your Python journey. By the end of this section you will understand how Python stores data, how to manipulate it, and how to talk to the user through the terminal.

No prior programming experience is required.

---

## Table of Contents

1. [Variables](#1-variables)
2. [Data Types](#2-data-types)
3. [Basic Operators](#3-basic-operators)
4. [Type Conversion](#4-type-conversion)
5. [Input and Output](#5-input-and-output)
6. [What's Next](#whats-next)

---

## 1. Variables

A **variable** is a named container that holds a value. Think of it as a labelled box — you put something inside it and refer to it later by the label.

### 1.1 Assignment

Use the `=` sign to assign a value to a variable.

```python
name = "Alice"
age = 25
height = 1.72
is_student = True
```

Python figures out the type of the value automatically — you do not need to declare it in advance.

### 1.2 Naming Rules

| Rule | Good example | Bad example |
|---|---|---|
| Start with a letter or underscore | `score`, `_count` | `1score` |
| Only letters, digits, and underscores | `first_name`, `x2` | `first-name`, `first name` |
| Case-sensitive | `age` and `Age` are different | — |
| Cannot be a Python keyword | `total` | `for`, `if`, `class` |

Python convention (PEP 8) is to use **snake_case** for variable names: all lowercase with underscores between words.

```python
# Good names
user_name = "Bob"
total_score = 100
max_retries = 3

# Avoid these (they work but are hard to read)
UN = "Bob"
TotalScore = 100
```

### 1.3 Multiple Assignment

You can assign values to several variables on a single line.

```python
# Assign the same value to multiple variables
x = y = z = 0

# Assign different values at once (tuple unpacking)
first, second, third = "gold", "silver", "bronze"

print(first)   # gold
print(second)  # silver
print(third)   # bronze
```

You can also swap two variables without a temporary helper:

```python
a = 10
b = 20
a, b = b, a
print(a, b)  # 20 10
```

---

## 2. Data Types

Every value in Python has a **type** that determines what you can do with it.

### 2.1 The Five Core Types

| Type | Python name | Example values |
|---|---|---|
| Integer | `int` | `0`, `42`, `-7` |
| Floating-point | `float` | `3.14`, `-0.5`, `1.0` |
| String | `str` | `"hello"`, `'world'` |
| Boolean | `bool` | `True`, `False` |
| Nothing / null | `NoneType` | `None` |

### 2.2 int — Whole Numbers

```python
apples = 5
temperature = -3
big_number = 1_000_000   # underscores are allowed for readability

print(apples)       # 5
print(big_number)   # 1000000
```

### 2.3 float — Decimal Numbers

```python
price = 9.99
pi = 3.14159
negative = -0.001

print(price)     # 9.99
print(pi)        # 3.14159
```

> **Heads up:** Floating-point arithmetic can produce tiny rounding errors.
> `0.1 + 0.2` gives `0.30000000000000004` in Python (and most languages).
> This is normal computer behaviour — not a bug.

### 2.4 str — Text

Strings are sequences of characters. You can use single quotes, double quotes, or triple quotes (for multi-line text).

```python
greeting = "Hello, world!"
city = 'London'
paragraph = """This is
a multi-line
string."""

print(greeting)
print(city)
print(paragraph)
```

Useful string operations:

```python
word = "python"

print(len(word))          # 6  — number of characters
print(word.upper())       # PYTHON
print(word.capitalize())  # Python
print(word[0])            # p  — first character (index 0)
print(word[-1])           # n  — last character
```

### 2.5 bool — True or False

Booleans represent logical values. They are the result of comparisons and conditions.

```python
is_sunny = True
is_raining = False

print(is_sunny)    # True
print(is_raining)  # False

# Booleans are produced by comparisons
print(5 > 3)    # True
print(10 == 9)  # False
```

### 2.6 NoneType — The Absence of a Value

`None` is Python's way of saying "nothing here". It is often used as a default or placeholder.

```python
result = None
print(result)          # None
print(type(result))    # <class 'NoneType'>
```

### 2.7 Checking the Type of a Value

Use the built-in `type()` function to inspect a value's type at any time.

```python
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>
print(type(None))      # <class 'NoneType'>
```

---

## 3. Basic Operators

### 3.1 Arithmetic Operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `3 + 2` | `5` |
| `-` | Subtraction | `10 - 4` | `6` |
| `*` | Multiplication | `6 * 7` | `42` |
| `/` | Division (always float) | `9 / 2` | `4.5` |
| `//` | Floor division (whole number) | `9 // 2` | `4` |
| `%` | Modulo (remainder) | `9 % 2` | `1` |
| `**` | Exponentiation | `2 ** 8` | `256` |

```python
a = 17
b = 5

print(a + b)   # 22
print(a - b)   # 12
print(a * b)   # 85
print(a / b)   # 3.4
print(a // b)  # 3
print(a % b)   # 2
print(a ** b)  # 1419857
```

The `%` operator is handy for checking whether a number is even or odd:

```python
number = 14
print(number % 2 == 0)  # True — it is even
```

### 3.2 Comparison Operators

Comparison operators always return a `bool` (`True` or `False`).

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `7 > 4` | `True` |
| `<` | Less than | `2 < 1` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `3 <= 2` | `False` |

```python
score = 85

print(score >= 90)   # False — not an A
print(score >= 70)   # True  — passing grade
print(score == 100)  # False — not perfect
print(score != 0)    # True  — not zero
```

> **Common mistake:** Do not confuse `=` (assignment) with `==` (comparison).
> `x = 5` stores the value. `x == 5` asks "is x equal to 5?".

### 3.3 Logical Operators

Logical operators combine boolean expressions.

| Operator | Meaning | Result is `True` when… |
|---|---|---|
| `and` | Both must be true | both sides are `True` |
| `or` | At least one must be true | at least one side is `True` |
| `not` | Reverses the boolean | the value is `False` |

```python
age = 20
has_ticket = True

# and — both conditions must hold
can_enter = age >= 18 and has_ticket
print(can_enter)  # True

# or — at least one condition must hold
is_weekend = False
is_holiday = True
day_off = is_weekend or is_holiday
print(day_off)  # True

# not — flips True to False and vice versa
is_closed = False
print(not is_closed)  # True
```

### 3.4 Assignment Operators

These are shortcuts that combine an arithmetic operation with assignment.

| Operator | Equivalent to | Example |
|---|---|---|
| `+=` | `x = x + n` | `x += 5` |
| `-=` | `x = x - n` | `x -= 3` |
| `*=` | `x = x * n` | `x *= 2` |
| `/=` | `x = x / n` | `x /= 4` |
| `//=` | `x = x // n` | `x //= 2` |
| `%=` | `x = x % n` | `x %= 3` |
| `**=` | `x = x ** n` | `x **= 2` |

```python
lives = 3
lives -= 1
print(lives)  # 2

score = 100
score *= 2
print(score)  # 200
```

---

## 4. Type Conversion

Sometimes you need to convert a value from one type to another. Python provides built-in functions for this.

| Function | Converts to | Example | Result |
|---|---|---|---|
| `int()` | Integer | `int("42")` | `42` |
| `float()` | Float | `float(7)` | `7.0` |
| `str()` | String | `str(3.14)` | `"3.14"` |
| `bool()` | Boolean | `bool(0)` | `False` |

```python
# String to number
text_number = "100"
real_number = int(text_number)
print(real_number + 5)    # 105  (not "1005")

# Number to string
price = 9.99
label = "Price: " + str(price)
print(label)              # Price: 9.99

# Float to int (truncates — does NOT round)
pi = 3.99
print(int(pi))            # 3
```

### 4.1 Truthy and Falsy Values

When converting to `bool`, most values are `True`. The exceptions (falsy values) are:

```python
print(bool(0))       # False
print(bool(0.0))     # False
print(bool(""))      # False — empty string
print(bool(None))    # False

print(bool(1))       # True
print(bool(-5))      # True
print(bool("hi"))    # True
print(bool(" "))     # True — space counts as a character
```

### 4.2 What Happens When Conversion Fails

If you try to convert something that does not make sense, Python raises a `ValueError`:

```python
int("hello")   # ValueError: invalid literal for int() with base 10: 'hello'
float("abc")   # ValueError: could not convert string to float: 'abc'
```

Always make sure the value can actually be converted before calling these functions on user input.

---

## 5. Input and Output

### 5.1 Printing with print()

`print()` displays values in the terminal.

```python
print("Hello, world!")
print(42)
print(3.14, True, None)   # multiple values separated by spaces
```

You can customise the separator and the ending character:

```python
print("one", "two", "three", sep="-")    # one-two-three
print("Loading", end="...")               # Loading... (no newline)
print("done")                             # done
```

### 5.2 Getting Input with input()

`input()` pauses the program and waits for the user to type something and press Enter. It **always returns a string**.

```python
name = input("What is your name? ")
print("Hello,", name)
```

Because `input()` always returns a string, you must convert it if you need a number:

```python
age_text = input("How old are you? ")
age = int(age_text)                        # convert to int
print("In 10 years you will be", age + 10)
```

You can also do this on one line:

```python
age = int(input("How old are you? "))
```

### 5.3 Formatting Output with f-strings

An **f-string** (formatted string literal) lets you embed variables directly inside a string by prefixing it with `f` and wrapping expressions in `{}`.

```python
name = "Alice"
age = 25

# Old way (harder to read)
print("My name is " + name + " and I am " + str(age) + " years old.")

# f-string (clean and easy)
print(f"My name is {name} and I am {age} years old.")
```

You can put any expression inside the curly braces:

```python
a = 7
b = 3

print(f"{a} + {b} = {a + b}")          # 7 + 3 = 10
print(f"{a} divided by {b} = {a / b:.2f}")  # 7 divided by 3 = 2.33
```

The `:.2f` inside the braces is a **format specifier** — it tells Python to display the number with exactly 2 decimal places.

### 5.4 Putting It All Together

Here is a small program that uses everything from this section:

```python
# Get user input
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

# Calculate
current_year = 2026
age = current_year - birth_year

# Display result
print(f"Hello, {name}!")
print(f"You are approximately {age} years old.")
print(f"In 10 years you will be {age + 10}.")
```

Sample run:

```
Enter your name: Alice
Enter your birth year: 2001
Hello, Alice!
You are approximately 25 years old.
In 10 years you will be 35.
```

---

## What's Next

You now know the building blocks of every Python program. The next step is to practise what you have learned.

Head over to the **[exercises](./exercises/)** folder. There you will find hands-on challenges for each topic covered here:

- Variables and naming
- Working with data types
- Using operators
- Converting types
- Reading input and formatting output

Work through the exercises in order. Try to solve each one on your own before looking anything up — that is how the concepts stick.

Good luck!
