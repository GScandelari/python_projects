# ============================================================
# advanced/projects/02-test-suite/bank.py
# Production code — do NOT modify
# ============================================================

import json
from pathlib import Path
from datetime import datetime


class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount  = amount
        super().__init__(
            f"Cannot withdraw R${amount:.2f}: balance is R${balance:.2f}"
        )


class InvalidAmountError(ValueError):
    pass


class Account:
    def __init__(self, owner: str, balance: float = 0.0):
        if not owner.strip():
            raise ValueError("Owner name cannot be empty")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.owner    = owner.strip()
        self._balance = float(balance)
        self._transactions: list[dict] = []

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise InvalidAmountError(f"Deposit amount must be positive, got {amount}")
        self._balance += amount
        self._transactions.append({
            "type": "deposit", "amount": amount,
            "balance": self._balance, "ts": datetime.now().isoformat()
        })
        return self._balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise InvalidAmountError(f"Withdrawal amount must be positive, got {amount}")
        if amount > self._balance:
            raise InsufficientFundsError(self._balance, amount)
        self._balance -= amount
        self._transactions.append({
            "type": "withdraw", "amount": amount,
            "balance": self._balance, "ts": datetime.now().isoformat()
        })
        return self._balance

    def balance(self) -> float:
        return self._balance

    def statement(self) -> list[dict]:
        return list(self._transactions)

    def __str__(self):
        return f"Account[{self.owner}] R${self._balance:.2f}"

    def __repr__(self):
        return f"Account(owner={self.owner!r}, balance={self._balance})"


class Bank:
    def __init__(self, name: str):
        self.name     = name
        self._accounts: dict[str, Account] = {}

    def open_account(self, owner: str, initial_deposit: float = 0.0) -> Account:
        if owner in self._accounts:
            raise ValueError(f"Account for {owner!r} already exists")
        acc = Account(owner, initial_deposit)
        self._accounts[owner] = acc
        return acc

    def get_account(self, owner: str) -> Account:
        if owner not in self._accounts:
            raise KeyError(f"No account for {owner!r}")
        return self._accounts[owner]

    def transfer(self, from_owner: str, to_owner: str, amount: float) -> None:
        src = self.get_account(from_owner)
        dst = self.get_account(to_owner)
        src.withdraw(amount)
        dst.deposit(amount)

    def total_assets(self) -> float:
        return sum(acc.balance() for acc in self._accounts.values())

    def save(self, path) -> None:
        data = {
            owner: {"balance": acc.balance(), "transactions": acc.statement()}
            for owner, acc in self._accounts.items()
        }
        Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")

    def load(self, path) -> None:
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
        for owner, info in raw.items():
            acc = Account(owner, info["balance"])
            self._accounts[owner] = acc
