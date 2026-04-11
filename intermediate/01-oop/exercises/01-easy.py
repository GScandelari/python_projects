# ============================================================
# intermediate/01-oop/exercises/01-easy.py
# Topic: OOP — classes, __init__, instance attributes, methods
# Difficulty: Easy
# ============================================================

# Exercise 1
# ----------
# Create a class called Person with:
#   - Attributes: name (str), age (int)
#   - Method: greet() → returns "Hi, I'm {name} and I'm {age} years old."
#   - Method: is_adult() → returns True if age >= 18
#
# Expected:
#   p = Person("Alice", 28)
#   print(p.greet())       → Hi, I'm Alice and I'm 28 years old.
#   print(p.is_adult())    → True
#   print(Person("Tom", 15).is_adult())  → False

# Write your code here


# Exercise 2
# ----------
# Create a class called Rectangle with:
#   - Attributes: width, height
#   - Method: area() → returns width * height
#   - Method: perimeter() → returns 2 * (width + height)
#   - Method: is_square() → returns True if width == height
#   - __str__ → returns "Rectangle(width=W, height=H)"
#
# Expected:
#   r = Rectangle(4, 6)
#   print(r.area())        → 24
#   print(r.perimeter())   → 20
#   print(r.is_square())   → False
#   print(Rectangle(5,5).is_square())  → True
#   print(r)               → Rectangle(width=4, height=6)

# Write your code here


# Exercise 3
# ----------
# Create a class called Counter with:
#   - Attribute: count (starts at 0)
#   - Method: increment() → adds 1 to count
#   - Method: decrement() → subtracts 1, but never below 0
#   - Method: reset() → sets count back to 0
#   - Method: value() → returns current count
#
# Expected:
#   c = Counter()
#   c.increment()
#   c.increment()
#   c.increment()
#   c.decrement()
#   print(c.value())   → 2
#   c.reset()
#   print(c.value())   → 0
#   c.decrement()
#   print(c.value())   → 0   (never goes below zero)

# Write your code here
