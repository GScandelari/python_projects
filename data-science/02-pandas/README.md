# Pandas

The essential library for tabular data manipulation and analysis.

**Install:** `pip install pandas`

**Import convention:** `import pandas as pd`

---

## 1. Series and DataFrame

```python
import pandas as pd

# Series — 1-D labelled array
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# DataFrame — 2-D table with labelled axes
df = pd.DataFrame({
    'name':  ['Alice', 'Bob', 'Carol'],
    'age':   [25, 30, 22],
    'score': [88.5, 74.0, 92.3],
})

print(df.shape)    # (3, 3)
print(df.dtypes)
print(df.info())
print(df.describe())
```

## 2. Reading and Writing Data

```python
# CSV
df = pd.read_csv('data.csv')
df.to_csv('output.csv', index=False)

# JSON
df = pd.read_json('data.json')

# Excel (requires openpyxl)
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Quick inspection
df.head(5)     # first 5 rows
df.tail(5)     # last 5 rows
df.sample(3)   # 3 random rows
```

## 3. Indexing — loc and iloc

```python
# loc — label-based
df.loc[0]                  # row with index label 0
df.loc[0:2, 'name']        # rows 0–2, column 'name'
df.loc[df['age'] > 25]     # boolean filtering

# iloc — position-based (integer)
df.iloc[0]          # first row
df.iloc[-1]         # last row
df.iloc[0:3, 1:3]   # rows 0–2, columns 1–2
```

## 4. Filtering and Querying

```python
# Boolean conditions
df[df['age'] > 25]
df[(df['age'] > 25) & (df['score'] >= 80)]
df[df['name'].isin(['Alice', 'Carol'])]

# query() — string expression (cleaner for complex conditions)
df.query('age > 25 and score >= 80')

# str methods
df[df['name'].str.startswith('A')]
df[df['name'].str.contains('li', case=False)]
```

## 5. Adding and Transforming Columns

```python
# New column
df['grade'] = df['score'].apply(lambda x: 'A' if x >= 90 else 'B')

# Vectorised operations (preferred over apply for simple math)
df['score_scaled'] = (df['score'] - df['score'].min()) / \
                     (df['score'].max() - df['score'].min())

# map — element-wise transformation using dict or function
df['level'] = df['age'].map({25: 'junior', 30: 'senior', 22: 'junior'})

# rename
df.rename(columns={'name': 'full_name'}, inplace=True)

# drop
df.drop(columns=['grade'], inplace=True)
```

## 6. groupby

```python
# Aggregate by group
df.groupby('department')['salary'].mean()
df.groupby('department').agg({'salary': 'mean', 'age': 'max'})

# Multiple aggregations on one column
df.groupby('department')['salary'].agg(['mean', 'min', 'max', 'count'])

# Transform — returns same-shape result (useful for normalisation within group)
df['salary_norm'] = df.groupby('dept')['salary'].transform(
    lambda x: (x - x.mean()) / x.std()
)
```

## 7. Missing Data

```python
df.isnull().sum()         # count NaN per column
df.dropna()               # drop rows with any NaN
df.dropna(subset=['age']) # drop only if 'age' is NaN
df.fillna(0)              # fill with constant
df.fillna(df.mean())      # fill with column mean
df['age'].fillna(df['age'].median(), inplace=True)
```

## 8. Merging and Joining

```python
# Merge (like SQL JOIN)
pd.merge(df_left, df_right, on='id', how='inner')
pd.merge(df_left, df_right, on='id', how='left')
pd.merge(df_left, df_right, left_on='user_id', right_on='id')

# Concatenate (stack)
pd.concat([df1, df2], ignore_index=True)          # vertical
pd.concat([df1, df2], axis=1)                     # horizontal
```

## 9. Sorting and Ranking

```python
df.sort_values('score', ascending=False)
df.sort_values(['dept', 'score'], ascending=[True, False])
df['rank'] = df['score'].rank(ascending=False, method='dense')
```

## 10. Pivot Tables

```python
pd.pivot_table(df,
    values='sales',
    index='region',
    columns='quarter',
    aggfunc='sum',
    fill_value=0)
```

---

## Quick Reference

```python
# I/O
pd.read_csv / pd.read_json / df.to_csv

# Inspection
df.shape / df.dtypes / df.info() / df.describe()
df.head() / df.tail() / df.sample()

# Indexing
df['col'] / df[['a','b']]       # column selection
df.loc[label] / df.iloc[pos]    # row selection
df[df['col'] > x]               # boolean filter

# Transformation
df['new'] = df['col'].apply(fn)
df.groupby('col').agg({'col2': 'mean'})
pd.merge(a, b, on='key', how='inner')
pd.concat([a, b], ignore_index=True)

# Cleaning
df.isnull().sum() / df.dropna() / df.fillna(value)
```

## Practice

| File | Difficulty | Topics |
|---|---|---|
| [01-easy.py](exercises/01-easy.py) | Easy | Series, DataFrame, indexing, filtering |
| [02-medium.py](exercises/02-medium.py) | Medium | groupby, apply, merge, missing data |
| [03-challenge.py](exercises/03-challenge.py) | Challenge | pivot tables, time series, complex transforms |

Solutions: [solutions/](solutions/)
