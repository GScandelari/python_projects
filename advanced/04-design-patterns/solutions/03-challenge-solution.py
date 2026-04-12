# ============================================================
# advanced/04-design-patterns/solutions/03-challenge-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Builder: SQL QueryBuilder
# ----------------------------------------------------------
class QueryBuilder:
    def __init__(self):
        self._fields  = ["*"]
        self._table   = None
        self._joins   = []
        self._wheres  = []
        self._order   = None
        self._desc    = False
        self._limit   = None

    def select(self, *fields):
        self._fields = list(fields)
        return self

    def from_table(self, table):
        self._table = table
        return self

    def join(self, table, on):
        self._joins.append((table, on))
        return self

    def where(self, *conditions):
        self._wheres.extend(conditions)
        return self

    def order_by(self, field, desc=False):
        self._order = field
        self._desc  = desc
        return self

    def limit(self, n):
        self._limit = n
        return self

    def build(self):
        if self._table is None:
            raise ValueError("from_table() is required before calling build()")
        parts = [f"SELECT {', '.join(self._fields)}",
                 f"FROM {self._table}"]
        for table, on in self._joins:
            parts.append(f"JOIN {table} ON {on}")
        if self._wheres:
            parts.append("WHERE " + " AND ".join(self._wheres))
        if self._order:
            order_dir = " DESC" if self._desc else ""
            parts.append(f"ORDER BY {self._order}{order_dir}")
        if self._limit:
            parts.append(f"LIMIT {self._limit}")
        return "\n".join(parts)


print("--- QueryBuilder ---")
sql = (QueryBuilder()
       .select("u.name", "u.email", "o.total")
       .from_table("users u")
       .join("orders o", "o.user_id = u.id")
       .where("u.active = true", "o.total > 100")
       .order_by("o.total", desc=True)
       .limit(20)
       .build())
print(sql)

try:
    QueryBuilder().build()
except ValueError as e:
    print(f"\nValueError: {e}")


# ----------------------------------------------------------
# Exercise 2 — Command: TextEditor with undo/redo
# ----------------------------------------------------------
class AppendCommand:
    def __init__(self, text):
        self._text = text

    def execute(self, editor):
        editor.content += self._text

    def undo(self, editor):
        editor.content = editor.content[:-len(self._text)]


class DeleteLastCommand:
    def __init__(self, n):
        self._n    = n
        self._deleted = ""

    def execute(self, editor):
        self._deleted = editor.content[-self._n:]
        editor.content = editor.content[:-self._n]

    def undo(self, editor):
        editor.content += self._deleted


class ReplaceCommand:
    def __init__(self, old, new):
        self._old = old
        self._new = new

    def execute(self, editor):
        editor.content = editor.content.replace(self._old, self._new, 1)

    def undo(self, editor):
        editor.content = editor.content.replace(self._new, self._old, 1)


class TextEditor:
    def __init__(self):
        self.content = ""
        self._undo_stack = []
        self._redo_stack = []

    def execute(self, command):
        command.execute(self)
        self._undo_stack.append(command)
        self._redo_stack.clear()

    def undo(self):
        if self._undo_stack:
            cmd = self._undo_stack.pop()
            cmd.undo(self)
            self._redo_stack.append(cmd)

    def redo(self):
        if self._redo_stack:
            cmd = self._redo_stack.pop()
            cmd.execute(self)
            self._undo_stack.append(cmd)

    def history(self):
        return [type(c).__name__ for c in self._undo_stack]


print("\n--- TextEditor with undo/redo ---")
editor = TextEditor()
editor.execute(AppendCommand("Hello"))
editor.execute(AppendCommand(", World"))
editor.execute(ReplaceCommand("World", "Python"))
print(editor.content)   # Hello, Python
editor.undo()
print(editor.content)   # Hello, World
editor.undo()
print(editor.content)   # Hello
editor.redo()
print(editor.content)   # Hello, World
print(editor.history()) # ['AppendCommand', 'ReplaceCommand'] (redo consumed the last undo-able command... actually: AppendCommand was first, then redo pushed ReplaceCommand back)


# ----------------------------------------------------------
# Exercise 3 — Plugin Registry (Singleton + Factory + Observer)
# ----------------------------------------------------------
class PluginRegistry:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._plugins    = {}
            cls._instance._observers  = []
        return cls._instance

    def on_register(self, callback):
        self._observers.append(callback)

    def register(self, name, plugin_class):
        self._plugins[name] = plugin_class
        for cb in self._observers:
            cb(name)

    def create(self, name, **kwargs):
        cls = self._plugins.get(name)
        if cls is None:
            raise KeyError(f"Plugin '{name}' not registered.")
        return cls(**kwargs)

    def list_plugins(self):
        return sorted(self._plugins.keys())


class Plugin:
    name = "base"

    def execute(self, **kwargs):
        raise NotImplementedError


class LogPlugin(Plugin):
    name = "LogPlugin"

    def execute(self, **kwargs):
        print(f"  [LOG] {kwargs.get('message', 'no message')}")


class EmailPlugin(Plugin):
    name = "EmailPlugin"

    def execute(self, **kwargs):
        print(f"  [EMAIL] to={kwargs.get('to')} subject={kwargs.get('subject')}")


class WebhookPlugin(Plugin):
    name = "WebhookPlugin"

    def execute(self, **kwargs):
        print(f"  [WEBHOOK] url={kwargs.get('url')} payload={kwargs.get('payload')}")


print("\n--- Plugin Registry ---")
# Reset singleton for demo
PluginRegistry._instance = None
registry = PluginRegistry()
registry.on_register(lambda name: print(f"  [EVENT] Plugin registered: {name}"))

registry.register("LogPlugin",     LogPlugin)
registry.register("EmailPlugin",   EmailPlugin)
registry.register("WebhookPlugin", WebhookPlugin)

print(f"\nRegistered plugins: {registry.list_plugins()}")

registry.create("LogPlugin").execute(message="Server started")
registry.create("EmailPlugin").execute(to="admin@site.com", subject="Alert")
registry.create("WebhookPlugin").execute(url="https://hooks.example.com", payload={"event": "deploy"})
