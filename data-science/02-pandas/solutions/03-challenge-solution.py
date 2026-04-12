"""
Pandas — Challenge Solutions
"""

import pandas as pd
import numpy as np

np.random.seed(42)


# ---------------------------------------------------------------------------
# 1. Pivot table
# ---------------------------------------------------------------------------
sales = pd.DataFrame({
    'rep':     ['Alice','Bob','Alice','Carol','Bob','Alice','Carol','Bob','Alice','Carol'],
    'product': ['A','B','A','C','A','B','C','C','B','A'],
    'units':   [12, 8, 15, 6, 10, 9, 14, 7, 11, 5],
    'price':   [100, 250, 100, 180, 100, 250, 180, 180, 250, 100],
})
sales['revenue'] = sales['units'] * sales['price']

pivot = pd.pivot_table(sales, values='revenue', index='rep',
                       columns='product', aggfunc='sum', fill_value=0, margins=True)
print(pivot)
print(f'Best product: {pivot.loc["All"].drop("All").idxmax()}')


# ---------------------------------------------------------------------------
# 2. Time series
# ---------------------------------------------------------------------------
bdays = pd.bdate_range('2024-01-01', '2024-01-31')
returns = np.random.normal(0, 0.5, len(bdays))
prices = pd.Series(100 + np.cumsum(returns), index=bdays)

weekly_close = prices.resample('W').last()
rolling_mean = prices.rolling(3).mean()
print(f'Max price date: {prices.idxmax().date()}')


# ---------------------------------------------------------------------------
# 3. Multi-index
# ---------------------------------------------------------------------------
index = pd.MultiIndex.from_tuples(
    [(2022,'Q1'),(2022,'Q2'),(2022,'Q3'),(2022,'Q4'),
     (2023,'Q1'),(2023,'Q2'),(2023,'Q3'),(2023,'Q4')],
    names=['year','quarter']
)
data = pd.DataFrame({
    'revenue': [120, 135, 128, 150, 145, 160, 155, 175],
    'costs':   [ 80,  90,  85,  95,  92, 100,  98, 110],
}, index=index)

print(data.loc[2023])                       # all 2023
print(data.xs('Q2', level='quarter'))       # Q2 across years
print(data['revenue'].unstack('quarter'))   # quarters as columns

# YoY growth — total revenue per year
yoy = data['revenue'].groupby('year').sum().pct_change() * 100
print(yoy.round(2))


# ---------------------------------------------------------------------------
# 4. Window functions
# ---------------------------------------------------------------------------
weekly_sales = pd.Series(
    [120, 135, 118, 142, 138, 155, 161, 148, 170, 165, 180, 175],
    index=pd.date_range('2024-01-01', periods=12, freq='W')
)

sma4  = weekly_sales.rolling(4).mean()
ewm4  = weekly_sales.ewm(span=4).mean()
wow   = weekly_sales.pct_change() * 100
peak  = weekly_sales.cummax()

print(pd.DataFrame({'sales': weekly_sales, 'SMA4': sma4.round(1),
                    'EWM4': ewm4.round(1), 'WoW%': wow.round(1), 'Peak': peak}))


# ---------------------------------------------------------------------------
# 5. Categorical data
# ---------------------------------------------------------------------------
tickets = pd.DataFrame({
    'id':       range(1, 9),
    'issue':    ['Bug A','Bug B','Feat A','Bug C','Feat B','Bug D','Feat C','Bug E'],
    'priority': ['High','Low','Medium','Critical','Low','High','Medium','Critical'],
})

order = ['Low', 'Medium', 'High', 'Critical']
tickets['priority'] = pd.Categorical(tickets['priority'], categories=order, ordered=True)

high_plus = tickets[tickets['priority'] > 'Medium']
print(high_plus)

print(tickets.sort_values('priority'))
print(tickets['priority'].value_counts().reindex(order))


# ---------------------------------------------------------------------------
# 6. End-to-end pipeline
# ---------------------------------------------------------------------------
raw_data = pd.DataFrame({
    'date':   ['2024-01-15', '2024-01-20', '2024-02-03', '2024-01-15',
               '2024-02-18', '2024-03-05', '2024-02-03', '2024-03-12'],
    'name':   [' Alice', 'Bob ', ' Alice', ' Alice',
               'Carol', ' Bob', 'Bob ', 'Carol'],
    'amount': [250, 130, 75, 250, None, 310, 130, 195],
})

clean = (raw_data
    .drop_duplicates()
    .assign(
        name   = lambda df: df['name'].str.strip(),
        date   = lambda df: pd.to_datetime(df['date']),
        amount = lambda df: df['amount'].fillna(df['amount'].median()),
    )
    .assign(month = lambda df: df['date'].dt.month)
)

monthly = clean.groupby('month')['amount'].sum()
print(monthly)
