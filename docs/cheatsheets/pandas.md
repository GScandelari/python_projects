# Pandas — Cheat Sheet

## Create and Inspect

```python
import pandas as pd
import numpy as np

# Create
df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})
df = pd.read_csv('file.csv', encoding='utf-8')
df = pd.read_json('file.json')
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')

# Inspect
df.shape         # (rows, cols)
df.dtypes        # column types
df.info()        # types + non-null counts
df.describe()    # numeric statistics
df.head(5)       # first 5 rows
df.tail(5)       # last 5 rows
df.sample(3)     # 3 random rows
df.columns.tolist()
df.index
```

---

## Select

```python
# Column(s)
df['col']              # Series
df[['a', 'b']]         # DataFrame

# Row(s) — loc (label), iloc (position)
df.loc[0]              # row with label 0
df.loc[0:3, 'name']    # rows 0–3, column 'name'
df.iloc[0]             # first row by position
df.iloc[-1]            # last row
df.iloc[0:3, 1:3]      # rows 0–2, cols 1–2

# Boolean filter
df[df['age'] > 25]
df[(df['age'] > 25) & (df['score'] >= 80)]
df[df['name'].isin(['Alice', 'Carol'])]
df.query('age > 25 and score >= 80')

# String filter
df[df['name'].str.startswith('A')]
df[df['email'].str.contains('@gmail', case=False)]
```

---

## Transform

```python
# New column
df['grade'] = df['score'].apply(lambda x: 'A' if x >= 90 else 'B')
df['total'] = df['units'] * df['price']   # vectorised

# Rename / drop
df.rename(columns={'old': 'new'}, inplace=True)
df.drop(columns=['col1', 'col2'], inplace=True)

# Type conversion
df['date'] = pd.to_datetime(df['date'])
df['price'] = df['price'].astype(float)

# map — element-wise lookup
df['level'] = df['score'].map({100: 'A', 90: 'B'})

# String accessor
df['name'] = df['name'].str.strip().str.title()
df['domain'] = df['email'].str.split('@').str[1]

# Chained assign (avoids SettingWithCopyWarning)
df = (df
    .assign(name=lambda d: d['name'].str.strip())
    .assign(total=lambda d: d['units'] * d['price'])
)
```

---

## Missing Data

```python
df.isnull().sum()              # count NaN per column
df.dropna()                    # drop rows with any NaN
df.dropna(subset=['score'])    # drop only if 'score' NaN
df.fillna(0)                   # fill all NaN with 0
df['age'].fillna(df['age'].median(), inplace=True)
df.interpolate()               # interpolate numeric NaN
```

---

## Aggregation

```python
df['score'].mean()
df['score'].agg(['mean', 'min', 'max', 'std'])

# groupby
df.groupby('dept')['salary'].mean()
df.groupby('dept').agg({'salary': 'mean', 'age': 'max'})

# transform — same shape as original (adds col without losing rows)
df['dept_avg'] = df.groupby('dept')['score'].transform('mean')

# value_counts
df['grade'].value_counts()
df['grade'].value_counts(normalize=True)   # proportions
```

---

## Merge / Join

```python
# merge (SQL JOIN)
pd.merge(left, right, on='id', how='inner')   # how: inner/left/right/outer
pd.merge(left, right, left_on='user_id', right_on='id')

# concat (stack)
pd.concat([df1, df2], ignore_index=True)      # vertical (axis=0)
pd.concat([df1, df2], axis=1)                 # horizontal

# pivot table
pd.pivot_table(df, values='sales', index='region',
               columns='quarter', aggfunc='sum', fill_value=0, margins=True)
```

---

## Sorting & Ranking

```python
df.sort_values('score', ascending=False)
df.sort_values(['dept', 'score'], ascending=[True, False])
df['rank'] = df['score'].rank(ascending=False, method='dense')
df.nlargest(5, 'score')
df.nsmallest(3, 'price')
```

---

## Time Series

```python
# Create date index
dates = pd.date_range('2024-01-01', periods=30, freq='B')   # business days
s = pd.Series(data, index=dates)

# Resample
s.resample('W').last()       # weekly close
s.resample('ME').mean()      # month-end mean

# Rolling / expanding
s.rolling(7).mean()          # 7-period moving average
s.ewm(span=7).mean()         # exponential weighted
s.expanding().max()          # running maximum

# Shift / pct_change
s.shift(1)                   # lag by 1 period
s.pct_change()               # period-over-period % change

# Datetime accessor
df['date'].dt.year / .month / .day / .weekday()
df['date'].dt.strftime('%Y-%m')
```

---

## I/O

```python
df.to_csv('out.csv', index=False, encoding='utf-8')
df.to_json('out.json', orient='records', indent=2)
df.to_excel('out.xlsx', sheet_name='Data', index=False)
df.to_dict(orient='records')  # list of dicts
```
