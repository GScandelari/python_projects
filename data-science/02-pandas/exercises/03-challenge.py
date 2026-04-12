"""
Pandas — Challenge Exercises
=============================
Topics: pivot tables, time series, multi-index, complex transformations,
        window functions, categorical data.

Run:  python 03-challenge.py
"""

import pandas as pd
import numpy as np

np.random.seed(42)


# ---------------------------------------------------------------------------
# 1. Pivot table
# ---------------------------------------------------------------------------
# Using the sales DataFrame below:
# a) Build a pivot table showing total revenue per rep (rows) × product (cols).
# b) Add a 'Total' row and column with marginal sums.
# c) Which product generated the most revenue overall?

sales = pd.DataFrame({
    'rep':     ['Alice','Bob','Alice','Carol','Bob','Alice','Carol','Bob','Alice','Carol'],
    'product': ['A','B','A','C','A','B','C','C','B','A'],
    'units':   [12, 8, 15, 6, 10, 9, 14, 7, 11, 5],
    'price':   [100, 250, 100, 180, 100, 250, 180, 180, 250, 100],
})
sales['revenue'] = sales['units'] * sales['price']

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 2. Time series basics
# ---------------------------------------------------------------------------
# a) Create a DatetimeIndex covering every business day of January 2024.
# b) Build a Series with random daily stock prices starting at 100,
#    using cumulative sum of small random returns.
# c) Resample to weekly frequency, reporting the last closing price of each week.
# d) Compute a 3-day rolling mean.
# e) Find the date of the maximum price.

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 3. Multi-index
# ---------------------------------------------------------------------------
# Given the DataFrame below with a MultiIndex (year, quarter):
# a) Select all data for year 2023.
# b) Select Q2 data across all years.
# c) Unstack the 'quarter' level to get quarters as columns.
# d) Compute year-over-year growth for revenue (pct_change at year level).

index = pd.MultiIndex.from_tuples(
    [(2022, 'Q1'), (2022, 'Q2'), (2022, 'Q3'), (2022, 'Q4'),
     (2023, 'Q1'), (2023, 'Q2'), (2023, 'Q3'), (2023, 'Q4')],
    names=['year', 'quarter']
)
data = pd.DataFrame({
    'revenue': [120, 135, 128, 150, 145, 160, 155, 175],
    'costs':   [ 80,  90,  85,  95,  92, 100,  98, 110],
}, index=index)

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 4. Window functions
# ---------------------------------------------------------------------------
# The series below represents weekly sales figures.
# a) Compute a 4-week simple moving average.
# b) Compute a 4-week exponential weighted mean (ewm).
# c) Compute week-over-week percentage change.
# d) Compute the cumulative maximum (running peak).

weekly_sales = pd.Series(
    [120, 135, 118, 142, 138, 155, 161, 148, 170, 165, 180, 175],
    index=pd.date_range('2024-01-01', periods=12, freq='W')
)

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 5. Categorical data
# ---------------------------------------------------------------------------
# a) Convert the 'priority' column to a Categorical with ordered levels:
#    Low < Medium < High < Critical
# b) Filter rows where priority > 'Medium' (use the ordering).
# c) Sort by priority (ascending — Low first).
# d) Print the value_counts in priority order.

tickets = pd.DataFrame({
    'id':       range(1, 9),
    'issue':    ['Bug A','Bug B','Feat A','Bug C','Feat B','Bug D','Feat C','Bug E'],
    'priority': ['High','Low','Medium','Critical','Low','High','Medium','Critical'],
})

# YOUR CODE HERE


# ---------------------------------------------------------------------------
# 6. End-to-end pipeline
# ---------------------------------------------------------------------------
# The raw_data DataFrame below has quality issues.
# Build a clean, analysis-ready DataFrame by:
# a) Dropping duplicate rows.
# b) Stripping whitespace from string columns.
# c) Converting 'date' to datetime.
# d) Filling missing 'amount' with the median.
# e) Adding a 'month' column extracted from 'date'.
# f) Grouping by month and computing total amount.

raw_data = pd.DataFrame({
    'date':   ['2024-01-15', '2024-01-20', '2024-02-03', '2024-01-15',
                '2024-02-18', '2024-03-05', '2024-02-03', '2024-03-12'],
    'name':   [' Alice', 'Bob ', ' Alice', ' Alice',
                'Carol', ' Bob', 'Bob ', 'Carol'],
    'amount': [250, 130, 75, 250, None, 310, 130, 195],
})

# YOUR CODE HERE
