# NumPy — Solution Notes

## Easy

**Array creation:** `np.arange(1, 11)` generates integers 1–10. Always inspect `.shape`, `.dtype`, `.size` when working with a new array.

**Slicing:** NumPy slicing follows the same `[start:stop:step]` convention as Python lists but works on N dimensions: `arr[row_slice, col_slice]`.

**Boolean indexing:** `arr[arr > 0]` returns a copy. Assigning back (`arr[arr < 0] = 0`) modifies in place.

## Medium

**Reshape:** `reshape` returns a **view** when possible (same memory). `flatten()` always returns a **copy**. Use `ravel()` when you want a 1-D view.

**Axis semantics:** `axis=0` collapses rows (result has one value per column). `axis=1` collapses columns (result has one value per row). Think "collapse along this axis".

**Broadcasting rules:** align shapes from the right — missing or size-1 dimensions are stretched. Always check shapes before broadcasting to avoid silent bugs.

**np.where:** `np.where(cond, a, b)` is the vectorised ternary. When `a` and `b` are arrays, they must broadcast with `cond`.

**np.partition:** O(n) time for finding the k largest/smallest values vs O(n log n) for full sort. Use it when you only need top-k.

## Challenge

**Linear algebra:** `np.linalg.solve(A, b)` is more numerically stable than `inv(A) @ b`. Always verify with `np.allclose`.

**Z-score (ddof):** `np.std(ddof=1)` uses the unbiased sample standard deviation (divides by n-1). `ddof=0` (default) gives population std (divides by n). Use `ddof=1` when normalising a sample.

**Moving average trick:**
```python
cs = np.cumsum(arr)
cs[w:] = cs[w:] - cs[:-w]
result = cs[w-1:] / w
```
This is O(n) and avoids loops entirely. The key insight: `sum(arr[i:i+w]) = cumsum[i+w-1] - cumsum[i-1]`.

**Correlation from scratch:**
```
corr(i,j) = cov(i,j) / (std_i * std_j)
```
Using `np.outer(std, std)` to compute the denominator matrix in one shot.

**k-NN with argpartition:** `np.argpartition(dists, k)[:k]` finds the k smallest distances in O(n) time — faster than sorting all n distances.

**Performance:** NumPy operations run in compiled C code. Expect 10–100× speedups over pure Python loops for large arrays, primarily because:
1. No Python object overhead per element.
2. Contiguous memory (cache-friendly).
3. SIMD vectorisation at the CPU level.
