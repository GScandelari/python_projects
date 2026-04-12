"""
NumPy — Medium Solutions
"""

import numpy as np

np.random.seed(42)


# ---------------------------------------------------------------------------
# 1. Reshape and flatten
# ---------------------------------------------------------------------------
a = np.arange(24)
m4x6 = a.reshape(4, 6)
print(m4x6.shape)        # (4, 6)

m2x3x4 = m4x6.reshape(2, 3, 4)
print(m2x3x4.shape)      # (2, 3, 4)

flat = m2x3x4.flatten()
print(flat.shape)        # (24,)


# ---------------------------------------------------------------------------
# 2. Aggregations with axis
# ---------------------------------------------------------------------------
scores = np.array([
    [85, 92, 78, 90],
    [70, 65, 88, 74],
    [95, 80, 91, 85],
])

print(scores.sum())              # 993
print(scores.sum(axis=0))        # [250 237 257 249]
print(scores.mean(axis=1))       # [86.25  74.25  87.75]
print(np.argmax(scores))         # 8  (index of 95 in flattened)
print(scores.max(axis=0))        # [95 92 91 90]


# ---------------------------------------------------------------------------
# 3. Broadcasting
# ---------------------------------------------------------------------------
m = np.random.randint(0, 100, (4, 3))
col_means = m.mean(axis=0)           # shape (3,)
m_centered = m - col_means           # broadcast across rows
print(m_centered.mean(axis=0))       # ~[0. 0. 0.]

weights = np.array([0.2, 0.3, 0.5])
mat = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
weighted_sums = (mat * weights).sum(axis=1)
print(weighted_sums)                 # [23. 53. 83.]


# ---------------------------------------------------------------------------
# 4. np.where
# ---------------------------------------------------------------------------
arr = np.array([-3, 0, 7, -1, 4, 0, -9, 2])
result = np.where(arr > 0, 1, np.where(arr == 0, 0, 0))
print(result)     # [0 0 1 0 1 0 0 1]  (negative→0, positive→1, zero→0)

mat = np.array([[20, 80, 45], [60, 10, 75], [55, 30, 90]])
labels = np.where(mat > 50, 'high', 'low')
print(labels)


# ---------------------------------------------------------------------------
# 5. Sorting and searching
# ---------------------------------------------------------------------------
data = np.array([34, 7, 23, 32, 5, 62, 14, 43, 1, 88])
print(np.sort(data))           # [ 1  5  7 14 23 32 34 43 62 88]
print(np.argsort(data))        # [8 4 1 6 2 3 0 7 5 9]

# 3 largest: partition puts 3 largest in last 3 positions
top3 = np.partition(data, -3)[-3:]
print(np.sort(top3)[::-1])    # [88 62 43]


# ---------------------------------------------------------------------------
# 6. Stack and split
# ---------------------------------------------------------------------------
a = np.arange(5)
b = np.arange(5, 10)
print(np.vstack([a, b]))           # shape (2, 5)
print(np.hstack([a, b]))           # shape (10,)

m6 = np.arange(24).reshape(4, 6)
left, right = np.split(m6, 2, axis=1)
print(left.shape, right.shape)     # (4, 3) (4, 3)
