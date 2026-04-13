# OOP — Cheat Sheet

## Class Basics

```python
class Animal:
    # Class attribute — shared by all instances
    kingdom = 'Animalia'

    def __init__(self, name: str, sound: str):
        # Instance attributes
        self.name  = name
        self._sound = sound   # convention: "private"

    def speak(self) -> str:
        return f'{self.name} says {self._sound}'

    @classmethod
    def create_dog(cls) -> 'Animal':
        """Factory method — alternative constructor."""
        return cls('Dog', 'Woof')

    @staticmethod
    def is_animal(obj) -> bool:
        """Utility — no access to cls or self."""
        return isinstance(obj, Animal)

    def __repr__(self) -> str:
        return f'Animal({self.name!r})'

    def __str__(self) -> str:
        return self.name
```

---

## Inheritance

```python
class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name, 'Woof')   # delegate to parent
        self.breed = breed

    # Override
    def speak(self) -> str:
        return f'{self.name} ({self.breed}) barks!'

    # Extend parent method
    def __repr__(self) -> str:
        return f'Dog({self.name!r}, {self.breed!r})'

# Multiple inheritance
class Flyable:
    def fly(self): return 'flying'

class FlyingDog(Dog, Flyable): ...
# MRO: FlyingDog → Dog → Animal → Flyable → object
print(FlyingDog.__mro__)
```

---

## Key Dunder Methods

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    # Representation
    def __repr__(self): return f'Vector({self.x}, {self.y})'
    def __str__(self):  return f'({self.x}, {self.y})'

    # Arithmetic
    def __add__(self, other): return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other): return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar): return Vector(self.x * scalar, self.y * scalar)
    def __rmul__(self, scalar): return self.__mul__(scalar)  # scalar * v

    # Comparison
    def __eq__(self, other): return self.x == other.x and self.y == other.y
    def __lt__(self, other): return abs(self) < abs(other)

    # Container protocol
    def __len__(self):     return 2
    def __getitem__(self, i): return (self.x, self.y)[i]
    def __iter__(self):    return iter((self.x, self.y))

    # Numeric
    def __abs__(self):     return (self.x**2 + self.y**2) ** 0.5
    def __neg__(self):     return Vector(-self.x, -self.y)
    def __bool__(self):    return self.x != 0 or self.y != 0

    # Context manager
    def __enter__(self):   return self
    def __exit__(self, *_): pass

    # Callable
    def __call__(self, scale): return self * scale

    # Hashing (needed if __eq__ is defined)
    def __hash__(self): return hash((self.x, self.y))
```

---

## Properties

```python
class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError('Below absolute zero')
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self.celsius = (value - 32) * 5/9

t = Temperature(100)
print(t.fahrenheit)   # 212.0
t.fahrenheit = 32
print(t.celsius)      # 0.0
```

---

## Abstract Base Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        return f'{type(self).__name__}: area={self.area():.2f}'

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self):      return 3.14159 * self.r ** 2
    def perimeter(self): return 2 * 3.14159 * self.r

# Shape()  → TypeError: Can't instantiate abstract class
```

---

## Dataclasses (Python 3.7+)

```python
from dataclasses import dataclass, field
from typing import ClassVar

@dataclass(order=True, frozen=False)
class Point:
    x: float
    y: float = 0.0
    label: str = field(default='', repr=False)
    _cache: dict = field(default_factory=dict, init=False, repr=False)
    count: ClassVar[int] = 0   # class variable, not instance field

    def distance(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

p1 = Point(1.0, 2.0)
p2 = Point(3.0)
print(p1)             # Point(x=1.0, y=2.0)
print(p1 < p2)        # True (order=True compares fields in order)
```

---

## SOLID Principles (quick reference)

| Principle | Rule | Bad smell |
|---|---|---|
| **S**ingle Responsibility | A class does one thing | Class that reads DB AND sends email |
| **O**pen/Closed | Open for extension, closed for modification | `if isinstance(x, Dog): ...` in base class |
| **L**iskov Substitution | Subclass can replace parent without breaking code | Subclass raises where parent would not |
| **I**nterface Segregation | Many specific interfaces > one general | `class Animal` with `fly()` and `swim()` |
| **D**ependency Inversion | Depend on abstractions, not concretions | `class Report` creates its own `PDFPrinter` |
