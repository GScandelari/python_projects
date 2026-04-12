"""
NumPy — Medium Exercises
========================
Topics: broadcasting, reshape, aggregations, fancy indexing, np.where.

Run:  python 02-medium.py
"""

import numpy as np

np.random.seed(42)


# ---------------------------------------------------------------------------
# 1. Reshape and flatten
# ---------------------------------------------------------------------------
# a) Create np.arange(24) and reshape it into shape (4, 6).
# b) From that matrix, reshape it into (2, 3, 4) — 3-D tensor.
# c) Flatten the 3-D tensor back to 1-D.
# d) Print the shape at each step.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. Aggregations with axis
# ---------------------------------------------------------------------------
# Given the matrix below, compute and print:
# a) Sum of all elements.
# b) Sum of each column (result shape: (4,)).
# c) Mean of each row (result shape: (3,)).
# d) Index of the maximum element in the entire matrix (np.argmax).
# e) Maximum value in each column.

scores = np.array([
    [85, 92, 78, 90],
    [70, 65, 88, 74],
    [95, 80, 91, 85],
])

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. Broadcasting
# ---------------------------------------------------------------------------
# a) Given a (4, 3) matrix of random integers [0, 100), subtract the
#    column mean from each element (zero-centre the columns).
#    Hint: mean shape should be (3,) — use axis=0.
#
# b) Given a (3,) array of weights [0.2, 0.3, 0.5], compute the weighted
#    sum of each row of the matrix below.

m = np.random.randint(0, 100, (4, 3))
weights = np.array([0.2, 0.3, 0.5])

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. np.where
# ---------------------------------------------------------------------------
# a) Given the array below, use np.where to replace negatives with 0
#    and positives with 1 (keep 0 as 0).
#
# b) Use np.where on the matrix below to create a same-shape matrix
#    where values above 50 become "high" and others "low" (strings).

arr = np.array([-3, 0, 7, -1, 4, 0, -9, 2])

mat = np.array([
    [20, 80, 45],
    [60, 10, 75],
    [55, 30, 90],
])

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 5. Sorting and searching
# ---------------------------------------------------------------------------
# Given the array below:
# a) Return a sorted copy (ascending).
# b) Return the indices that would sort the array (np.argsort).
# c) Find the 3 largest values without fully sorting (np.partition).

data = np.array([34, 7, 23, 32, 5, 62, 14, 43, 1, 88])

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 6. Stack and split
# ---------------------------------------------------------------------------
# a) Stack a = np.arange(5) and b = np.arange(5, 10) vertically
#    (result shape (2, 5)) and horizontally (result shape (10,)).
#
# b) Split the (4, 6) matrix below into two equal halves along axis=1.
#    Each half should have shape (4, 3).

a = np.arange(5)
b = np.arange(5, 10)
m6 = np.arange(24).reshape(4, 6)

# YOUR CODE HERE
