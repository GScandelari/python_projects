"""
Pandas — Easy Exercises
=======================
Topics: Series, DataFrame creation, indexing, filtering, basic operations.

Run:  python 01-easy.py
"""

import pandas as pd


# ---------------------------------------------------------------------------
# 1. Series basics
# ---------------------------------------------------------------------------
# a) Create a Series of monthly temperatures (°C) for Jan–Jun:
#    [22, 25, 28, 30, 27, 24]
#    Use the month names as the index.
# b) Print the temperature for March and May.
# c) Print all months where the temperature is above 26°C.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. DataFrame creation
# ---------------------------------------------------------------------------
# Create a DataFrame from the data below and print:
# a) The first 3 rows.
# b) The shape.
# c) The column names.
# d) The data types of each column.

students_data = {
    'name':    ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'age':     [20, 22, 21, 23, 20],
    'grade':   [88, 74, 92, 65, 79],
    'passed':  [True, True, True, False, True],
}

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. Column selection and row slicing
# ---------------------------------------------------------------------------
# Using the DataFrame from exercise 2:
# a) Select only the 'name' and 'grade' columns.
# b) Select rows at positions 1, 2, and 3 (iloc).
# c) Select the row where name == 'Carol' using loc with a boolean mask.
# d) Print the grade of the student named 'David'.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. Filtering
# ---------------------------------------------------------------------------
# Using the DataFrame from exercise 2:
# a) Filter students with grade >= 80.
# b) Filter students who passed AND are older than 20.
# c) Filter students whose name starts with a vowel (A or E).

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 5. Basic operations
# ---------------------------------------------------------------------------
# Using the DataFrame from exercise 2:
# a) Add a new column 'letter_grade':
#    grade >= 90 → 'A', grade >= 80 → 'B', grade >= 70 → 'C', else → 'F'
#    (use pd.cut or apply — your choice)
# b) Compute the average grade (mean).
# c) Sort by grade descending and print the result.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 6. describe and value_counts
# ---------------------------------------------------------------------------
# Using the DataFrame from exercise 2:
# a) Print the statistical summary of numeric columns (describe).
# b) Print how many students have each letter_grade (value_counts).

# YOUR CODE HERE
