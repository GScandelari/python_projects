# ============================================================
# advanced/04-design-patterns/exercises/03-challenge.py
# Topic: Design Patterns — Builder, Command, combined patterns
# Difficulty: Challenge
# ============================================================

# Exercise 1 — Builder: SQL Query Builder
# ----------------------------------------
# Build a fluent QueryBuilder that supports:
#   .select(*fields)          → SELECT field1, field2 ...
#   .from_table(table)        → FROM table
#   .join(table, on)          → JOIN table ON condition
#   .where(*conditions)       → WHERE cond1 AND cond2
#   .order_by(field, desc=False)  → ORDER BY field [DESC]
#   .limit(n)                 → LIMIT n
#   .build()                  → returns the final SQL string
#
# Rules:
#   - select() defaults to "*" if not called
#   - join() can be called multiple times
#   - where() conditions are ANDed together
#   - build() raises ValueError if from_table() was never called
#
# Expected:
#   sql = (QueryBuilder()
#          .select("u.name", "u.email", "o.total")
#          .from_table("users u")
#          .join("orders o", "o.user_id = u.id")
#          .where("u.active = true", "o.total > 100")
#          .order_by("o.total", desc=True)
#          .limit(20)
#          .build())
#   # SELECT u.name, u.email, o.total
#   # FROM users u
#   # JOIN orders o ON o.user_id = u.id
#   # WHERE u.active = true AND o.total > 100
#   # ORDER BY o.total DESC
#   # LIMIT 20

# Write your code here


# Exercise 2 — Command: Text editor with undo/redo
# --------------------------------------------------
# Build a text editor with full undo/redo support using the
# Command pattern.
#
# Commands (each has execute(editor) and undo(editor)):
#   AppendCommand(text)        → appends text to editor.content
#   DeleteLastCommand(n)       → removes last n characters
#   ReplaceCommand(old, new)   → replaces first occurrence of old with new
#
# TextEditor:
#   - content: str (starts empty)
#   - execute(command) → runs command, pushes to undo stack, clears redo stack
#   - undo() → undoes last command, pushes to redo stack
#   - redo() → redoes last undone command
#   - history() → returns list of command class names in order
#
# Expected:
#   editor = TextEditor()
#   editor.execute(AppendCommand("Hello"))
#   editor.execute(AppendCommand(", World"))
#   editor.execute(ReplaceCommand("World", "Python"))
#   editor.content          → "Hello, Python"
#   editor.undo()
#   editor.content          → "Hello, World"
#   editor.undo()
#   editor.content          → "Hello"
#   editor.redo()
#   editor.content          → "Hello, World"

# Write your code here


# Exercise 3 — Combined: Plugin Registry (Factory + Singleton + Observer)
# ------------------------------------------------------------------------
# Build a plugin system combining three patterns:
#
# PluginRegistry (Singleton):
#   - register(name, plugin_class) → store the plugin class by name
#   - create(name, **kwargs) → instantiate and return the plugin
#   - list_plugins() → return sorted list of registered plugin names
#   - on_register(callback) → callback called whenever a new plugin
#                              is registered (Observer pattern)
#
# Plugin base class:
#   - name: str (class attribute)
#   - execute(**kwargs) → raises NotImplementedError
#
# Create 3 concrete plugins: LogPlugin, EmailPlugin, WebhookPlugin
# Each has an execute() that prints what it does.
#
# Demonstrate:
#   - Subscribe an observer that prints "[EVENT] Plugin registered: {name}"
#   - Register all 3 plugins (observer fires 3 times)
#   - list_plugins() → ['EmailPlugin', 'LogPlugin', 'WebhookPlugin']
#   - Create and execute each plugin with sample kwargs

# Write your code here
