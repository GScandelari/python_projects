# Mini-Project 02 — Personal Finance Tracker

## Description

A terminal-based personal finance tracker. Records income and expenses, computes balances, and generates monthly reports — all persisted in JSON.

## Concepts Used

| Concept | Where |
|---|---|
| `01-oop` | `Transaction`, `FinanceTracker` classes, custom exceptions |
| `03-file-handling` | JSON persistence, CSV monthly report |
| `04-error-handling` | `InvalidAmountError`, `InvalidDateError`, input validation |
| `02-modules-packages` | `json`, `csv`, `datetime` |

## How to Run

```bash
python main.py
```

Data is saved to `finances.json` automatically.

## Features

- Add income or expense transactions (amount, category, date, description)
- View current balance
- Filter transactions by month/year
- Summary by category (total spent/earned per category)
- Monthly report exported to CSV
- All amounts validated (must be positive numbers)
- All dates validated (DD/MM/YYYY format)
- JSON persistence

## Categories

Income: `salary`, `freelance`, `investment`, `other_income`  
Expense: `food`, `transport`, `housing`, `health`, `education`, `entertainment`, `other`

## Example Output

```
=== FINANCE TRACKER ===
[1] Add transaction
[2] View balance
[3] Monthly summary
[4] Transaction history
[5] Export monthly report (CSV)
[0] Save & Exit

> 3

=== APRIL 2026 ===
Balance        : R$ 2,340.00
Total income   : R$ 5,000.00
Total expenses : R$ 2,660.00

By category:
  salary       : +R$ 5,000.00
  food         : -R$   890.00
  housing      : -R$ 1,200.00
  transport    : -R$   320.00
  entertainment: -R$   250.00
```
