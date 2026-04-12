# Pandas — Solution Notes

## Easy

**loc vs iloc:** `loc` is label-based (works with index labels and column names). `iloc` is position-based (0-indexed integers). When the index is the default RangeIndex, `loc[0]` and `iloc[0]` are equivalent — but diverge once you reset, sort, or filter.

**Boolean filtering:** Combine conditions with `&` (and) and `|` (or), not Python's `and`/`or`. Always wrap each condition in parentheses: `df[(df['a'] > 1) & (df['b'] < 5)]`.

**apply vs vectorised:** For simple math, prefer vectorised operations (`df['score'] * 2`). Use `apply` only when the logic can't be expressed as a vectorised expression.

## Medium

**groupby mental model:** Think of it as split → apply → combine. `transform` returns a same-size result aligned to the original index — perfect for adding aggregated columns without losing rows.

**transform vs agg:** `agg` reduces each group to one row. `transform` returns one value per original row. Use `transform` when you need the group result alongside the original data.

**Missing data strategy:**
- `dropna(subset=['col'])` — drop only when a specific column is NaN.
- `fillna(df['col'].median())` — use robust statistics for numeric imputation.
- Always impute on training data; apply the same value to test data.

**Merge how parameter:**
- `inner` — intersection (rows in both).
- `left` — all left rows, NaN where no match.
- `outer` — union (all rows from both).

**String accessor `.str`:** Exposes string methods as vectorised operations. Chain them: `df['email'].str.lower().str.split('@').str[1]`.

## Challenge

**Pivot tables with margins:** `margins=True` adds a row/column named `"All"` with marginal aggregates. Drop it before finding idxmax: `pivot.loc["All"].drop("All").idxmax()`.

**Time series resampling:** `resample('W')` creates weekly buckets. Common aggregations: `.last()` (closing price), `.mean()`, `.sum()`. The frequency string follows pandas offset aliases: `'D'` day, `'W'` week, `'MS'` month start, `'QS'` quarter start.

**MultiIndex selection:**
- `df.loc[level_0_value]` — select by outer level.
- `df.xs(value, level='name')` — cross-section at any level.
- `unstack(level)` — pivot a level into columns.

**Categorical ordering:** `pd.Categorical(values, categories=[...], ordered=True)` enables comparison operators (`>`, `<`) and correct sorting. `value_counts().reindex(order)` shows counts in the defined order.

**Chained assignment with `.assign`:** Prefer `.assign()` over direct column assignment in pipelines — it returns a new DataFrame and avoids `SettingWithCopyWarning`. Each `.assign` call can reference columns created earlier in the same chain.
