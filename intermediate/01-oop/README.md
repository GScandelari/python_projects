# Object-Oriented Programming (OOP)

OOP is a paradigm that organizes code around **objects** — bundles of data (attributes) and behavior (methods). Python is fully object-oriented: everything you have used so far (strings, lists, dicts) is already an object.

## Table of Contents

- [Classes and Objects](#1-classes-and-objects)
- [The `__init__` Method](#2-the-__init__-method)
- [Instance vs Class Attributes](#3-instance-vs-class-attributes)
- [Methods](#4-methods)
- [Encapsulation](#5-encapsulation)
- [Inheritance](#6-inheritance)
- [Method Overriding](#7-method-overriding)
- [Dunder Methods](#8-dunder-methods)
- [Quick Reference](#quick-reference)
- [What's Next](#whats-next)

---

## 1. Classes and Objects

A **class** is a blueprint. An **object** (instance) is a specific thing built from that blueprint.

```python
class Dog:
    pass          # empty class — valid Python

rex = Dog()       # create an instance
print(type(rex))  # <class '__main__.Dog'>
```

Convention: class names use **PascalCase** (`BankAccount`, `ShoppingCart`).

---

## 2. The `__init__` Method

`__init__` is called automatically when you create an instance. It sets up the object's initial state.

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name      # instance attribute
        self.breed = breed
        self.age = age

rex = Dog("Rex", "Labrador", 3)
print(rex.name)    # Rex
print(rex.breed)   # Labrador
print(rex.age)     # 3
```

`self` refers to the **current instance** — always the first parameter of every instance method.

---

## 3. Instance vs Class Attributes

| | Instance Attribute | Class Attribute |
|---|---|---|
| Defined in | `__init__` with `self.` | Class body, outside any method |
| Unique per | Each object | All objects share the same value |
| Access | `self.attr` or `obj.attr` | `ClassName.attr` or `obj.attr` |

```python
class Dog:
    species = "Canis lupus familiaris"   # class attribute — shared by all dogs

    def __init__(self, name):
        self.name = name                 # instance attribute — unique per dog

rex = Dog("Rex")
fido = Dog("Fido")

print(Dog.species)    # Canis lupus familiaris
print(rex.species)    # Canis lupus familiaris
print(rex.name)       # Rex
print(fido.name)      # Fido
```

---

## 4. Methods

Methods are functions defined inside a class. They always take `self` as the first argument.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

    def human_years(self):
        """Return approximate age in human years."""
        return self.age * 7

    def birthday(self):
        """Increment age by 1."""
        self.age += 1

rex = Dog("Rex", 3)
print(rex.bark())          # Rex says: Woof!
print(rex.human_years())   # 21
rex.birthday()
print(rex.age)             # 4
```

---

## 5. Encapsulation

Encapsulation means hiding internal details. Python uses naming conventions:

| Convention | Meaning |
|---|---|
| `name` | Public — use freely |
| `_name` | Protected — internal use, avoid from outside |
| `__name` | Private — name-mangled, strongly internal |

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance       # protected

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return amount
        return 0

    def get_balance(self):
        return self._balance

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())   # 1300
```

---

## 6. Inheritance

A child class **inherits** all attributes and methods from its parent class, and can extend or override them.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

    def __str__(self):
        return f"Animal({self.name})"


class Dog(Animal):           # Dog inherits from Animal
    def speak(self):         # override the parent method
        return f"{self.name} says: Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"


animals = [Dog("Rex"), Cat("Whiskers"), Animal("Unknown")]
for a in animals:
    print(a.speak())
# Rex says: Woof!
# Whiskers says: Meow!
# Unknown makes a sound.
```

### `super()`

Use `super()` to call the parent's method from within the child:

```python
class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)       # call Dog (and Animal) __init__
        self.owner = owner

    def speak(self):
        base = super().speak()
        return f"{base} (Guide dog for {self.owner})"

g = GuideDog("Buddy", "Alice")
print(g.speak())   # Buddy says: Woof! (Guide dog for Alice)
```

---

## 7. Method Overriding

A subclass can replace any parent method. Python always calls the most specific version.

```python
class Shape:
    def area(self):
        return 0

    def describe(self):
        return f"I am a {type(self).__name__} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(s.describe())
# I am a Circle with area 78.54
# I am a Rectangle with area 24.00
```

---

## 8. Dunder Methods

Dunder (double underscore) methods let your objects work with Python's built-in syntax.

| Method | Triggered by |
|---|---|
| `__init__` | `MyClass()` |
| `__str__` | `str(obj)`, `print(obj)` |
| `__repr__` | `repr(obj)`, REPL display |
| `__len__` | `len(obj)` |
| `__eq__` | `obj1 == obj2` |
| `__lt__` | `obj1 < obj2` |
| `__add__` | `obj1 + obj2` |

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)           # Point(1, 2)
print(p1 + p2)      # Point(4, 6)
print(p1 == p2)     # False
print(p1 == Point(1, 2))  # True
```

---

## Quick Reference

```python
# Define a class
class MyClass:
    class_attr = "shared"           # class attribute

    def __init__(self, value):
        self.value = value          # instance attribute

    def method(self):               # instance method
        return self.value

    def __str__(self):              # string representation
        return f"MyClass({self.value})"

# Inheritance
class Child(Parent):
    def __init__(self, value, extra):
        super().__init__(value)     # call parent __init__
        self.extra = extra

    def method(self):               # override
        base = super().method()
        return f"{base} + {self.extra}"

# Create instances
obj = MyClass(42)
print(obj.value)       # 42
print(obj.method())    # 42
print(obj)             # MyClass(42)
print(MyClass.class_attr)  # shared
```

---

## What's Next

Try the exercises in [`exercises/`](./exercises/) — model real-world entities as classes.

Next concept: [`02-modules-packages`](../02-modules-packages/)
