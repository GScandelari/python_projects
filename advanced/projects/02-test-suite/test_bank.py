# ============================================================
# advanced/projects/02-test-suite/test_bank.py
# Your task: write a complete test suite for bank.py
# Run: pytest test_bank.py -v
# ============================================================

import pytest
from bank import Account, Bank, InsufficientFundsError, InvalidAmountError


# ============================================================
# TODO: Write fixtures for Account and Bank
# ============================================================

# ============================================================
# TODO: Test Account.__init__
#   - Valid creation
#   - Empty owner raises ValueError
#   - Negative balance raises ValueError
# ============================================================

# ============================================================
# TODO: Test Account.deposit
#   - Positive amount increases balance and returns new balance
#   - Zero raises InvalidAmountError
#   - Negative raises InvalidAmountError
#   - Multiple deposits accumulate correctly
# ============================================================

# ============================================================
# TODO: Test Account.withdraw
#   - Valid withdrawal decreases balance
#   - Insufficient funds raises InsufficientFundsError
#   - Verify error carries .balance and .amount attributes
#   - Zero raises InvalidAmountError
#   - Exact balance withdrawal (edge case)
# ============================================================

# ============================================================
# TODO: Test Account.statement
#   - Empty on new account
#   - Records correct type and amount per transaction
#   - Returns a copy (mutations don't affect the account)
# ============================================================

# ============================================================
# TODO: Test Bank
#   - open_account creates and returns an Account
#   - Duplicate open_account raises ValueError
#   - get_account returns correct Account
#   - get_account for missing owner raises KeyError
#   - transfer moves money correctly between accounts
#   - transfer with insufficient funds raises InsufficientFundsError
#     and leaves BOTH accounts unchanged (atomicity check)
#   - total_assets returns sum of all balances
# ============================================================

# ============================================================
# TODO: Test Bank.save and Bank.load with tmp_path
#   - save writes a valid JSON file
#   - load restores accounts with correct balances
#   - load on missing file raises an appropriate exception
# ============================================================
