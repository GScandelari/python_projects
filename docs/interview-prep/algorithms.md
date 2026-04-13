# Algorithms & Data Structures — Interview Reference

## Big-O Complexity

### Common Complexities (best → worst)

| Notation | Name | Example |
|---|---|---|
| O(1) | Constant | Dict lookup, list index |
| O(log n) | Logarithmic | Binary search, balanced BST |
| O(n) | Linear | Linear search, single loop |
| O(n log n) | Linearithmic | Merge sort, Timsort |
| O(n²) | Quadratic | Bubble/insertion sort, nested loops |
| O(2ⁿ) | Exponential | Recursive subset enumeration |
| O(n!) | Factorial | Brute-force permutations |

### Python Built-in Complexities

| Operation | list | dict / set |
|---|---|---|
| Index `l[i]` | O(1) | — |
| Append | O(1) amortised | — |
| Insert at index | O(n) | — |
| `in` / lookup | O(n) | O(1) average |
| Delete by index | O(n) | — |
| Delete by key | — | O(1) average |
| `len()` | O(1) | O(1) |
| Sort | O(n log n) | — |

---

## Sorting Algorithms

### Quick reference

| Algorithm | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| Bubble sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Insertion sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Timsort (Python) | O(n) | O(n log n) | O(n log n) | O(n) | Yes |

### Merge Sort

```python
def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]
```

### Quick Sort

```python
def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

---

## Searching

### Binary Search — O(log n)

Requires sorted input.

```python
def binary_search(arr: list, target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# Python built-in: bisect module
import bisect
bisect.bisect_left([1, 3, 5, 7], 5)   # 2 (insertion point)
```

---

## Data Structures

### Stack — LIFO

```python
# Use a list (O(1) push/pop at end)
stack = []
stack.append(1)   # push
stack.append(2)
stack.pop()       # 2 — pop
stack[-1]         # peek

# Thread-safe alternative
from collections import deque
stack = deque()
stack.append(1)
stack.pop()
```

### Queue — FIFO

```python
from collections import deque

q = deque()
q.append('a')    # enqueue
q.append('b')
q.popleft()      # 'a' — dequeue

# Priority queue (min-heap)
import heapq
pq = []
heapq.heappush(pq, (2, 'task-B'))
heapq.heappush(pq, (1, 'task-A'))
heapq.heappop(pq)   # (1, 'task-A')
```

### Linked List

```python
class Node:
    def __init__(self, val, next=None):
        self.val  = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, val):
        self.head = Node(val, self.head)

    def to_list(self):
        result, cur = [], self.head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result
```

### Hash Map (dict) — Key patterns

```python
from collections import defaultdict, Counter

# Frequency count
freq = Counter('banana')       # {'a': 3, 'n': 2, 'b': 1}
freq.most_common(2)            # [('a', 3), ('n', 2)]

# Group by key
groups = defaultdict(list)
for word in ['apple', 'ant', 'bear']:
    groups[word[0]].append(word)
# {'a': ['apple', 'ant'], 'b': ['bear']}

# Two-sum pattern: O(n)
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
```

### Binary Tree

```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# DFS traversals
def inorder(node):   # left → root → right (sorted for BST)
    return inorder(node.left) + [node.val] + inorder(node.right) if node else []

def preorder(node):  # root → left → right
    return [node.val] + preorder(node.left) + preorder(node.right) if node else []

def postorder(node): # left → right → root
    return postorder(node.left) + postorder(node.right) + [node.val] if node else []

# BFS (level-order)
from collections import deque

def bfs(root):
    if not root: return []
    result, q = [], deque([root])
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left:  q.append(node.left)
        if node.right: q.append(node.right)
    return result
```

---

## Graph Algorithms

### Representation

```python
# Adjacency list (most common for sparse graphs)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B'],
}
```

### BFS — Shortest path in unweighted graph

```python
from collections import deque

def bfs(graph, start, end):
    visited = {start}
    q = deque([[start]])
    while q:
        path = q.popleft()
        node = path[-1]
        if node == end:
            return path
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                q.append(path + [neighbour])
    return None
```

### DFS — Cycle detection, connected components

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbour in graph.get(start, []):
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
    return visited
```

---

## Dynamic Programming Patterns

### Memoisation (top-down)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n <= 1: return n
    return fib(n - 1) + fib(n - 2)
```

### Tabulation (bottom-up)

```python
def fib(n: int) -> int:
    if n <= 1: return n
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]

# Space-optimised O(1)
def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

### Common DP patterns

| Pattern | Problem type | Key idea |
|---|---|---|
| 1-D DP | Fibonacci, climbing stairs | `dp[i] = f(dp[i-1], dp[i-2])` |
| Knapsack | 0/1 subset selection | `dp[i][w] = max(include, exclude)` |
| LCS/LIS | Subsequences | 2-D table or patience sorting |
| Interval DP | Matrix chain, burst balloons | `dp[i][j] = min over all splits k` |

---

## Recursion

**Q: When to use recursion vs iteration?**

Use recursion when the problem has **natural recursive structure** (trees, divide-and-conquer). Prefer iteration for simple loops — Python's default recursion limit is 1000.

```python
import sys
sys.setrecursionlimit(10_000)   # increase if needed

# Tail recursion is NOT optimised by CPython — use a loop or explicit stack
def factorial(n: int) -> int:
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
```

---

## Interview Problem Patterns

| Pattern | Signal | Example |
|---|---|---|
| Two pointers | Sorted array, in-place | Remove duplicates, container with most water |
| Sliding window | Subarray/substring | Max sum k-window, longest unique substring |
| Fast & slow pointer | Cycle detection | Linked list cycle, find middle |
| Binary search | Sorted / monotonic | Search rotated array, min in rotated |
| BFS | Shortest path, level order | Word ladder, 01 matrix |
| DFS / backtracking | All combinations/paths | N-queens, permutations, subsets |
| Heap | Top-K, k-th largest | K closest points, merge k sorted lists |
| Monotonic stack | Next greater/smaller | Daily temperatures, largest rectangle |
| DP | Optimal substructure | Coin change, longest palindrome |
