"""
Pandas — Medium Exercises
=========================
Topics: groupby, apply, merge, missing data, rename, pivot.

Run:  python 02-medium.py
"""

import pandas as pd
import numpy as np

np.random.seed(42)


# Sample dataset — sales records
sales = pd.DataFrame({
    'rep':      ['Alice', 'Bob', 'Alice', 'Carol', 'Bob', 'Alice', 'Carol', 'Bob'],
    'region':   ['North', 'South', 'North', 'East', 'South', 'East', 'East', 'North'],
    'product':  ['A', 'B', 'A', 'C', 'A', 'B', 'C', 'C'],
    'units':    [12, 8, 15, 6, 10, 9, 14, 7],
    'price':    [100, 250, 100, 180, 100, 250, 180, 180],
})
sales['revenue'] = sales['units'] * sales['price']


# ---------------------------------------------------------------------------
# 1. groupby aggregation
# ---------------------------------------------------------------------------
# a) Compute total revenue per sales rep.
# b) Compute average units sold per region.
# c) For each product, compute min, max, and mean revenue.
#    (Use agg with a dict or a list.)

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. groupby + transform
# ---------------------------------------------------------------------------
# a) Add a column 'rep_total_revenue' with each rep's total revenue
#    (same value repeated for every row of that rep).
# b) Add a column 'region_rank' ranking reps by revenue within their region
#    (1 = highest revenue in that region).

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. apply with a custom function
# ---------------------------------------------------------------------------
# a) Apply a function that returns the revenue category per row:
#    revenue >= 2000 → 'high', >= 1000 → 'medium', else → 'low'
# b) Group by region, then apply a function that returns the
#    top-selling rep (by total units) in each region as a string.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. Missing data
# ---------------------------------------------------------------------------
# The DataFrame below has intentional NaN values.
# a) Count missing values per column.
# b) Drop rows where 'score' is NaN.
# c) Fill 'age' NaN with the median age.
# d) Fill 'city' NaN with 'Unknown'.

employees = pd.DataFrame({
    'name':  ['Ana', 'Bruno', 'Clara', 'Diego', 'Elisa'],
    'age':   [28, None, 35, 29, None],
    'score': [90, 75, None, 88, 82],
    'city':  ['SP', 'RJ', None, 'BH', None],
})

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 5. Merge
# ---------------------------------------------------------------------------
# Merge the two DataFrames below:
# a) Inner join on 'id' — only customers with orders.
# b) Left join on 'id' — all customers, NaN for those without orders.
# c) After the left join, fill missing 'total_spent' with 0.

customers = pd.DataFrame({
    'id':   [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'city': ['SP', 'RJ', 'SP', 'BH', 'RJ'],
})

orders = pd.DataFrame({
    'id':          [2, 3, 3, 5],
    'total_spent': [150, 320, 80, 210],
})

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 6. String operations
# ---------------------------------------------------------------------------
# Given the DataFrame below:
# a) Normalise 'name' to title case.
# b) Extract the domain from each email into a new column 'domain'.
# c) Filter only rows where the email domain is 'gmail.com'.

contacts = pd.DataFrame({
    'name':  ['alice SMITH', 'BOB jones', 'carol WHITE'],
    'email': ['alice@gmail.com', 'bob@yahoo.com', 'carol@gmail.com'],
})

# YOUR CODE HERE
