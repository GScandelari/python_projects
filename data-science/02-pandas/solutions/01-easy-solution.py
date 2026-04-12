"""
Pandas — Easy Solutions
"""

import pandas as pd


# ---------------------------------------------------------------------------
# 1. Series basics
# ---------------------------------------------------------------------------
temps = pd.Series(
    [22, 25, 28, 30, 27, 24],
    index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
)
print(temps['Mar'])          # 28
print(temps['May'])          # 27
print(temps[temps > 26])     # Mar 28, Apr 30, May 27


# ---------------------------------------------------------------------------
# 2. DataFrame creation
# ---------------------------------------------------------------------------
students_data = {
    'name':   ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'age':    [20, 22, 21, 23, 20],
    'grade':  [88, 74, 92, 65, 79],
    'passed': [True, True, True, False, True],
}
df = pd.DataFrame(students_data)
print(df.head(3))
print(df.shape)        # (5, 4)
print(df.columns.tolist())
print(df.dtypes)


# ---------------------------------------------------------------------------
# 3. Column selection and row slicing
# ---------------------------------------------------------------------------
print(df[['name', 'grade']])
print(df.iloc[1:4])
print(df.loc[df['name'] == 'Carol'])
print(df.loc[df['name'] == 'David', 'grade'].values[0])   # 65


# ---------------------------------------------------------------------------
# 4. Filtering
# ---------------------------------------------------------------------------
print(df[df['grade'] >= 80])
print(df[(df['passed']) & (df['age'] > 20)])
print(df[df['name'].str[0].isin(['A', 'E'])])


# ---------------------------------------------------------------------------
# 5. Basic operations
# ---------------------------------------------------------------------------
def letter_grade(g):
    if g >= 90: return 'A'
    if g >= 80: return 'B'
    if g >= 70: return 'C'
    return 'F'

df['letter_grade'] = df['grade'].apply(letter_grade)
print(df['grade'].mean())                        # 79.6
print(df.sort_values('grade', ascending=False))


# ---------------------------------------------------------------------------
# 6. describe and value_counts
# ---------------------------------------------------------------------------
print(df.describe())
print(df['letter_grade'].value_counts())
