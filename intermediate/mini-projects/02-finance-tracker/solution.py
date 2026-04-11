# ============================================================
# Intermediate Mini-Project 02 — Personal Finance Tracker (SOLUTION)
# ============================================================

import json
import csv
import os
from datetime import datetime, date

DB_PATH = os.path.join(os.path.dirname(__file__), "finances.json")


# ── Custom Exceptions ─────────────────────────────────────

class FinanceError(Exception):
    pass

class InvalidAmountError(FinanceError):
    def __init__(self, value):
        super().__init__(f"Amount must be a positive number, got: {value!r}")

class InvalidDateError(FinanceError):
    def __init__(self, value):
        super().__init__(f"Invalid date '{value}'. Use DD/MM/YYYY format.")

class InvalidCategoryError(FinanceError):
    def __init__(self, category, valid):
        super().__init__(f"Unknown category '{category}'. Valid: {valid}")


# ── Transaction ───────────────────────────────────────────

class Transaction:
    def __init__(self, type_, amount, category, date_, description=""):
        self.type = type_            # "income" or "expense"
        self.amount = amount         # positive float
        self.category = category
        self.date = date_            # date object
        self.description = description

    def to_dict(self):
        return {
            "type": self.type,
            "amount": self.amount,
            "category": self.category,
            "date": str(self.date),
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["type"],
            data["amount"],
            data["category"],
            date.fromisoformat(data["date"]),
            data.get("description", ""),
        )

    def __str__(self):
        sign = "+" if self.type == "income" else "-"
        return (f"{self.date}  {sign}R$ {self.amount:>10,.2f}  "
                f"{self.category:<15} {self.description}")


# ── FinanceTracker ────────────────────────────────────────

class FinanceTracker:
    INCOME_CATEGORIES = ["salary", "freelance", "investment", "other_income"]
    EXPENSE_CATEGORIES = ["food", "transport", "housing", "health",
                          "education", "entertainment", "other"]

    def __init__(self):
        self.transactions = []

    @property
    def all_categories(self):
        return self.INCOME_CATEGORIES + self.EXPENSE_CATEGORIES

    def _validate_amount(self, amount):
        try:
            val = float(amount)
        except (TypeError, ValueError):
            raise InvalidAmountError(amount)
        if val <= 0:
            raise InvalidAmountError(amount)
        return val

    def _validate_date(self, date_str):
        try:
            return datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            raise InvalidDateError(date_str)

    def _validate_category(self, type_, category):
        valid = self.INCOME_CATEGORIES if type_ == "income" else self.EXPENSE_CATEGORIES
        if category not in valid:
            raise InvalidCategoryError(category, valid)

    def add_transaction(self, type_, amount, category, date_str, description=""):
        amount = self._validate_amount(amount)
        date_ = self._validate_date(date_str)
        self._validate_category(type_, category)
        t = Transaction(type_, amount, category, date_, description)
        self.transactions.append(t)
        return t

    def balance(self):
        total = 0
        for t in self.transactions:
            total += t.amount if t.type == "income" else -t.amount
        return total

    def history(self, year=None, month=None):
        result = self.transactions
        if year:
            result = [t for t in result if t.date.year == year]
        if month:
            result = [t for t in result if t.date.month == month]
        return sorted(result, key=lambda t: t.date)

    def monthly_summary(self, year, month):
        txns = self.history(year, month)
        income = sum(t.amount for t in txns if t.type == "income")
        expenses = sum(t.amount for t in txns if t.type == "expense")
        by_cat = {}
        for t in txns:
            sign = 1 if t.type == "income" else -1
            by_cat[t.category] = by_cat.get(t.category, 0) + sign * t.amount
        return {
            "balance": income - expenses,
            "income": income,
            "expenses": expenses,
            "by_category": by_cat,
        }

    def export_monthly_csv(self, year, month, path):
        txns = self.history(year, month)
        with open(path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "type", "amount", "category", "description"])
            for t in txns:
                writer.writerow([t.date, t.type, f"{t.amount:.2f}", t.category, t.description])
        print(f"  Exported {len(txns)} transactions to {path}")

    def save(self, path):
        data = {"transactions": [t.to_dict() for t in self.transactions]}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load(self, path):
        if not os.path.exists(path):
            return
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.transactions = [Transaction.from_dict(d) for d in data.get("transactions", [])]


# ── Menu ──────────────────────────────────────────────────

def show_menu():
    print("\n" + "=" * 35)
    print("      FINANCE TRACKER")
    print("=" * 35)
    print("  [1] Add transaction")
    print("  [2] Current balance")
    print("  [3] Monthly summary")
    print("  [4] Transaction history")
    print("  [5] Export monthly CSV")
    print("  [0] Save & Exit")


def add_transaction_menu(tracker):
    type_ = ""
    while type_ not in ("income", "expense"):
        type_ = input("Type (income/expense): ").strip().lower()

    cats = tracker.INCOME_CATEGORIES if type_ == "income" else tracker.EXPENSE_CATEGORIES
    print("Categories:", ", ".join(cats))
    category = input("Category: ").strip().lower()

    amount = input("Amount (R$): ").strip()
    date_str = input("Date (DD/MM/YYYY): ").strip()
    description = input("Description (optional): ").strip()

    t = tracker.add_transaction(type_, amount, category, date_str, description)
    sign = "+" if type_ == "income" else "-"
    print(f"  Added: {sign}R$ {t.amount:,.2f} [{t.category}]")


def monthly_summary_menu(tracker):
    try:
        year = int(input("Year (e.g. 2026): "))
        month = int(input("Month (1-12): "))
    except ValueError:
        print("  Invalid year/month.")
        return
    s = tracker.monthly_summary(year, month)
    months = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    print(f"\n=== {months[month]} {year} ===")
    print(f"Balance        : R$ {s['balance']:>12,.2f}")
    print(f"Total income   : R$ {s['income']:>12,.2f}")
    print(f"Total expenses : R$ {s['expenses']:>12,.2f}")
    if s["by_category"]:
        print("\nBy category:")
        for cat, val in sorted(s["by_category"].items(), key=lambda x: x[1], reverse=True):
            sign = "+" if val >= 0 else ""
            print(f"  {cat:<15}: {sign}R$ {val:>10,.2f}")


def main():
    tracker = FinanceTracker()
    tracker.load(DB_PATH)
    print(f"Finance Tracker loaded. Balance: R$ {tracker.balance():,.2f}")

    while True:
        show_menu()
        choice = input("> ").strip()

        if choice == "0":
            tracker.save(DB_PATH)
            print("Saved. Goodbye!")
            break
        try:
            if choice == "1":
                add_transaction_menu(tracker)
            elif choice == "2":
                print(f"\n  Current balance: R$ {tracker.balance():,.2f}")
            elif choice == "3":
                monthly_summary_menu(tracker)
            elif choice == "4":
                txns = tracker.history()
                if not txns:
                    print("  No transactions.")
                else:
                    for t in txns[-20:]:   # show last 20
                        print(f"  {t}")
            elif choice == "5":
                try:
                    year = int(input("Year: "))
                    month = int(input("Month (1-12): "))
                except ValueError:
                    print("  Invalid input.")
                    continue
                path = os.path.join(os.path.dirname(__file__), f"report_{year}_{month:02d}.csv")
                tracker.export_monthly_csv(year, month, path)
            else:
                print("  Invalid option.")
        except FinanceError as e:
            print(f"  Error: {e}")


if __name__ == "__main__":
    main()
