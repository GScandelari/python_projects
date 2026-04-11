# Solutions Guide — 03-file-handling

---

## What Each Exercise Reinforces

### Easy 1 — Write and Read
**Concept:** `with open()` as the safe way to handle files.  
The `with` statement is a context manager — it guarantees `f.close()` is called even if an exception occurs inside the block. Without it, a crash mid-write could leave the file handle open.

### Easy 2 — Count lines/words/chars
**Concept:** Reading a file once and computing multiple stats.  
`splitlines()` handles `\n`, `\r\n`, and `\r` — more robust than `split("\n")`.

### Easy 3 — Append
**Concept:** `"a"` mode vs `"w"` mode.  
`"w"` truncates (destroys existing content). `"a"` seeks to end. For logs and accumulated data, always use `"a"`.

### Easy 4 — Find and Replace
**Concept:** Read → modify in memory → write back.  
Never open the same file for reading and writing at the same time in separate handles — race conditions can corrupt data.

### Easy 5 — pathlib.glob
**Concept:** `Path.glob()` with patterns.  
`"*.py"` matches current directory only. `"**/*.py"` matches recursively. `Path` objects are composable with `/`.

### Medium 1 — CSV with DictReader/DictWriter
**Concept:** Why `newline=""` is required.  
Without `newline=""`, the csv module on Windows adds extra blank rows because of `\r\n` handling. Always pass it.

### Medium 3 — Statistics from CSV
**Concept:** Process data from files into a report file.  
The pipeline: read CSV → compute stats → format strings → write report. Separating computation from I/O keeps functions testable.

### Medium 4 — Log File
**Concept:** Append-mode logging with timestamps.  
Using `datetime.now().strftime(...)` inside the log function means every entry is automatically timestamped at write time.

### Challenge 1 — CSV Merger
**Concept:** Using a dict as an accumulator while reading multiple files.  
Key insight: use the product name as the dict key, and accumulate units. When the same product appears twice, add — don't overwrite.

### Challenge 2 — JSON CRUD Database
**Concept:** File as a simple persistent store.  
Load → modify in memory → save back. This is the pattern behind many lightweight config systems. The `next_id` counter avoids ID reuse after deletion.

### Challenge 3 — Backup Utility
**Concept:** `datetime`-stamped filenames, `Path.mkdir(parents=True, exist_ok=True)`.  
`exist_ok=True` prevents errors if the directory already exists — safer than checking first.

---

## File Modes Quick Reference

| Mode | Creates | Overwrites | Position |
|---|---|---|---|
| `"r"` | No | — | Start |
| `"w"` | Yes | Yes | Start |
| `"a"` | Yes | No | End |
| `"r+"` | No | No | Start |
| `"x"` | Yes (fail if exists) | — | Start |
| `"rb"` / `"wb"` | — | — | Binary equivalents |

---

## Common Beginner Mistakes

### 1. Forgetting `encoding="utf-8"`
```python
# Bug: default encoding varies by OS — breaks with accented chars on Windows
with open("file.txt", "r") as f: ...

# Fix:
with open("file.txt", "r", encoding="utf-8") as f: ...
```

### 2. Using `"w"` when you meant `"a"`
```python
# Bug: destroys all previous content on each run
with open("log.txt", "w") as f:
    f.write("New entry\n")

# Fix for logs: use "a"
with open("log.txt", "a") as f:
    f.write("New entry\n")
```

### 3. Forgetting `newline=""` for CSV
```python
# Bug: extra blank rows on Windows
with open("data.csv", "w") as f:
    writer = csv.writer(f)

# Fix:
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
```

### 4. Reading a file that doesn't exist
```python
# Bug: FileNotFoundError crash
with open("missing.txt") as f: ...

# Fix: check first or handle the exception
from pathlib import Path
if Path("missing.txt").exists():
    with open("missing.txt") as f: ...
```

### 5. Modifying a list while building it from a file
```python
# Fine: process line by line — never hold the whole file in memory
with open("big_file.txt") as f:
    for line in f:
        process(line)   # memory-efficient streaming
```

### 6. `json.dump` vs `json.dumps` confusion
```python
json.dumps(data)          # → returns a string
json.dump(data, file)     # → writes to a file object (no 's')
json.loads(string)        # ← parses from a string
json.load(file)           # ← parses from a file object (no 's')
```
