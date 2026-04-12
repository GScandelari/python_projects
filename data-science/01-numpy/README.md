# NumPy

Fast numerical computing with N-dimensional arrays.

**Install:** `pip install numpy`

**Import convention:** `import numpy as np`

---

## 1. Arrays and dtypes

NumPy's core is `ndarray` — a fixed-type, fixed-size N-dimensional array.

```python
import numpy as np

a = np.array([1, 2, 3])          # 1-D, dtype=int64
b = np.array([1.0, 2.0, 3.0])   # 1-D, dtype=float64
m = np.array([[1, 2], [3, 4]])   # 2-D (matrix)

print(a.shape)    # (3,)
print(m.shape)    # (2, 2)
print(m.dtype)    # int64
print(m.ndim)     # 2
print(m.size)     # 4
```

## 2. Array Creation

```python
np.zeros((3, 4))              # all zeros, float64
np.ones((2, 3), dtype=int)    # all ones, int
np.eye(3)                     # 3×3 identity matrix
np.arange(0, 10, 2)           # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)          # 5 evenly spaced points 0→1
np.full((2, 2), 7)            # fill with constant
np.random.rand(3, 3)          # uniform [0, 1)
np.random.randn(3, 3)         # standard normal
np.random.randint(0, 10, (3, 3))  # random ints
```

## 3. Indexing and Slicing

```python
a = np.array([10, 20, 30, 40, 50])
a[0]       # 10
a[-1]      # 50
a[1:4]     # [20, 30, 40]
a[::2]     # [10, 30, 50]

m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

m[0, 1]    # 2  (row 0, col 1)
m[1:, :2]  # [[4, 5], [7, 8]]
m[:, 1]    # [2, 5, 8]  column 1

# Boolean indexing
a[a > 25]       # [30, 40, 50]
a[a % 2 == 0]   # [20, 40]
```

## 4. Vectorised Operations

Operations apply element-wise — no loops needed.

```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

a + b       # [11, 22, 33, 44]
a * b       # [10, 40, 90, 160]
a ** 2      # [1, 4, 9, 16]
np.sqrt(a)  # element-wise square root
np.sin(a)   # element-wise sine
np.log(a)   # element-wise natural log
```

## 5. Broadcasting

NumPy can operate on arrays of different shapes by "stretching" the smaller one.

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])   # shape (2, 3)

row = np.array([10, 20, 30])    # shape (3,) → broadcast across rows
a + row   # [[11, 22, 33], [14, 25, 36]]

col = np.array([[100], [200]])  # shape (2, 1) → broadcast across cols
a + col   # [[101, 102, 103], [204, 205, 206]]
```

**Rule:** Two dimensions are compatible when they are equal or one of them is 1.

## 6. Shape Manipulation

```python
a = np.arange(12)
m = a.reshape(3, 4)             # view — same data, new shape
m.flatten()                     # copy → 1-D
m.ravel()                       # view → 1-D (when possible)
m.T                             # transpose
np.concatenate([m, m], axis=0)  # stack vertically
np.vstack([m, m])               # same as axis=0
np.hstack([m, m])               # stack horizontally
```

## 7. Aggregations

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])

a.sum()          # 21 — all elements
a.sum(axis=0)    # [5, 7, 9] — column sums
a.sum(axis=1)    # [6, 15] — row sums
a.mean()         # 3.5
a.std()          # standard deviation
a.min(), a.max()
a.argmin()       # flat index of minimum
np.cumsum(a)     # cumulative sum (flattened)
np.sort(a, axis=1)  # sort each row
```

## 8. Linear Algebra

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

A @ B                    # matrix multiplication
np.linalg.det(A)         # determinant
np.linalg.inv(A)         # inverse
np.linalg.eig(A)         # eigenvalues and eigenvectors
np.linalg.solve(A, b)    # solve Ax = b
```

---

## Quick Reference

```python
# Creation
np.zeros / np.ones / np.eye / np.full
np.arange / np.linspace / np.random.rand / np.random.randn

# Inspection
arr.shape / arr.dtype / arr.ndim / arr.size

# Indexing
arr[i, j]  /  arr[1:3, ::2]  /  arr[arr > 0]

# Transformation
arr.reshape() / arr.flatten() / arr.T
np.concatenate / np.vstack / np.hstack

# Math
arr + arr / arr * scalar  # vectorised
arr @ arr                 # matrix multiply
arr.sum / arr.mean / arr.std / arr.min / arr.max
```

## Practice

| File | Difficulty | Topics |
|---|---|---|
| [01-easy.py](exercises/01-easy.py) | Easy | Array creation, indexing, vectorised ops |
| [02-medium.py](exercises/02-medium.py) | Medium | Broadcasting, reshape, aggregations |
| [03-challenge.py](exercises/03-challenge.py) | Challenge | Linear algebra, statistics, performance |

Solutions: [solutions/](solutions/)
