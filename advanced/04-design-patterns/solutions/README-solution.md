# Solutions Guide — 04-design-patterns

---

## Key Concepts by Exercise

### Easy 1 — Singleton
`__new__` controls instance creation. The check `if cls._instance is None` ensures only one instance is ever created. `hasattr(self, "_initialized")` in `__init__` (if used) prevents re-initialization on subsequent calls. **Warning:** Singletons make testing harder — prefer dependency injection when possible.

### Easy 2 — Factory
A dict mapping type strings to classes (`_SHAPES = {"circle": Circle, ...}`) is cleaner than `if/elif` chains. `cls(**kwargs)` forwards keyword arguments to the constructor — the factory doesn't need to know what each shape requires.

### Easy 3 — Template Method
The base class defines `generate()` — the algorithm skeleton. Subclasses override `header()` and `footer()` to specialize steps. `body()` has a default implementation that subclasses can optionally override. This avoids code duplication across report types while keeping differences isolated.

---

### Medium 1 — Observer
`_subscribers` is a dict mapping event names (stock symbols) to lists of observer objects. `update_price` iterates all observers without knowing their types — polymorphism via duck typing. Observers only need a `notify(symbol, price)` method.

### Medium 2 — Strategy
The strategy is injected at runtime via `checkout(strategy)`. Each strategy implements `apply(total)`. Swapping strategies doesn't require changing `ShoppingCart`. This is the Open/Closed Principle in action: open for extension (new strategies), closed for modification.

### Medium 3 — GoF Decorator
Each decorator wraps a `component` and adds one transformation. Decorators can be stacked in any order by nesting constructors. This is more flexible than inheritance: you don't need a class for every combination.

---

### Challenge 1 — QueryBuilder
Method chaining (`return self`) enables a fluent API where each call returns the builder itself. The `build()` method validates required state (`_table`) before assembling the SQL. `_joins` is a list to support multiple `JOIN` clauses.

### Challenge 2 — Command with undo/redo
Two stacks (`_undo_stack` and `_redo_stack`) implement undo/redo. On `execute`, the command goes to the undo stack and the redo stack is cleared (a new action invalidates the redo history). `DeleteLastCommand` saves the deleted text in `_deleted` so `undo` can restore it — the command carries its own rollback data.

### Challenge 3 — Combined patterns
`PluginRegistry` is a Singleton so all callers share the same registry. `register()` acts as a Factory registration step. `on_register()` callbacks implement Observer — any number of listeners can react to plugin registration. Resetting `_instance = None` in tests is the standard way to reset a Singleton between test cases.

---

## Pattern Selection Guide

| You want to... | Use |
|---|---|
| Share one instance globally | Singleton |
| Create objects without knowing their class | Factory |
| Build complex objects step by step | Builder |
| Add behaviour without subclassing | Decorator (GoF) |
| Make two incompatible interfaces work together | Adapter |
| Notify many objects when something changes | Observer |
| Swap algorithms at runtime | Strategy |
| Support undo/redo, queuing of actions | Command |
| Define an algorithm skeleton with variable steps | Template Method |

## Common Mistakes

### Overusing Singleton
Singletons are global state. They make unit testing hard (shared state between tests) and create hidden dependencies. Prefer passing the shared object as a constructor argument (dependency injection).

### Making the base class too abstract
Template Method works best when the base class provides a useful default for at least one step. If every method is `raise NotImplementedError`, consider whether an interface (Protocol) would be cleaner.

### Strategy with too many strategies
When strategies proliferate and each is used once, simple functions or lambdas are often cleaner than a full class hierarchy. Use classes when strategies need state or multiple methods.
