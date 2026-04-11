# Solutions Guide — 01-oop

---

## What Each Exercise Reinforces

### Easy 1 — Person
**Concept:** `__init__`, `self`, instance attributes, boolean-returning method.  
Every instance gets its own copy of `name` and `age`. `is_adult()` returns `self.age >= 18` directly — no need for an explicit `if/else`.

### Easy 2 — Rectangle
**Concept:** Methods as computed properties, `__str__` dunder.  
`__str__` controls what `print(obj)` and `str(obj)` produce. Always implement it for classes that will be displayed to users.

### Easy 3 — Counter
**Concept:** Mutable object state, guard clauses.  
`max(0, self.count - 1)` is cleaner than an `if` block for a floor guard.

### Medium 1 — BankAccount
**Concept:** Encapsulation with `_balance`, input validation with `ValueError`.  
Prefixing with `_` signals "internal — don't touch directly". Raising `ValueError` for bad input is the Pythonic approach over silently doing nothing.

### Medium 2 — Student with class attribute
**Concept:** Class attribute vs instance attribute.  
`school` belongs to the class — all students share it and it can be changed for everyone via `Student.school = "..."`. `grades` is an instance list — each student has their own.

### Medium 3 — Shape hierarchy
**Concept:** Inheritance, method overriding, `type(self).__name__`.  
`type(self).__name__` inside `Shape.describe()` returns the actual subclass name (`"Circle"`, `"Triangle"`), not `"Shape"` — polymorphism in action.

### Challenge 1 — Vector2D
**Concept:** Dunder methods for operator overloading.  
`__add__`, `__sub__`, `__mul__` let you write `v1 + v2` instead of `v1.add(v2)`. The convention is to return a **new** instance, not modify `self`.

### Challenge 2 — Vehicle → Car → ElectricCar
**Concept:** Multi-level inheritance, `super()`, overriding.  
Each level adds or specializes behavior. `super().__init__()` avoids duplicating the parent setup. `ElectricCar` can set `fuel_type="electric"` transparently.

### Challenge 3 — Library + Book (composition)
**Concept:** Composition — a class that *contains* instances of another class.  
Prefer composition over deep inheritance when objects have a "has-a" relationship (a Library *has* Books) rather than an "is-a" relationship.

---

## Key OOP Concepts at a Glance

| Concept | Keyword / Pattern | When to use |
|---|---|---|
| Define a class | `class Name:` | Model a real-world entity |
| Constructor | `def __init__(self, ...)` | Set initial state |
| Instance attribute | `self.attr = value` | Per-object data |
| Class attribute | `attr = value` (class body) | Shared constant or counter |
| Instance method | `def method(self)` | Behavior that reads/modifies state |
| Inheritance | `class Child(Parent)` | "is-a" relationship |
| Call parent | `super().method()` | Extend without duplicating |
| String repr | `__str__` / `__repr__` | Human / debug display |
| Operator overload | `__add__`, `__eq__`, etc. | Natural syntax for custom types |
| Encapsulation | `_attr` convention | Hide implementation details |
| Composition | Attribute = other object | "has-a" relationship |

---

## Common Beginner Mistakes

### 1. Forgetting `self` in method definition
```python
class Dog:
    def bark():          # missing self → TypeError when called
        return "Woof!"

# Fix:
    def bark(self):
        return "Woof!"
```

### 2. Forgetting `self.` when accessing attributes
```python
class Dog:
    def __init__(self, name):
        name = name      # creates a local variable, NOT an attribute!

# Fix:
        self.name = name
```

### 3. Mutable default in class attribute
```python
class Student:
    grades = []          # shared by ALL instances!

s1 = Student()
s2 = Student()
s1.grades.append(10)
print(s2.grades)         # [10] — unexpected!

# Fix: initialize list in __init__
class Student:
    def __init__(self):
        self.grades = []
```

### 4. Not calling `super().__init__()` in subclass
```python
class Cat(Animal):
    def __init__(self, name, indoor):
        # forgot super().__init__(name) → self.name never set!
        self.indoor = indoor

# Fix:
    def __init__(self, name, indoor):
        super().__init__(name)
        self.indoor = indoor
```

### 5. Modifying `self` in dunder operator methods
```python
def __add__(self, other):
    self.x += other.x   # mutates self — unexpected side effect!
    return self

# Fix: return a new instance
def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)
```

### 6. Confusing `__str__` and `__repr__`
- `__str__` → human-readable, used by `print()` and `str()`
- `__repr__` → unambiguous, used in the REPL and `repr()`  
- Rule: if only one, implement `__repr__` — Python falls back to it for both.
