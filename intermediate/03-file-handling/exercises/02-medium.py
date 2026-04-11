# ============================================================
# intermediate/03-file-handling/exercises/02-medium.py
# Topic: File Handling — CSV, JSON, pathlib, reports
# Difficulty: Medium
# ============================================================

import csv
import json
import os
from pathlib import Path

EXERCISES_DIR = Path(os.path.dirname(__file__))


# Exercise 1 — Write and Read a CSV file
# ----------------------------------------
# a) Create a CSV file "students.csv" with this data:
#    name,grade,city
#    Alice,92,São Paulo
#    Bob,78,Rio de Janeiro
#    Carol,85,Curitiba
#    Dave,91,Belo Horizonte
#    Eve,67,Fortaleza
#
# b) Read it back using csv.DictReader and print each student's
#    name and grade, plus whether they passed (grade >= 70).
#
# Expected:
#   Alice  | 92 | Pass
#   Bob    | 78 | Pass
#   Carol  | 85 | Pass
#   Dave   | 91 | Pass
#   Eve    | 67 | Fail

# Write your code here


# Exercise 2 — JSON Config File
# ------------------------------
# a) Create a "settings.json" file with:
#    { "theme": "light", "font_size": 12, "language": "pt-BR",
#      "autosave": true, "recent_files": [] }
# b) Load it, update "theme" to "dark" and "font_size" to 14,
#    add "notes.txt" to "recent_files"
# c) Save the updated config back to the same file
# d) Load again and print the final config in a readable format
#
# Expected final output:
#   theme       : dark
#   font_size   : 14
#   language    : pt-BR
#   autosave    : True
#   recent_files: ['notes.txt']

# Write your code here


# Exercise 3 — CSV Statistics Report
# ------------------------------------
# Read "students.csv" from Exercise 1 and compute:
#   - Class average (all grades)
#   - Highest grade and student name
#   - Lowest grade and student name
#   - Number of students who passed (>= 70)
# Write a text report to "report.txt" with this information.
# Then print the report to the console.
#
# Expected report format:
#   === CLASS REPORT ===
#   Students     : 5
#   Average grade: 82.6
#   Highest      : Alice — 92
#   Lowest       : Eve — 67
#   Passed       : 4 / 5

# Write your code here


# Exercise 4 — Log File
# ----------------------
# Simulate a simple logging system:
#   a) Write a function log(message, level="INFO") that appends
#      a line to "app.log" in the format:
#      [YYYY-MM-DD HH:MM:SS] [LEVEL] message
#   b) Call it 5 times with different levels (INFO, WARNING, ERROR)
#   c) Read "app.log" and print only the lines that contain "ERROR"
#
# Expected (ERROR lines only):
#   [2026-04-11 14:30:00] [ERROR] Something went wrong!

from datetime import datetime
# Write your code here


# Exercise 5 — Walk a directory tree with pathlib
# ------------------------------------------------
# Use pathlib.Path to walk the project root (go up from EXERCISES_DIR).
# Count and print:
#   - Total number of .py files in the entire project
#   - Total number of .md files
#   - Total number of .ipynb files
# Print a summary table.
#
# Expected (approximate):
#   .py files  : 42
#   .md files  : 18
#   .ipynb files: 9

# Write your code here
