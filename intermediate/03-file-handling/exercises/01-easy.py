# ============================================================
# intermediate/03-file-handling/exercises/01-easy.py
# Topic: File Handling — open, read, write, append
# Difficulty: Easy
# ============================================================

import os

# All files created in these exercises go to this folder
EXERCISES_DIR = os.path.dirname(__file__)


# Exercise 1 — Write and Read a text file
# ----------------------------------------
# a) Write a file called "hello.txt" in EXERCISES_DIR with 3 lines:
#      "Hello, World!"
#      "This is a text file."
#      "Created with Python."
# b) Read it back and print each line (strip trailing whitespace)
#
# Expected output:
#   Hello, World!
#   This is a text file.
#   Created with Python.

# Write your code here


# Exercise 2 — Count lines, words, characters
# --------------------------------------------
# Read the file "hello.txt" you created above and print:
#   - Number of lines
#   - Number of words
#   - Number of characters (total, including spaces and newlines)
#
# Expected output:
#   Lines: 3
#   Words: 11
#   Chars: 57

# Write your code here


# Exercise 3 — Append to a file
# ------------------------------
# Append two more lines to "hello.txt":
#   "Python makes file handling easy."
#   "This line was appended."
# Then read the full file and print all 5 lines.
#
# Expected output (last 2 lines):
#   Python makes file handling easy.
#   This line was appended.

# Write your code here


# Exercise 4 — Find and Replace
# ------------------------------
# Read "hello.txt", replace every occurrence of the word "Python"
# with "🐍 Python" (or just "PYTHON" if you prefer no emoji),
# then overwrite the file with the updated content.
# Print the updated content to verify.

# Write your code here


# Exercise 5 — List .py files using pathlib
# ------------------------------------------
# Use pathlib.Path to:
#   a) Point to the EXERCISES_DIR directory
#   b) List all .py files in that directory (not recursive)
#   c) Print each filename (name only, not the full path)
#   d) Print the total count
#
# Expected output (approximate):
#   01-easy.py
#   02-medium.py
#   03-challenge.py
#   Total: 3 .py files

from pathlib import Path
# Write your code here
