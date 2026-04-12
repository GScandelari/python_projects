"""
NumPy — Easy Exercises
======================
Topics: array creation, indexing, slicing, vectorised operations.

Run:  python 01-easy.py
"""

import numpy as np


# ---------------------------------------------------------------------------
# 1. Array basics
# ---------------------------------------------------------------------------
# a) Create a 1-D array of integers from 1 to 10 (inclusive).
# b) Print its shape, dtype, and size.
# c) Print the last element using negative indexing.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. Array creation functions
# ---------------------------------------------------------------------------
# Create and print:
# a) A 3×3 matrix of zeros (float64).
# b) A 4×4 identity matrix.
# c) 6 evenly spaced values between 0 and 1 (inclusive).
# d) An array [0, 5, 10, 15, 20] using np.arange.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. Slicing
# ---------------------------------------------------------------------------
# Given the array below, extract and print:
# a) The first three elements.
# b) Every other element (step 2).
# c) The subarray [30, 40, 50] using a slice.

data = np.array([10, 20, 30, 40, 50, 60, 70])

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. 2-D indexing
# ---------------------------------------------------------------------------
# Given the matrix below:
# a) Print the element at row 1, column 2.
# b) Print the entire second row.
# c) Print the third column as a 1-D array.
# d) Print the 2×2 submatrix in the bottom-right corner.

matrix = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
])

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 5. Vectorised operations
# ---------------------------------------------------------------------------
# a) Given a = np.array([1, 2, 3, 4, 5]), compute and print:
#    - a squared (element-wise)
#    - square root of a
#    - a multiplied by 3
#
# b) Given two arrays a and b below, compute:
#    - their element-wise sum
#    - their element-wise product
#    - the dot product (hint: np.dot or @)

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 6. Boolean indexing
# ---------------------------------------------------------------------------
# Given the array below:
# a) Print all values greater than 30.
# b) Print all even values.
# c) Replace all negative values with 0 (modify in place).

values = np.array([15, -3, 42, 7, -18, 56, 0, -1, 33])

# YOUR CODE HERE
