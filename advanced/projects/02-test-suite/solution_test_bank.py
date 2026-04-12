# ============================================================
# advanced/projects/02-test-suite/solution_test_bank.py
# Run: pytest solution_test_bank.py -v --tb=short
# ============================================================

import pytest
import json
from bank import Account, Bank, InsufficientFundsError, InvalidAmountError


# ============================================================
# Fixtures
# ============================================================

@pytest.fixture
def account():
    return Account("Alice", 1000.0)

@pytest.fixture
def empty_account():
    return Account("Bob", 0.0)

@pytest.fixture
def bank():
    b = Bank("PyBank")
    b.open_account("Alice", 1000.0)
    b.open_account("Bob",   500.0)
    return b


# ============================================================
# Account.__init__
# ============================================================

def test_account_creation_valid():
    acc = Account("Alice", 500)
    assert acc.owner == "Alice"
    assert acc.balance() == 500.0

def test_account_empty_owner_raises():
    with pytest.raises(ValueError, match="empty"):
        Account("  ", 100)

def test_account_negative_balance_raises():
    with pytest.raises(ValueError, match="negative"):
        Account("Alice", -1)

def test_account_default_balance_zero():
    acc = Account("Dave")
    assert acc.balance() == 0.0

def test_account_owner_stripped():
    acc = Account("  Carol  ", 0)
    assert acc.owner == "Carol"


# ============================================================
# Account.deposit
# ============================================================

def test_deposit_increases_balance(account):
    new_bal = account.deposit(200)
    assert new_bal == 1200.0
    assert account.balance() == 1200.0

def test_deposit_zero_raises(account):
    with pytest.raises(InvalidAmountError):
        account.deposit(0)

def test_deposit_negative_raises(account):
    with pytest.raises(InvalidAmountError):
        account.deposit(-50)

def test_deposit_multiple_accumulates(empty_account):
    empty_account.deposit(100)
    empty_account.deposit(200)
    empty_account.deposit(50)
    assert empty_account.balance() == 350.0

@pytest.mark.parametrize("amount", [0, -1, -100, -0.01])
def test_deposit_invalid_amounts(account, amount):
    with pytest.raises(InvalidAmountError):
        account.deposit(amount)


# ============================================================
# Account.withdraw
# ============================================================

def test_withdraw_decreases_balance(account):
    new_bal = account.withdraw(300)
    assert new_bal == 700.0
    assert account.balance() == 700.0

def test_withdraw_exact_balance(account):
    new_bal = account.withdraw(1000.0)
    assert new_bal == 0.0

def test_withdraw_insufficient_funds(account):
    with pytest.raises(InsufficientFundsError):
        account.withdraw(2000)

def test_withdraw_error_carries_attributes(account):
    with pytest.raises(InsufficientFundsError) as exc_info:
        account.withdraw(5000)
    err = exc_info.value
    assert err.balance == 1000.0
    assert err.amount == 5000

def test_withdraw_zero_raises(account):
    with pytest.raises(InvalidAmountError):
        account.withdraw(0)

def test_withdraw_does_not_change_balance_on_error(account):
    before = account.balance()
    with pytest.raises(InsufficientFundsError):
        account.withdraw(9999)
    assert account.balance() == before


# ============================================================
# Account.statement
# ============================================================

def test_statement_empty_on_new_account(empty_account):
    assert empty_account.statement() == []

def test_statement_records_deposit(empty_account):
    empty_account.deposit(100)
    stmt = empty_account.statement()
    assert len(stmt) == 1
    assert stmt[0]["type"] == "deposit"
    assert stmt[0]["amount"] == 100

def test_statement_records_withdraw(account):
    account.withdraw(50)
    stmt = account.statement()
    assert stmt[-1]["type"] == "withdraw"
    assert stmt[-1]["amount"] == 50

def test_statement_returns_copy(account):
    account.deposit(100)
    stmt = account.statement()
    stmt.clear()   # mutate the returned list
    assert len(account.statement()) == 1   # original unchanged


# ============================================================
# Bank
# ============================================================

def test_bank_open_account_creates_account(bank):
    acc = bank.open_account("Carol", 200)
    assert acc.owner == "Carol"
    assert acc.balance() == 200

def test_bank_duplicate_account_raises(bank):
    with pytest.raises(ValueError):
        bank.open_account("Alice", 100)

def test_bank_get_account_returns_account(bank):
    acc = bank.get_account("Alice")
    assert acc.owner == "Alice"

def test_bank_get_missing_account_raises(bank):
    with pytest.raises(KeyError):
        bank.get_account("Unknown")

def test_bank_transfer_moves_money(bank):
    bank.transfer("Alice", "Bob", 200)
    assert bank.get_account("Alice").balance() == 800.0
    assert bank.get_account("Bob").balance() == 700.0

def test_bank_transfer_insufficient_funds_is_atomic(bank):
    alice_before = bank.get_account("Alice").balance()
    bob_before   = bank.get_account("Bob").balance()
    with pytest.raises(InsufficientFundsError):
        bank.transfer("Alice", "Bob", 9999)
    # Both balances unchanged
    assert bank.get_account("Alice").balance() == alice_before
    assert bank.get_account("Bob").balance() == bob_before

def test_bank_total_assets(bank):
    assert bank.total_assets() == 1500.0


# ============================================================
# Bank.save and Bank.load
# ============================================================

def test_bank_save_creates_valid_json(bank, tmp_path):
    path = tmp_path / "bank.json"
    bank.save(path)
    assert path.exists()
    data = json.loads(path.read_text())
    assert "Alice" in data
    assert data["Alice"]["balance"] == 1000.0

def test_bank_load_restores_accounts(bank, tmp_path):
    path = tmp_path / "bank.json"
    bank.save(path)
    new_bank = Bank("PyBank2")
    new_bank.load(path)
    assert new_bank.get_account("Alice").balance() == 1000.0
    assert new_bank.get_account("Bob").balance() == 500.0

def test_bank_load_missing_file_raises(tmp_path):
    b = Bank("X")
    with pytest.raises(Exception):   # FileNotFoundError or similar
        b.load(tmp_path / "missing.json")

def test_bank_total_assets_after_load(bank, tmp_path):
    path = tmp_path / "bank.json"
    bank.save(path)
    new_bank = Bank("Y")
    new_bank.load(path)
    assert new_bank.total_assets() == bank.total_assets()
