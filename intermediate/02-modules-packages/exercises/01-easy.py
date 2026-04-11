# ============================================================
# intermediate/02-modules-packages/exercises/01-easy.py
# Topic: Built-in modules — math, random, datetime, os
# Difficulty: Easy
# ============================================================

# Exercise 1 — math module
# ------------------------
# Import the math module and use it to:
#   a) Print pi rounded to 5 decimal places
#   b) Print the square root of 256
#   c) Print the ceiling of 7.2 and the floor of 7.8
#   d) Print 2 raised to the power of 16 using math.pow
#   e) Print the factorial of 10
#
# Expected:
#   pi = 3.14159
#   sqrt(256) = 16.0
#   ceil(7.2) = 8 | floor(7.8) = 7
#   2^16 = 65536.0
#   10! = 3628800

# Write your code here


# Exercise 2 — random module
# --------------------------
# Import random and:
#   a) Set the seed to 99 (for reproducibility)
#   b) Print a random integer between 1 and 100
#   c) Print a random choice from the list ["rock", "paper", "scissors"]
#   d) Print a sorted list of 5 unique random integers between 1 and 50
#   e) Create a list [1..10], shuffle it, and print the result
#
# (With seed=99, your first randint result should be consistent)

# Write your code here


# Exercise 3 — datetime module
# ----------------------------
# From datetime import date, datetime, and timedelta, then:
#   a) Print today's date in the format DD/MM/YYYY
#   b) Print the current day of the week (e.g. "Friday")
#   c) Print the date 100 days from today
#   d) Calculate and print how many days remain until January 1st, 2027
#
# Expected (approximate, depends on run date):
#   Today: 11/04/2026
#   Day: Saturday
#   In 100 days: 20/07/2026
#   Days until 2027: 265

# Write your code here


# Exercise 4 — os module
# ----------------------
# Import os and:
#   a) Print the current working directory
#   b) Print only the .py files in the current directory (use os.listdir)
#   c) Build and print a path using os.path.join for:
#      ["projects", "python", "exercises", "01-easy.py"]
#   d) Check if a file called "README.md" exists one level up (hint: "..")
#      and print True or False
#
# Expected:
#   cwd: C:\...\exercises
#   .py files: ['01-easy.py', '02-medium.py', '03-challenge.py']
#   path: projects/python/exercises/01-easy.py
#   README exists: True

# Write your code here


# Exercise 5 — json module
# ------------------------
# Import json and:
#   a) Create a dict with keys: "name", "language", "level", "topics" (list)
#   b) Convert it to a JSON string with indent=2 and print it
#   c) Parse the JSON string back to a Python dict and print the "topics" list
#
# Expected:
#   {
#     "name": "Python Projects",
#     "language": "Python",
#     "level": "intermediate",
#     "topics": ["modules", "packages", "imports"]
#   }
#   Topics: ['modules', 'packages', 'imports']

# Write your code here
