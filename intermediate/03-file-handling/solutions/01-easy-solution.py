# ============================================================
# intermediate/03-file-handling/solutions/01-easy-solution.py
# ============================================================

import os
from pathlib import Path

EXERCISES_DIR = os.path.dirname(__file__)
HELLO_PATH = os.path.join(EXERCISES_DIR, "hello.txt")


print("=== Exercise 1 — Write and Read ===")
# APPROACH: Use 'with open(...)' so the file is always closed.
# 'w' creates or overwrites. Always specify encoding="utf-8".

with open(HELLO_PATH, "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("This is a text file.\n")
    f.write("Created with Python.\n")

with open(HELLO_PATH, "r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())


print("\n=== Exercise 2 — Count lines, words, chars ===")
# APPROACH: Read once into a string, then compute all stats.
# splitlines() handles different newline styles (\n, \r\n).

with open(HELLO_PATH, "r", encoding="utf-8") as f:
    content = f.read()

lines = content.splitlines()
words = content.split()
print(f"Lines: {len(lines)}")
print(f"Words: {len(words)}")
print(f"Chars: {len(content)}")


print("\n=== Exercise 3 — Append ===")
# APPROACH: 'a' mode adds to the end without touching existing content.

with open(HELLO_PATH, "a", encoding="utf-8") as f:
    f.write("Python makes file handling easy.\n")
    f.write("This line was appended.\n")

with open(HELLO_PATH, "r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())


print("\n=== Exercise 4 — Find and Replace ===")
# APPROACH: Read → modify in memory → write back.
# Never write while reading — use two separate 'with' blocks.

with open(HELLO_PATH, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("Python", "PYTHON")

with open(HELLO_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(content)


print("\n=== Exercise 5 — List .py files with pathlib ===")
# APPROACH: Path.glob("*.py") matches files in the current dir only.
# Use "**/*.py" for recursive. Sort for consistent order.

exercises_path = Path(os.path.dirname(__file__))
py_files = sorted(exercises_path.glob("*.py"))

for f in py_files:
    print(f.name)

print(f"Total: {len(py_files)} .py files")
