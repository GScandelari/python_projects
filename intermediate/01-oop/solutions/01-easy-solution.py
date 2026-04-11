# ============================================================
# intermediate/01-oop/solutions/01-easy-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Person class
# ----------------------------------------------------------
# APPROACH: Simple class with two instance attributes set in __init__.
# Methods access them via self. is_adult() returns a boolean expression.

class Person:
    """Represents a person with a name and age."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

    def is_adult(self):
        return self.age >= 18


p = Person("Alice", 28)
print(p.greet())                     # Hi, I'm Alice and I'm 28 years old.
print(p.is_adult())                  # True
print(Person("Tom", 15).is_adult())  # False


# ----------------------------------------------------------
# Exercise 2 — Rectangle class
# ----------------------------------------------------------
# APPROACH: Formulas stored as methods. __str__ is the dunder
# that controls what print() shows for the object.

class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


r = Rectangle(4, 6)
print(r.area())               # 24
print(r.perimeter())          # 20
print(r.is_square())          # False
print(Rectangle(5, 5).is_square())  # True
print(r)                      # Rectangle(width=4, height=6)


# ----------------------------------------------------------
# Exercise 3 — Counter class
# ----------------------------------------------------------
# APPROACH: State is stored as a single integer attribute.
# decrement() uses max() to prevent going below zero.

class Counter:
    """A simple counter that never goes below zero."""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count = max(0, self.count - 1)

    def reset(self):
        self.count = 0

    def value(self):
        return self.count


c = Counter()
c.increment()
c.increment()
c.increment()
c.decrement()
print(c.value())   # 2
c.reset()
print(c.value())   # 0
c.decrement()
print(c.value())   # 0
