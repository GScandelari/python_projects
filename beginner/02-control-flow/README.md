# 02 — Control Flow

So far you have written Python that runs top-to-bottom, one line at a time.
**Control flow** lets your program make decisions and repeat work — two abilities
that turn small scripts into genuinely useful programs.

No imports are needed for anything on this page. Every code block is ready to
run as-is.

---

## Table of Contents

1. [Conditional Statements](#1-conditional-statements)
   - 1.1 [if / elif / else](#11-if--elif--else)
   - 1.2 [Indentation Rules](#12-indentation-rules)
   - 1.3 [Nested Conditions](#13-nested-conditions)
   - 1.4 [Ternary Expression](#14-ternary-expression)
2. [Comparison and Logical Operators](#2-comparison-and-logical-operators)
3. [while Loop](#3-while-loop)
   - 3.1 [Basic Syntax](#31-basic-syntax)
   - 3.2 [break and continue](#32-break-and-continue)
   - 3.3 [Infinite Loop Pattern](#33-infinite-loop-pattern)
4. [for Loop](#4-for-loop)
   - 4.1 [range()](#41-range)
   - 4.2 [Iterating over Strings and Lists](#42-iterating-over-strings-and-lists)
   - 4.3 [break, continue, and else](#43-break-continue-and-else)
5. [Common Patterns](#5-common-patterns)
   - 5.1 [Accumulator Pattern](#51-accumulator-pattern)
   - 5.2 [Counting Occurrences](#52-counting-occurrences)
   - 5.3 [Finding Min and Max Manually](#53-finding-min-and-max-manually)
6. [What's Next](#whats-next)

---

## 1. Conditional Statements

A **conditional statement** lets your program choose between different paths
depending on whether something is true or false.

### 1.1 if / elif / else

```python
temperature = 35

if temperature > 30:
    print("It's hot outside.")
elif temperature > 20:
    print("It's a pleasant day.")
elif temperature > 10:
    print("It's a bit chilly.")
else:
    print("It's cold outside.")
```

How it works:

1. Python evaluates the `if` condition first.
2. If it is `True`, it runs that block and **skips** all remaining `elif` and
   `else` branches.
3. If it is `False`, Python moves to the next `elif` and checks that condition.
4. `else` is a catch-all — it runs only when every condition above was `False`.
5. `elif` and `else` are both optional. A lone `if` is perfectly valid.

```python
# Minimal example — just an if
score = 80

if score >= 50:
    print("You passed!")
```

### 1.2 Indentation Rules

Python uses **indentation** (spaces or tabs at the start of a line) to define
which code belongs to which block. This is not optional decoration — Python will
raise an error if the indentation is wrong.

**The rule:** every line inside a block must be indented by the same amount.
The official style (PEP 8) recommends **4 spaces** per level.

```python
age = 20

if age >= 18:
    print("You are an adult.")   # 4 spaces — inside the if block
    print("You can vote.")       # still 4 spaces — same block

print("This always runs.")       # 0 spaces — outside the if block
```

```python
# WRONG — mismatched indentation causes an IndentationError
if age >= 18:
    print("Adult")
  print("Still inside?")   # 2 spaces instead of 4 — Python will complain
```

A good rule of thumb: every time you write a colon (`:`) at the end of a line,
the *next* line must be indented one level deeper.

### 1.3 Nested Conditions

You can place an `if` statement inside another `if` statement. Each level gets
an additional 4 spaces of indentation.

```python
has_ticket = True
age = 15

if has_ticket:
    print("You have a ticket.")
    if age >= 18:
        print("You may enter the adult section.")
    else:
        print("You must stay in the general area.")
else:
    print("Sorry, no ticket — no entry.")
```

Tip: if you find yourself nesting more than two or three levels deep, the logic
is usually easier to read when split into separate functions or combined with
logical operators (see the next section).

### 1.4 Ternary Expression

Python has a compact, one-line form of if/else called a **ternary expression**
(also called a conditional expression).

```
value_if_true  if  condition  else  value_if_false
```

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)   # adult
```

```python
number = -7
description = "positive" if number > 0 else "non-positive"
print(description)   # non-positive
```

Use the ternary expression when the result is a single, simple value. For
anything more complex, the regular multi-line form is easier to read.

---

## 2. Comparison and Logical Operators

You used these in **01-fundamentals**. Here is a quick reference, because you
will need them constantly with control flow.

### Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | equal to | `5 == 5` | `True` |
| `!=` | not equal to | `5 != 3` | `True` |
| `>` | greater than | `7 > 3` | `True` |
| `<` | less than | `2 < 8` | `True` |
| `>=` | greater than or equal | `5 >= 5` | `True` |
| `<=` | less than or equal | `4 <= 3` | `False` |

### Logical Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | both must be True | `True and False` | `False` |
| `or` | at least one must be True | `True or False` | `True` |
| `not` | reverses True/False | `not True` | `False` |

### Membership Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `in` | value is present | `"a" in "cat"` | `True` |
| `not in` | value is absent | `3 not in [1, 2]` | `True` |

```python
username = "alice"
password_length = 10
is_admin = False

# Combining operators in a condition
if len(username) >= 3 and password_length >= 8 and not is_admin:
    print("Regular user login successful.")
```

```python
vowels = "aeiou"
letter = "e"

if letter in vowels:
    print(f"'{letter}' is a vowel.")
else:
    print(f"'{letter}' is a consonant.")
```

---

## 3. while Loop

A `while` loop keeps running its block of code **for as long as a condition
remains True**.

### 3.1 Basic Syntax

```
while condition:
    # code to repeat
```

```python
count = 1

while count <= 5:
    print(f"Count is {count}")
    count += 1   # move count forward so the loop eventually stops

print("Done!")
```

Output:
```
Count is 1
Count is 2
Count is 3
Count is 4
Count is 5
Done!
```

> **Warning — infinite loops:** If the condition never becomes `False`, your
> program will loop forever. Always make sure something inside the loop changes
> the condition.

```python
# DANGER — infinite loop (do not run this as written)
# n = 1
# while n > 0:
#     print(n)   # n never changes, so this runs forever
```

### 3.2 break and continue

| Keyword | What it does |
|---------|-------------|
| `break` | Exits the loop immediately, no matter what the condition says |
| `continue` | Skips the rest of the current iteration and jumps back to the condition check |

```python
# break example — stop as soon as we find a negative number
numbers = [4, 7, 2, -3, 8, 1]
index = 0

while index < len(numbers):
    if numbers[index] < 0:
        print(f"Found a negative number: {numbers[index]}")
        break            # exit the loop right now
    index += 1
```

```python
# continue example — skip even numbers, only print odd ones
n = 0

while n < 10:
    n += 1
    if n % 2 == 0:
        continue         # skip even numbers
    print(n)             # only reached for odd n
```

### 3.3 Infinite Loop Pattern

A common and intentional pattern is to write `while True:` and use `break` to
exit when a certain condition is met. This is useful when the number of
iterations is unknown in advance.

```python
# Keep asking the user for a positive number until they give one
while True:
    raw = input("Enter a positive number: ")
    number = int(raw)
    if number > 0:
        print(f"Thank you! You entered {number}.")
        break
    else:
        print("That is not positive. Please try again.")
```

The loop runs indefinitely until the user enters a valid value, at which point
`break` ends it.

---

## 4. for Loop

A `for` loop **iterates** over a sequence, processing each item one at a time.
You do not need to manage a counter manually.

### 4.1 range()

`range()` generates a sequence of integers. It is the most common companion to
a `for` loop when you need to repeat something a fixed number of times.

| Call | Produces |
|------|----------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(2, 6)` | 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

```python
# Print squares of 1 through 5
for i in range(1, 6):
    print(f"{i} squared is {i ** 2}")
```

```python
# Countdown
for i in range(5, 0, -1):
    print(i)
print("Blast off!")
```

```python
# Repeat something a fixed number of times (the variable is ignored)
for _ in range(3):
    print("Hello!")
```

The underscore `_` is a Python convention for a loop variable you do not
actually need.

### 4.2 Iterating over Strings and Lists

Any **sequence** can be used directly in a `for` loop — Python will hand you
one item at a time.

**Strings** — each character in turn:

```python
word = "Python"

for letter in word:
    print(letter)
```

```python
# Count how many times 'a' appears in a word
word = "banana"
count = 0

for letter in word:
    if letter == "a":
        count += 1

print(f"'a' appears {count} times.")   # 3
```

**Lists** — each element in turn (lists are covered in depth in 03-data-structures):

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}.")
```

```python
# Sum a list of numbers
grades = [88, 72, 95, 60, 84]
total = 0

for grade in grades:
    total += grade

print(f"Total: {total}")
print(f"Average: {total / len(grades):.1f}")
```

### 4.3 break, continue, and else

`break` and `continue` work the same way inside a `for` loop as they do inside
a `while` loop.

```python
# break — stop when the target is found
names = ["Alice", "Bob", "Carol", "Dave"]

for name in names:
    if name == "Carol":
        print("Found Carol!")
        break
    print(f"Not Carol: {name}")
```

```python
# continue — skip entries that do not meet a condition
scores = [55, 82, 40, 91, 73]

print("Passing scores (>= 60):")
for score in scores:
    if score < 60:
        continue        # skip this score and move to the next
    print(score)
```

**The else clause on a loop**

A `for` loop (and a `while` loop) can have an `else` block. The `else` runs
when the loop finishes **normally** — that is, without hitting a `break`.

```python
# Search for a number; report if it was not found
target = 7
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

for number in numbers:
    if number == target:
        print(f"Found {target}!")
        break
else:
    # This runs only if break was never triggered
    print(f"{target} was not in the list.")
```

This pattern is a clean alternative to using a boolean flag variable.

---

## 5. Common Patterns

The following patterns appear constantly in real Python programs. Understanding
them early will make every loop you write easier.

### 5.1 Accumulator Pattern

Start a variable at a neutral value, then update it inside the loop.

```python
# Sum all numbers from 1 to 100
total = 0             # neutral value for addition

for n in range(1, 101):
    total += n        # accumulate

print(f"Sum 1–100: {total}")   # 5050
```

```python
# Build a string character by character
word = "Hello"
reversed_word = ""    # neutral value for string concatenation

for letter in word:
    reversed_word = letter + reversed_word

print(reversed_word)   # olleH
```

The key idea: the accumulator variable exists **before** the loop, is updated
**inside** the loop, and is used **after** the loop.

### 5.2 Counting Occurrences

A specialisation of the accumulator pattern where you count how many times
something happens.

```python
# Count vowels in a sentence
sentence = "The quick brown fox jumps over the lazy dog"
vowels = "aeiouAEIOU"
vowel_count = 0

for char in sentence:
    if char in vowels:
        vowel_count += 1

print(f"Vowels found: {vowel_count}")
```

```python
# Count how many grades are above average
grades = [55, 78, 92, 60, 85, 70, 88]
total = 0

for g in grades:
    total += g

average = total / len(grades)
above_count = 0

for g in grades:
    if g > average:
        above_count += 1

print(f"Average: {average:.1f}")
print(f"Grades above average: {above_count}")
```

### 5.3 Finding Min and Max Manually

Python has built-in `min()` and `max()` functions, but implementing them
yourself is an excellent exercise in loop thinking.

The strategy: start by assuming the first item is the best candidate, then
update whenever you find a better one.

```python
# Find the maximum value
numbers = [34, 12, 78, 56, 23, 91, 45]
maximum = numbers[0]   # assume first is largest

for n in numbers:
    if n > maximum:
        maximum = n    # found a bigger one — update

print(f"Maximum: {maximum}")   # 91
```

```python
# Find the minimum value
numbers = [34, 12, 78, 56, 23, 91, 45]
minimum = numbers[0]   # assume first is smallest

for n in numbers:
    if n < minimum:
        minimum = n

print(f"Minimum: {minimum}")   # 12
```

```python
# Find both in a single pass
numbers = [34, 12, 78, 56, 23, 91, 45]
lowest = numbers[0]
highest = numbers[0]

for n in numbers:
    if n < lowest:
        lowest = n
    if n > highest:
        highest = n

print(f"Lowest: {lowest}, Highest: {highest}")
```

---

## Quick Reference

```python
# if / elif / else
if condition_a:
    ...
elif condition_b:
    ...
else:
    ...

# Ternary
result = value_a if condition else value_b

# while loop
while condition:
    ...
    if something:
        break       # exit immediately
    if other:
        continue    # skip to next check

# for loop with range
for i in range(start, stop, step):
    ...

# for loop over a sequence
for item in sequence:
    ...
else:
    # runs if break was never hit
    ...
```

---

## What's Next

Head over to the **`exercises/`** folder inside this directory. The exercises
are organised by topic and increase in difficulty:

- Start with the conditional exercises to practise `if/elif/else`.
- Move on to the loop exercises — they build directly on the patterns above.
- The final challenges combine conditions and loops to solve small real-world
  problems.

After you are comfortable with control flow, continue to
**`03-data-structures/`** where you will learn about lists, tuples,
dictionaries, and sets — the containers that make loops truly powerful.

Good luck, and remember: the best way to learn is to experiment. Change the
values in the examples, break things on purpose, and see what happens.
