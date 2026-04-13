# Python Core — Cheat Sheet

## Built-in Types

```python
# Numeric
x: int   = 42
y: float = 3.14
z: complex = 1 + 2j

# Text
s: str   = 'hello'
b: bytes = b'hello'

# Collections
lst:  list  = [1, 2, 3]          # mutable, ordered
tup:  tuple = (1, 2, 3)          # immutable, ordered
dct:  dict  = {'a': 1, 'b': 2}   # mutable, insertion-ordered (3.7+)
st:   set   = {1, 2, 3}          # mutable, unordered, unique
fst:  frozenset = frozenset({1, 2})  # immutable set

# Boolean / None
flag: bool = True
nothing = None
```

---

## String Operations

```python
s = 'Hello, World!'

s.upper()            # 'HELLO, WORLD!'
s.lower()            # 'hello, world!'
s.strip()            # remove leading/trailing whitespace
s.split(',')         # ['Hello', ' World!']
','.join(['a','b'])  # 'a,b'
s.replace('l','L')   # 'HeLLo, WorLd!'
s.startswith('He')   # True
s.find('World')      # 7  (-1 if not found)
s[7:12]              # 'World'
s[::-1]              # reversed

# f-strings (Python 3.6+)
name, score = 'Alice', 98.5
f'{name} scored {score:.1f}'    # 'Alice scored 98.5'
f'{score:>10.2f}'               # right-align, 2 decimals
f'{1_000_000:,}'                # '1,000,000'
```

---

## List Operations

```python
lst = [3, 1, 4, 1, 5, 9]

lst.append(2)          # add to end
lst.insert(0, 0)       # insert at index
lst.pop()              # remove & return last
lst.pop(0)             # remove & return index 0
lst.remove(1)          # remove first occurrence of value
lst.index(4)           # find index of value
lst.count(1)           # count occurrences
lst.sort()             # in-place sort
lst.sort(reverse=True)
sorted(lst)            # returns new sorted list
lst.reverse()          # in-place reverse
lst.copy()             # shallow copy
lst * 2                # [3,1,4,..., 3,1,4,...]
len(lst)               # length

# Slicing [start:stop:step]
lst[1:4]       # elements 1,2,3
lst[::2]       # every other element
lst[::-1]      # reversed copy
```

---

## Dict Operations

```python
d = {'a': 1, 'b': 2, 'c': 3}

d['a']                   # 1  (KeyError if missing)
d.get('x', 0)            # 0  (safe, returns default)
d.setdefault('z', 99)    # sets if missing, returns value
d.update({'d': 4})       # merge in-place
d.keys()   / list(d)     # keys view
d.values()               # values view
d.items()                # (key, value) pairs
d.pop('a')               # remove and return value
'b' in d                 # True  (key check)
{**d, 'e': 5}            # merge / spread (3.9+: d | {'e': 5})

# dict comprehension
squares = {n: n**2 for n in range(5)}
```

---

## Comprehensions

```python
# List
[x**2 for x in range(10)]
[x for x in range(10) if x % 2 == 0]
[x if x > 0 else 0 for x in lst]    # ternary

# Dict
{k: v for k, v in d.items() if v > 1}

# Set
{x % 3 for x in range(10)}

# Generator (lazy — no memory allocation)
(x**2 for x in range(1_000_000))
sum(x**2 for x in range(1_000_000))  # no intermediate list
```

---

## Functions

```python
def greet(name: str, greeting: str = 'Hello') -> str:
    return f'{greeting}, {name}!'

# *args — variable positional
def total(*nums):
    return sum(nums)

# **kwargs — variable keyword
def config(**kwargs):
    return kwargs

# Positional-only (/)  and keyword-only (*)
def strict(pos_only, /, normal, *, kw_only):
    ...

# Lambda
square = lambda x: x ** 2
sorted(items, key=lambda x: x['score'], reverse=True)

# Annotations (do not enforce — use mypy for that)
def add(a: int, b: int) -> int: ...
```

---

## Exceptions

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f'Error: {e}')
except (TypeError, ValueError):
    print('Type or value error')
else:
    print('No error')     # runs only if no exception
finally:
    print('Always runs')  # cleanup

# Raise
raise ValueError('must be positive')
raise ValueError('chained') from original_exc

# Custom exception
class AppError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code
```

---

## Useful Built-ins

```python
# Iteration
enumerate(['a','b','c'])        # (0,'a'), (1,'b'), (2,'c')
zip([1,2,3], ['a','b','c'])     # (1,'a'), (2,'b'), (3,'c')
map(str, [1, 2, 3])             # ['1', '2', '3']
filter(None, [0, 1, '', 'hi'])  # [1, 'hi']

# Reduction
sum([1, 2, 3])     # 6
min([3, 1, 2])     # 1
max([3, 1, 2])     # 3
any([0, 0, 1])     # True
all([1, 1, 1])     # True
sorted([3,1,2])    # [1, 2, 3]
reversed([1,2,3])  # iterator

# Type conversion
int('42')     float('3.14')     str(42)     list('abc')
bool(0)       bool('')          bool([])    # all False

# Inspection
type(x)        isinstance(x, int)
len(x)         id(x)            dir(x)
vars(obj)      hasattr(obj, 'attr')
```

---

## File I/O

```python
# Text
with open('file.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    lines = f.readlines()

with open('out.txt', 'w', encoding='utf-8') as f:
    f.write('hello\n')

# pathlib (preferred)
from pathlib import Path
Path('file.txt').read_text(encoding='utf-8')
Path('file.txt').write_text('hello', encoding='utf-8')
list(Path('.').glob('**/*.py'))

# CSV
import csv
with open('data.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

# JSON
import json
data = json.loads(Path('data.json').read_text())
Path('out.json').write_text(json.dumps(data, indent=2))
```

---

## Useful Standard Library Modules

| Module | Purpose | Key APIs |
|---|---|---|
| `pathlib` | File system paths | `Path`, `.glob()`, `.read_text()` |
| `os` | OS interface | `os.environ`, `os.getcwd()`, `os.walk()` |
| `sys` | Interpreter | `sys.argv`, `sys.path`, `sys.exit()` |
| `json` | JSON encode/decode | `json.loads()`, `json.dumps()` |
| `csv` | CSV read/write | `DictReader`, `DictWriter` |
| `datetime` | Dates & times | `datetime.now()`, `.strftime()` |
| `collections` | Specialized containers | `Counter`, `defaultdict`, `deque` |
| `itertools` | Iterator tools | `chain`, `product`, `groupby` |
| `functools` | Higher-order functions | `wraps`, `lru_cache`, `reduce` |
| `re` | Regular expressions | `re.match()`, `re.findall()` |
| `math` | Math functions | `math.sqrt()`, `math.ceil()` |
| `random` | Random numbers | `random.choice()`, `random.shuffle()` |
| `copy` | Shallow/deep copy | `copy.copy()`, `copy.deepcopy()` |
| `shutil` | File operations | `shutil.copy()`, `shutil.rmtree()` |
| `subprocess` | Run shell commands | `subprocess.run()` |
| `logging` | Logging | `logging.basicConfig()`, `getLogger()` |
| `threading` | Threads | `Thread`, `Lock` |
| `asyncio` | Async I/O | `asyncio.run()`, `gather()` |
| `unittest` | Testing | `TestCase`, `Mock` |
