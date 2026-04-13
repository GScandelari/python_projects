# OOP — Interview Questions

## Core Concepts

**Q: What are the four pillars of OOP?**

| Pillar | Definition | Python example |
|---|---|---|
| **Encapsulation** | Bundle data + methods; hide internal state | `_private`, `__mangled`, `@property` |
| **Abstraction** | Expose interface, hide implementation detail | `ABC`, `abstractmethod` |
| **Inheritance** | Derive new classes from existing ones | `class Dog(Animal)` |
| **Polymorphism** | Same interface, different behaviour per type | method overriding, duck typing |

---

**Q: What is the difference between `@classmethod`, `@staticmethod`, and an instance method?**

```python
class MyClass:
    count = 0

    def instance_method(self):
        # Access instance (self) and class
        return self

    @classmethod
    def class_method(cls):
        # Access class (cls), not instance
        # Use case: alternative constructors, factory methods
        cls.count += 1
        return cls()

    @staticmethod
    def static_method(x, y):
        # No access to self or cls
        # Use case: pure utility function related to the class
        return x + y
```

**Rule of thumb:** if it doesn't need `self` or `cls`, make it `@staticmethod`; if it needs the class but not the instance, make it `@classmethod`.

---

**Q: Explain Python's MRO (Method Resolution Order).**

Python uses the **C3 linearization** algorithm. The order is always: current class → left parent → right parent → further ancestors → `object`.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

D.__mro__
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

`super()` follows the MRO — important in cooperative multiple inheritance:

```python
class Base:
    def greet(self): print('Base')

class Left(Base):
    def greet(self):
        print('Left')
        super().greet()   # next in MRO, not necessarily Base

class Right(Base):
    def greet(self):
        print('Right')
        super().greet()

class Child(Left, Right):
    def greet(self):
        print('Child')
        super().greet()

Child().greet()
# Child → Left → Right → Base   (each super() follows D's MRO)
```

---

**Q: What are dunder (magic) methods? Give key examples.**

Dunder methods (double underscore) let custom classes integrate with Python's built-in operators and protocols.

| Method | Triggered by |
|---|---|
| `__init__` | `MyClass()` — initialisation |
| `__repr__` | `repr(obj)`, interactive shell |
| `__str__` | `str(obj)`, `print(obj)` |
| `__eq__` | `==` |
| `__lt__`, `__le__`, ... | `<`, `<=`, ... (or `@functools.total_ordering`) |
| `__hash__` | `hash(obj)`, dict key / set member |
| `__len__` | `len(obj)` |
| `__getitem__` | `obj[key]` |
| `__iter__` / `__next__` | `for x in obj` |
| `__contains__` | `x in obj` |
| `__enter__` / `__exit__` | `with obj as ...` |
| `__call__` | `obj(args)` |
| `__add__`, `__mul__`, ... | `+`, `*`, ... |

**Important:** if you define `__eq__`, Python sets `__hash__ = None` (making the object unhashable). Define `__hash__` explicitly if you need both.

---

**Q: What is the difference between `__repr__` and `__str__`?**

- `__repr__`: unambiguous developer representation — should ideally be valid Python to recreate the object.
- `__str__`: human-readable string — used by `print()` and `str()`.
- If only `__repr__` is defined, it is used as a fallback for `str()`.

```python
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def __repr__(self): return f'Point({self.x}, {self.y})'  # dev-friendly
    def __str__(self):  return f'({self.x}, {self.y})'       # user-friendly
```

---

## Encapsulation & Properties

**Q: How does Python implement access control?**

Python uses **naming conventions**, not enforced access modifiers:

| Convention | Meaning |
|---|---|
| `name` | Public — full access |
| `_name` | Protected by convention — "don't touch from outside" |
| `__name` | Name-mangled to `_ClassName__name` — harder to access accidentally |

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance   # mangled → _Account__balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError('Balance cannot be negative')
        self.__balance = value
```

---

## Inheritance & Polymorphism

**Q: What is duck typing?**

> "If it walks like a duck and quacks like a duck, it's a duck."

Python doesn't check types at runtime — it checks behaviour (method/attribute existence). Any object that implements the required interface works.

```python
def make_sound(animal):
    animal.speak()   # works for Dog, Cat, Robot — anything with speak()

class Robot:
    def speak(self): print('Beep boop')

make_sound(Robot())   # works — no inheritance required
```

---

**Q: Abstract base classes vs Protocols (structural subtyping)?**

- **ABC** (`abc.ABC` + `@abstractmethod`): nominal subtyping — subclass must explicitly inherit and implement all abstract methods.
- **Protocol** (Python 3.8+, `typing.Protocol`): structural subtyping — any class that has the required methods satisfies the protocol, no inheritance needed.

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self): print('O')   # satisfies Drawable — no inheritance

def render(obj: Drawable): obj.draw()
render(Circle())   # passes type checking and runtime
```

---

## SOLID

**Q: Explain the Single Responsibility Principle with a bad/good example.**

```python
# BAD — one class handles data AND formatting AND persistence
class Report:
    def generate(self): ...
    def to_pdf(self): ...
    def save_to_db(self): ...

# GOOD — separate concerns
class Report:
    def generate(self) -> dict: ...

class ReportFormatter:
    def to_pdf(self, report: Report) -> bytes: ...

class ReportRepository:
    def save(self, report: Report): ...
```

---

**Q: Explain the Open/Closed Principle.**

A class should be open for extension but closed for modification — add behaviour without changing existing code.

```python
# BAD — add new shape → modify area()
def area(shape):
    if isinstance(shape, Circle): return 3.14 * shape.r ** 2
    if isinstance(shape, Square): return shape.side ** 2

# GOOD — extend by adding new subclass
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Circle(Shape):
    def area(self): return 3.14 * self.r ** 2

class Triangle(Shape):   # new shape — no change to existing code
    def area(self): return 0.5 * self.base * self.height
```

---

## Design Patterns

**Q: What is the Singleton pattern? How is it implemented in Python?**

Ensures only one instance of a class exists.

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
a is b   # True
```

Python modules are singletons by nature — `import config` always returns the same module object.

---

**Q: What is the Factory pattern?**

Delegates object creation to a factory method, decoupling the caller from the concrete class.

```python
class Notification:
    def send(self, msg): raise NotImplementedError

class EmailNotification(Notification):
    def send(self, msg): print(f'Email: {msg}')

class SMSNotification(Notification):
    def send(self, msg): print(f'SMS: {msg}')

def notification_factory(channel: str) -> Notification:
    return {'email': EmailNotification, 'sms': SMSNotification}[channel]()

n = notification_factory('email')
n.send('Hello')
```

---

**Q: What is the Observer pattern?**

An object (subject) maintains a list of dependents (observers) and notifies them of state changes.

```python
class EventEmitter:
    def __init__(self):
        self._listeners: dict[str, list] = {}

    def on(self, event, callback):
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event, *args):
        for cb in self._listeners.get(event, []):
            cb(*args)

emitter = EventEmitter()
emitter.on('data', lambda x: print(f'Got: {x}'))
emitter.emit('data', 42)   # Got: 42
```

---

## Common Gotchas

| Gotcha | Explanation |
|---|---|
| Mutable class attribute | Shared across all instances — use instance attribute in `__init__` |
| `__eq__` without `__hash__` | Object becomes unhashable |
| Calling parent `__init__` | Forgetting `super().__init__()` in subclass |
| `isinstance` vs `type()` | `isinstance(d, Animal)` respects inheritance; `type(d) == Dog` does not |
| `copy` vs `deepcopy` on objects | Shallow copy shares nested mutable objects |
