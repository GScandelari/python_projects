"""
Automation — Easy Exercises
============================
Topics: pathlib basics, shutil, CSV read/write, JSON read/write.

Run:  python 01-easy.py
"""

from pathlib import Path
import shutil
import csv
import json


# ---------------------------------------------------------------------------
# 1. pathlib basics
# ---------------------------------------------------------------------------
# a) Print the current working directory (Path.cwd()).
# b) List all .py files in the current directory (non-recursive).
# c) Create a directory called 'sandbox' inside the current directory.
#    Use exist_ok=True so it doesn't fail if it already exists.
# d) Print the name, suffix, and parent of Path('reports/2024/summary.csv').

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. Read and write text files
# ---------------------------------------------------------------------------
# a) Write the string below to 'sandbox/hello.txt':
#    "Hello from Python!\nLine 2\nLine 3"
#
# b) Read it back and print each line with its line number:
#    1: Hello from Python!
#    2: Line 2
#    3: Line 3
#
# c) Append a fourth line "Line 4" to the file (open in append mode).
# d) Print the total number of lines after appending.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. Copy and move files
# ---------------------------------------------------------------------------
# a) Copy 'sandbox/hello.txt' to 'sandbox/hello_backup.txt'.
# b) Create a subdirectory 'sandbox/archive/'.
# c) Move 'sandbox/hello_backup.txt' into 'sandbox/archive/'.
# d) List all files in 'sandbox/' recursively (glob **/*) and print them.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. CSV read and write
# ---------------------------------------------------------------------------
# a) Write the following data to 'sandbox/students.csv':
STUDENTS = [
    {'name': 'Alice', 'age': 20, 'grade': 'A'},
    {'name': 'Bob',   'age': 22, 'grade': 'B'},
    {'name': 'Carol', 'age': 21, 'grade': 'A'},
    {'name': 'David', 'age': 23, 'grade': 'C'},
]
# b) Read it back and print only the students with grade 'A'.
# c) Print the average age.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 5. JSON read and write
# ---------------------------------------------------------------------------
# a) Write the CONFIG dict below to 'sandbox/config.json' (indent=2).
CONFIG = {
    'app': 'MyApp',
    'version': '2.1.0',
    'debug': False,
    'database': {'host': 'localhost', 'port': 5432},
    'allowed_hosts': ['127.0.0.1', 'localhost'],
}
# b) Read it back and print the database host and port.
# c) Update the version to '2.2.0' and save back to the file.
# d) Verify by reading again and printing the version.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 6. Cleanup
# ---------------------------------------------------------------------------
# Remove the entire 'sandbox' directory and everything inside it.

# YOUR CODE HERE
