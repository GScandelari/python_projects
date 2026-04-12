"""
NumPy — Challenge Solutions
"""

import numpy as np
import time

np.random.seed(0)


# ---------------------------------------------------------------------------
# 1. Linear algebra
# ---------------------------------------------------------------------------
A = np.array([[2, 3], [5, -1]], dtype=float)
b = np.array([8, -2], dtype=float)

solution = np.linalg.solve(A, b)
print(f'x={solution[0]:.4f}, y={solution[1]:.4f}')   # x=0.4545, y=2.3636

# Verify
print(np.allclose(A @ solution, b))   # True

print(f'det(A) = {np.linalg.det(A):.4f}')   # -17.0
print(np.linalg.inv(A))


# ---------------------------------------------------------------------------
# 2. Normalisation
# ---------------------------------------------------------------------------
data = np.random.randn(100, 4) * np.array([10, 5, 20, 2]) + np.array([50, 100, -10, 0])

# a) Global min-max
gmin, gmax = data.min(), data.max()
normalised_global = (data - gmin) / (gmax - gmin)

# b) Column-wise min-max
cmin = data.min(axis=0)  # shape (4,)
cmax = data.max(axis=0)
normalised_col = (data - cmin) / (cmax - cmin)
print(normalised_col.min(axis=0))   # [0. 0. 0. 0.]
print(normalised_col.max(axis=0))   # [1. 1. 1. 1.]

# c) Z-score column-wise
z = (data - data.mean(axis=0)) / data.std(axis=0)
print(z.mean(axis=0).round(10))    # ~[0. 0. 0. 0.]
print(z.std(axis=0).round(10))     # ~[1. 1. 1. 1.]


# ---------------------------------------------------------------------------
# 3. Moving average
# ---------------------------------------------------------------------------
def moving_average(arr, window):
    cs = np.cumsum(arr)
    cs[window:] = cs[window:] - cs[:-window]
    return cs[window - 1:] / window

signal = np.array([1.0, 3.0, 5.0, 2.0, 8.0, 6.0, 4.0, 7.0])
print(moving_average(signal, 3).round(2))
# [3.   3.33 5.   5.33 6.   5.67]


# ---------------------------------------------------------------------------
# 4. Correlation matrix
# ---------------------------------------------------------------------------
dataset = np.random.randn(50, 3)

# Centre
X = dataset - dataset.mean(axis=0)
# Covariance matrix
cov = (X.T @ X) / (len(X) - 1)
# Standard deviations
std = dataset.std(axis=0, ddof=1)
# Correlation
corr = cov / np.outer(std, std)
print(corr.round(4))

# Validate
print(np.allclose(corr, np.corrcoef(dataset.T)))   # True


# ---------------------------------------------------------------------------
# 5. Pure NumPy k-nearest neighbours (1-D)
# ---------------------------------------------------------------------------
def nearest_k(points, query, k):
    dists = np.abs(points - query)
    idx = np.argpartition(dists, k)[:k]
    return points[idx[np.argsort(dists[idx])]]

points = np.array([3.5, 1.2, 7.8, 4.1, 9.0, 2.3, 6.6])
print(nearest_k(points, 5.0, 3))   # [4.1 6.6 3.5]


# ---------------------------------------------------------------------------
# 6. Performance: loop vs vectorised
# ---------------------------------------------------------------------------
n = 10_000_000

start = time.perf_counter()
result_py = sum(i ** 2 for i in range(n))
py_time = time.perf_counter() - start

start = time.perf_counter()
result_np = np.arange(n, dtype=np.int64) ** 2
result_np = result_np.sum()
np_time = time.perf_counter() - start

print(f'Python: {result_py}  ({py_time:.3f}s)')
print(f'NumPy:  {result_np}  ({np_time:.3f}s)')
print(f'Speedup: {py_time / np_time:.1f}x')
