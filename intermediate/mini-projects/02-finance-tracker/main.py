# ============================================================
# Intermediate Mini-Project 02 — Personal Finance Tracker
# ============================================================
#
# HOW TO APPROACH THIS PROJECT:
#   1. Read the README.md for the full feature list
#   2. Build the Transaction class first (pure data, no I/O)
#   3. Build FinanceTracker (manages a list of transactions)
#   4. Add persistence (save/load JSON)
#   5. Build the menu loop last
#   6. Check solution.py only after you have a working version
#
# SUGGESTED CLASS STRUCTURE:
#
# class InvalidAmountError(Exception): ...
# class InvalidDateError(Exception): ...
#
# class Transaction:
#     def __init__(self, type_, amount, category, date_, description):
#         # type_: "income" or "expense"
#         # amount: positive float
#         # date_: date object
#     def to_dict(self): ...
#     @classmethod
#     def from_dict(cls, data): ...
#     def __str__(self): ...
#
# class FinanceTracker:
#     INCOME_CATEGORIES = ["salary", "freelance", "investment", "other_income"]
#     EXPENSE_CATEGORIES = ["food", "transport", "housing", "health",
#                           "education", "entertainment", "other"]
#
#     def __init__(self): ...
#     def add_transaction(self, type_, amount, category, date_str, description=""): ...
#     def balance(self): ...  # total income - total expenses
#     def monthly_summary(self, year, month): ...
#         # returns {"balance":..., "income":..., "expenses":..., "by_category":{...}}
#     def history(self, year=None, month=None): ...
#     def export_monthly_csv(self, year, month, path): ...
#     def save(self, path): ...
#     def load(self, path): ...
#
# DATE VALIDATION:
#   Use datetime.strptime(date_str, "%d/%m/%Y").date()
#   Raise InvalidDateError on ValueError
#
# AMOUNT VALIDATION:
#   Must be a positive number. Raise InvalidAmountError otherwise.
#
# PERSISTENCE FORMAT (finances.json):
# {
#   "transactions": [
#     {"type": "income", "amount": 5000.0, "category": "salary",
#      "date": "2026-04-01", "description": "Monthly salary"}
#   ]
# }
# ============================================================

import json
import csv
import os
from datetime import datetime, date

DB_PATH = os.path.join(os.path.dirname(__file__), "finances.json")

# Write your code here


if __name__ == "__main__":
    main()
