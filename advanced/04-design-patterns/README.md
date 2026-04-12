# Design Patterns

Design patterns are proven, reusable solutions to common software design problems. They're not code to copy — they're templates for thinking about structure.

## Table of Contents

- [Creational Patterns](#creational-patterns)
  - [Singleton](#1-singleton)
  - [Factory](#2-factory)
  - [Builder](#3-builder)
- [Structural Patterns](#structural-patterns)
  - [Decorator (GoF)](#4-decorator-gof)
  - [Adapter](#5-adapter)
- [Behavioural Patterns](#behavioural-patterns)
  - [Observer](#6-observer)
  - [Strategy](#7-strategy)
  - [Command](#8-command)
  - [Template Method](#9-template-method)
- [Quick Reference](#quick-reference)
- [What's Next](#whats-next)

---

## Creational Patterns

### 1. Singleton

Ensures a class has **exactly one instance**. Use for shared resources (config, logger, connection pool).

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, "_initialized"):
            self.value = value
            self._initialized = True


a = Singleton("first")
b = Singleton("second")
print(a is b)        # True — same object
print(a.value)       # first (second call to __init__ is ignored)
```

---

### 2. Factory

A factory function or class creates objects without exposing instantiation logic:

```python
class Dog:
    def speak(self): return "Woof!"

class Cat:
    def speak(self): return "Meow!"

class Bird:
    def speak(self): return "Tweet!"

def animal_factory(animal_type):
    animals = {"dog": Dog, "cat": Cat, "bird": Bird}
    cls = animals.get(animal_type.lower())
    if cls is None:
        raise ValueError(f"Unknown animal: {animal_type!r}")
    return cls()

for kind in ["dog", "cat", "bird"]:
    animal = animal_factory(kind)
    print(animal.speak())
# Woof! Meow! Tweet!
```

---

### 3. Builder

Separates the construction of a complex object from its representation:

```python
class QueryBuilder:
    def __init__(self, table):
        self._table  = table
        self._fields = ["*"]
        self._where  = []
        self._limit  = None

    def select(self, *fields):
        self._fields = list(fields)
        return self   # return self enables method chaining

    def where(self, condition):
        self._where.append(condition)
        return self

    def limit(self, n):
        self._limit = n
        return self

    def build(self):
        sql = f"SELECT {', '.join(self._fields)} FROM {self._table}"
        if self._where:
            sql += " WHERE " + " AND ".join(self._where)
        if self._limit:
            sql += f" LIMIT {self._limit}"
        return sql


query = (QueryBuilder("users")
         .select("name", "email")
         .where("age > 18")
         .where("active = true")
         .limit(10)
         .build())
print(query)
# SELECT name, email FROM users WHERE age > 18 AND active = true LIMIT 10
```

---

## Structural Patterns

### 4. Decorator (GoF)

The GoF Decorator wraps an object to add behaviour — distinct from Python's `@decorator` syntax, though the concept is the same:

```python
class TextRenderer:
    def render(self, text):
        return text

class BoldDecorator:
    def __init__(self, component):
        self._component = component

    def render(self, text):
        return f"<b>{self._component.render(text)}</b>"

class ItalicDecorator:
    def __init__(self, component):
        self._component = component

    def render(self, text):
        return f"<i>{self._component.render(text)}</i>"


renderer = ItalicDecorator(BoldDecorator(TextRenderer()))
print(renderer.render("Hello"))   # <i><b>Hello</b></i>
```

---

### 5. Adapter

Converts one interface into another that a client expects:

```python
class EuropeanSocket:
    def voltage(self): return 220
    def plug_type(self): return "Type C"

class USADevice:
    def run(self, socket):
        if socket.voltage() > 150:
            raise RuntimeError("Too much voltage!")
        return "Device running"

class SocketAdapter:
    def __init__(self, european_socket):
        self._socket = european_socket

    def voltage(self): return 110        # step down
    def plug_type(self): return "Type A"

eu = EuropeanSocket()
adapter = SocketAdapter(eu)
device = USADevice()
print(device.run(adapter))   # Device running
```

---

## Behavioural Patterns

### 6. Observer

Objects (observers) subscribe to events from a subject. When the subject's state changes, all observers are notified:

```python
class EventEmitter:
    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event, *args, **kwargs):
        for cb in self._listeners.get(event, []):
            cb(*args, **kwargs)


emitter = EventEmitter()
emitter.on("data", lambda x: print(f"Logger: {x}"))
emitter.on("data", lambda x: print(f"Processor: {x.upper()}"))
emitter.on("error", lambda e: print(f"Error: {e}"))

emitter.emit("data", "hello world")
# Logger: hello world
# Processor: HELLO WORLD

emitter.emit("error", "connection refused")
# Error: connection refused
```

---

### 7. Strategy

Defines a family of algorithms, encapsulates each one, and makes them interchangeable:

```python
class Sorter:
    def __init__(self, strategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy(data)


data = [3, 1, 4, 1, 5, 9, 2, 6]

asc_sorter  = Sorter(strategy=sorted)
desc_sorter = Sorter(strategy=lambda d: sorted(d, reverse=True))
len_sorter  = Sorter(strategy=lambda d: sorted(d, key=lambda x: str(x)))

print(asc_sorter.sort(data))    # [1, 1, 2, 3, 4, 5, 6, 9]
print(desc_sorter.sort(data))   # [9, 6, 5, 4, 3, 2, 1, 1]
```

---

### 8. Command

Encapsulates a request as an object, allowing undo/redo, queuing, and logging:

```python
class TextEditor:
    def __init__(self):
        self.text = ""
        self._history = []

    def execute(self, command):
        command.execute(self)
        self._history.append(command)

    def undo(self):
        if self._history:
            self._history.pop().undo(self)

class AppendCommand:
    def __init__(self, text):
        self._text = text

    def execute(self, editor):
        editor.text += self._text

    def undo(self, editor):
        editor.text = editor.text[:-len(self._text)]


editor = TextEditor()
editor.execute(AppendCommand("Hello"))
editor.execute(AppendCommand(", World"))
print(editor.text)   # Hello, World
editor.undo()
print(editor.text)   # Hello
```

---

### 9. Template Method

Defines the skeleton of an algorithm in a base class, deferring specific steps to subclasses:

```python
class DataProcessor:
    def process(self, data):          # template method
        raw     = self.load(data)
        cleaned = self.clean(raw)
        result  = self.transform(cleaned)
        self.save(result)
        return result

    def load(self, data): return data
    def clean(self, data): return data
    def transform(self, data): raise NotImplementedError
    def save(self, result): print(f"Saved: {result}")

class UpperProcessor(DataProcessor):
    def transform(self, data):
        return data.upper()

class ReverseProcessor(DataProcessor):
    def transform(self, data):
        return data[::-1]

UpperProcessor().process("hello")    # Saved: HELLO
ReverseProcessor().process("hello")  # Saved: olleh
```

---

## Quick Reference

| Pattern | Category | Use when |
|---|---|---|
| Singleton | Creational | One shared instance (config, logger) |
| Factory | Creational | Create objects without knowing the exact class |
| Builder | Creational | Construct complex objects step by step |
| Decorator | Structural | Add behaviour to objects at runtime |
| Adapter | Structural | Make incompatible interfaces work together |
| Observer | Behavioural | Notify many objects when state changes |
| Strategy | Behavioural | Swap algorithms at runtime |
| Command | Behavioural | Encapsulate actions (undo/redo, queue) |
| Template Method | Behavioural | Common algorithm, variable steps |

---

## What's Next

Try the exercises in [`exercises/`](./exercises/) — implement patterns for real scenarios.

Next concept: [`projects/`](../projects/)
