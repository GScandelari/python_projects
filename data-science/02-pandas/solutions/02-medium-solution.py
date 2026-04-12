"""
Pandas — Medium Solutions
"""

import pandas as pd
import numpy as np

np.random.seed(42)

sales = pd.DataFrame({
    'rep':     ['Alice', 'Bob', 'Alice', 'Carol', 'Bob', 'Alice', 'Carol', 'Bob'],
    'region':  ['North', 'South', 'North', 'East', 'South', 'East', 'East', 'North'],
    'product': ['A', 'B', 'A', 'C', 'A', 'B', 'C', 'C'],
    'units':   [12, 8, 15, 6, 10, 9, 14, 7],
    'price':   [100, 250, 100, 180, 100, 250, 180, 180],
})
sales['revenue'] = sales['units'] * sales['price']


# ---------------------------------------------------------------------------
# 1. groupby aggregation
# ---------------------------------------------------------------------------
print(sales.groupby('rep')['revenue'].sum())

print(sales.groupby('region')['units'].mean())

print(sales.groupby('product')['revenue'].agg(['min', 'max', 'mean']))


# ---------------------------------------------------------------------------
# 2. groupby + transform
# ---------------------------------------------------------------------------
sales['rep_total_revenue'] = sales.groupby('rep')['revenue'].transform('sum')

sales['region_rank'] = sales.groupby('region')['revenue'].rank(
    ascending=False, method='dense'
)
print(sales[['rep', 'region', 'revenue', 'rep_total_revenue', 'region_rank']])


# ---------------------------------------------------------------------------
# 3. apply with a custom function
# ---------------------------------------------------------------------------
def categorise(row):
    if row['revenue'] >= 2000: return 'high'
    if row['revenue'] >= 1000: return 'medium'
    return 'low'

sales['category'] = sales.apply(categorise, axis=1)
print(sales[['rep', 'revenue', 'category']])

# Top rep per region by total units
def top_rep(group):
    return group.groupby('rep')['units'].sum().idxmax()

print(sales.groupby('region').apply(top_rep))


# ---------------------------------------------------------------------------
# 4. Missing data
# ---------------------------------------------------------------------------
employees = pd.DataFrame({
    'name':  ['Ana', 'Bruno', 'Clara', 'Diego', 'Elisa'],
    'age':   [28, None, 35, 29, None],
    'score': [90, 75, None, 88, 82],
    'city':  ['SP', 'RJ', None, 'BH', None],
})

print(employees.isnull().sum())
clean = employees.dropna(subset=['score'])
clean = clean.copy()
clean['age'] = clean['age'].fillna(clean['age'].median())
clean['city'] = clean['city'].fillna('Unknown')
print(clean)


# ---------------------------------------------------------------------------
# 5. Merge
# ---------------------------------------------------------------------------
customers = pd.DataFrame({
    'id':   [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'city': ['SP', 'RJ', 'SP', 'BH', 'RJ'],
})
orders = pd.DataFrame({
    'id':          [2, 3, 3, 5],
    'total_spent': [150, 320, 80, 210],
})

# a) Inner join
inner = pd.merge(customers, orders, on='id', how='inner')
print(inner)

# b) Left join
left = pd.merge(customers, orders, on='id', how='left')
print(left)

# c) Fill missing
left['total_spent'] = left['total_spent'].fillna(0)
print(left)


# ---------------------------------------------------------------------------
# 6. String operations
# ---------------------------------------------------------------------------
contacts = pd.DataFrame({
    'name':  ['alice SMITH', 'BOB jones', 'carol WHITE'],
    'email': ['alice@gmail.com', 'bob@yahoo.com', 'carol@gmail.com'],
})

contacts['name'] = contacts['name'].str.title()
contacts['domain'] = contacts['email'].str.split('@').str[1]
gmail_only = contacts[contacts['domain'] == 'gmail.com']
print(gmail_only)
