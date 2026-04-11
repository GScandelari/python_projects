# File Handling

Reading and writing files is one of the most common real-world tasks. Python makes it clean with the built-in `open()` function and the `with` statement, which guarantees files are always closed properly.

## Table of Contents

- [Opening Files — the `with` Statement](#1-opening-files--the-with-statement)
- [Reading Files](#2-reading-files)
- [Writing Files](#3-writing-files)
- [File Modes Reference](#4-file-modes-reference)
- [Working with CSV](#5-working-with-csv)
- [Working with JSON](#6-working-with-json)
- [pathlib — Modern Path Handling](#7-pathlib--modern-path-handling)
- [Common Patterns](#8-common-patterns)
- [Quick Reference](#quick-reference)
- [What's Next](#whats-next)

---

## 1. Opening Files — the `with` Statement

Always use `with open(...)` — it automatically closes the file even if an exception occurs.

```python
# Old way — risky if an exception is raised before close()
f = open("file.txt", "r")
content = f.read()
f.close()

# Correct way — file is closed automatically when the block exits
with open("file.txt", "r") as f:
    content = f.read()
# file is closed here, even if an error occurred inside the block
```

`open(path, mode, encoding)` — always specify encoding for text files:

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

---

## 2. Reading Files

### `read()` — entire file as one string

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()        # one big string
    print(len(content))       # total characters
```

### `readlines()` — list of lines (newlines included)

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()     # ['line 1\n', 'line 2\n', ...]
    lines = [l.rstrip() for l in lines]  # strip newlines
```

### Iterating line by line (most memory-efficient)

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:            # reads one line at a time
        print(line.rstrip())
```

### `readline()` — one line at a time

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    first = f.readline()      # 'line 1\n'
    second = f.readline()     # 'line 2\n'
```

---

## 3. Writing Files

### `"w"` — write (creates or overwrites)

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("Second line.\n")
```

### `"a"` — append (adds to end, never overwrites)

```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New log entry\n")
```

### `writelines()` — write a list of strings

```python
lines = ["line 1\n", "line 2\n", "line 3\n"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)       # no separator added — include \n yourself
```

---

## 4. File Modes Reference

| Mode | Meaning | Creates? | Overwrites? |
|---|---|---|---|
| `"r"` | Read text | No | — |
| `"w"` | Write text | Yes | Yes |
| `"a"` | Append text | Yes | No |
| `"r+"` | Read + write | No | No |
| `"x"` | Create (fails if exists) | Yes | — |
| `"rb"` | Read binary | No | — |
| `"wb"` | Write binary | Yes | Yes |

---

## 5. Working with CSV

The `csv` module handles comma-separated value files correctly (quotes, commas inside fields, etc.).

### Reading CSV

```python
import csv

with open("students.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)        # skip the header row
    for row in reader:
        name, grade = row[0], float(row[1])
        print(f"{name}: {grade}")
```

### Reading CSV as dicts (`DictReader`)

```python
import csv

with open("students.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)   # first row becomes keys
    for row in reader:
        print(row["name"], row["grade"])   # access by column name
```

### Writing CSV

```python
import csv

students = [
    ["Alice", 92],
    ["Bob", 78],
    ["Carol", 85],
]

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "grade"])    # header
    writer.writerows(students)            # all rows at once
```

### Writing CSV as dicts (`DictWriter`)

```python
import csv

students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob", "grade": 78},
]

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "grade"])
    writer.writeheader()
    writer.writerows(students)
```

---

## 6. Working with JSON

```python
import json

# Write JSON to file
data = {"name": "Alice", "scores": [90, 85, 92]}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# Read JSON from file
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(loaded["name"])   # Alice
```

> `json.dump` / `json.load` work with files.  
> `json.dumps` / `json.loads` work with strings.

---

## 7. pathlib — Modern Path Handling

`pathlib.Path` is the modern, object-oriented alternative to `os.path`.

```python
from pathlib import Path

p = Path("beginner") / "01-fundamentals" / "README.md"   # OS-aware join
print(p.exists())        # True / False
print(p.name)            # README.md
print(p.stem)            # README
print(p.suffix)          # .md
print(p.parent)          # beginner/01-fundamentals
print(p.resolve())       # absolute path

# Read and write directly
text = p.read_text(encoding="utf-8")
Path("copy.md").write_text(text, encoding="utf-8")

# List files
for f in Path(".").glob("**/*.py"):
    print(f)

# Create directories
Path("new/nested/folder").mkdir(parents=True, exist_ok=True)
```

---

## 8. Common Patterns

### Count lines, words, characters (like `wc`)

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

lines = content.splitlines()
words = content.split()
chars = len(content)
print(f"Lines: {len(lines)}, Words: {len(words)}, Chars: {chars}")
```

### Find and replace in a file

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("old_text", "new_text")

with open("file.txt", "w", encoding="utf-8") as f:
    f.write(content)
```

### Write a formatted report

```python
from datetime import datetime

report_lines = [
    f"Report generated: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n",
    f"{'Name':<20} {'Score':>6}\n",
    "-" * 28 + "\n",
]
for name, score in [("Alice", 92), ("Bob", 78)]:
    report_lines.append(f"{name:<20} {score:>6}\n")

with open("report.txt", "w", encoding="utf-8") as f:
    f.writelines(report_lines)
```

### Safe file write (write to temp, then rename)

```python
import os

def safe_write(path, content):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(content)
    os.replace(tmp, path)    # atomic on most OS
```

---

## Quick Reference

```python
# Read
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()           # full string
    lines = f.readlines()        # list of strings (with \n)
    for line in f: ...           # line by line (memory-efficient)

# Write
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("text\n")
    f.writelines(["a\n", "b\n"])

# Append
with open("file.txt", "a", encoding="utf-8") as f:
    f.write("new line\n")

# CSV
import csv
with open("data.csv", "r", newline="") as f:
    for row in csv.DictReader(f): ...

# JSON
import json
with open("data.json") as f: data = json.load(f)
with open("data.json", "w") as f: json.dump(data, f, indent=2)

# pathlib
from pathlib import Path
p = Path("folder") / "file.txt"
text = p.read_text(encoding="utf-8")
p.write_text("content", encoding="utf-8")
```

---

## What's Next

Try the exercises in [`exercises/`](./exercises/).

Next concept: [`04-error-handling`](../04-error-handling/)
