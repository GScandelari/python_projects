"""
NumPy — Challenge Exercises
============================
Topics: linear algebra, statistics, vectorised algorithms, performance.

Run:  python 03-challenge.py
"""

import numpy as np
import time

np.random.seed(0)


# ---------------------------------------------------------------------------
# 1. Linear algebra
# ---------------------------------------------------------------------------
# Given the system of equations:
#   2x + 3y =  8
#   5x -  y = -2
#
# a) Express as Ax = b and solve with np.linalg.solve.
# b) Verify by computing A @ solution and comparing with b.
# c) Compute the determinant and inverse of A.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. Normalisation
# ---------------------------------------------------------------------------
# Implement min-max normalisation:
#   normalised = (x - x_min) / (x_max - x_min)
#
# a) Apply it to the entire matrix (global min/max).
# b) Apply it column-wise (each column in [0, 1] independently).
# c) Implement z-score normalisation column-wise:
#       z = (x - mean) / std

data = np.random.randn(100, 4) * np.array([10, 5, 20, 2]) + np.array([50, 100, -10, 0])

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. Moving average
# ---------------------------------------------------------------------------
# Implement a function moving_average(arr, window) that computes
# the sliding window mean without using any loop.
# Hint: use np.cumsum with the offset trick.
#
# Example:
#   moving_average(np.array([1,2,3,4,5,6]), 3)
#   → [2.0, 3.0, 4.0, 5.0]

def moving_average(arr, window):
    # YOUR CODE HERE
    pass

signal = np.array([1.0, 3.0, 5.0, 2.0, 8.0, 6.0, 4.0, 7.0])
print(moving_average(signal, 3))   # [3.0, 3.33, 5.0, 5.33, 6.0, 5.67]


# ---------------------------------------------------------------------------
# 4. Correlation matrix
# ---------------------------------------------------------------------------
# Given a dataset with 3 features (columns), compute the Pearson correlation
# matrix without using np.corrcoef — only np.std, np.mean, and @ operator.
#
# Formula: corr(i, j) = cov(i, j) / (std_i * std_j)
# where cov(X) = (X_centered.T @ X_centered) / (n - 1)
#
# Validate your result against np.corrcoef(dataset.T).

dataset = np.random.randn(50, 3)

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 5. Pure NumPy k-nearest neighbours (1-D)
# ---------------------------------------------------------------------------
# Given a 1-D array of points and a query value, find the k nearest points
# using only NumPy (no loops).
#
# Implement: nearest_k(points, query, k) → sorted array of k nearest values

def nearest_k(points, query, k):
    # YOUR CODE HERE
    pass

points = np.array([3.5, 1.2, 7.8, 4.1, 9.0, 2.3, 6.6])
print(nearest_k(points, 5.0, 3))   # [4.1, 6.6, 3.5]


# ---------------------------------------------------------------------------
# 6. Performance: loop vs vectorised
# ---------------------------------------------------------------------------
# Compute the sum of squares for 10 million numbers.
# Compare:
#   a) Python list comprehension
#   b) NumPy vectorised
# Print both results and both execution times.

n = 10_000_000

start = time.perf_counter()
result_py = sum(i ** 2 for i in range(n))
py_time = time.perf_counter() - start

# YOUR CODE HERE — NumPy version

print(f'Python: {result_py}  ({py_time:.3f}s)')
# print(f'NumPy:  {result_np}  ({np_time:.3f}s)')
