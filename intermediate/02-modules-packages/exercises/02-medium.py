# ============================================================
# intermediate/02-modules-packages/exercises/02-medium.py
# Topic: Modules — practical combinations of built-ins
# Difficulty: Medium
# ============================================================

# Exercise 1 — Dice Roller with Statistics
# ----------------------------------------
# Using the random module, simulate rolling two 6-sided dice
# 1000 times. Track how many times each possible sum (2–12) occurs.
# Print a frequency table showing the count and a bar of '#' symbols
# proportional to the count (each '#' = 10 rolls).
#
# Expected output (approximate):
#    2:  28  ###
#    3:  57  #####
#    7: 167  ################
#   12:  28  ###

import random
# Write your code here


# Exercise 2 — Birthday Countdown
# --------------------------------
# Ask the user for their birthday in the format DD/MM (e.g. 25/12).
# Calculate and print:
#   a) Their next birthday date (this year or next if already passed)
#   b) How many days until their next birthday
#   c) What day of the week it falls on
#
# Expected:
#   Enter your birthday (DD/MM): 25/12
#   Next birthday: 25/12/2026
#   Days until birthday: 258
#   Day of the week: Friday

from datetime import date, datetime, timedelta
# Write your code here


# Exercise 3 — Directory Explorer
# ---------------------------------
# Using os and os.path, write code that:
#   a) Starts from the current file's directory (use __file__ and os.path.dirname)
#   b) Goes up two levels to the project root
#   c) Walks the "beginner" folder and prints a tree like:
#      beginner/
#        01-fundamentals/
#          README.md
#          notebook.ipynb
#          exercises/
#          solutions/
# Print only files and folders (skip .gitkeep files).
# Use os.walk or os.scandir for traversal.

import os
# Write your code here


# Exercise 4 — Config File with JSON
# ------------------------------------
# Simulate a simple app configuration system:
#   a) Define a default config dict with keys:
#      "theme", "font_size", "language", "notifications" (bool)
#   b) Save it to "config.json" in the current directory
#   c) Load it back, update "theme" to "dark" and "font_size" to 16
#   d) Save the updated config back to the file
#   e) Load and print the final config in a formatted way
#
# Expected final output:
#   theme        : dark
#   font_size    : 16
#   language     : en
#   notifications: True

import json
import os
# Write your code here


# Exercise 5 — Module Inspection
# --------------------------------
# Use dir() and help() (or .__doc__) to explore built-in modules:
#   a) Print all names in the `math` module that start with a lowercase letter
#   b) Print the first line of the docstring for math.log
#   c) Print all names in `random` that contain the word "int"
#   d) Print the Python version from sys.version (first line only)

import math
import random
import sys
# Write your code here
