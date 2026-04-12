# ============================================================
# advanced/03-testing/exercises/03-challenge.py
# Topic: Testing with pytest — mocking, monkeypatching, async
# Difficulty: Challenge
# ============================================================
#
# Run with: pytest exercises/03-challenge.py -v
# ============================================================

import pytest
import asyncio
import json
import time
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path


# --- Code under test ---

class EmailService:
    def __init__(self, smtp_client):
        self._smtp = smtp_client

    def send_welcome(self, user_email, user_name):
        subject = "Welcome!"
        body = f"Hi {user_name}, welcome to our platform."
        return self._smtp.send(to=user_email, subject=subject, body=body)

    def send_notification(self, user_email, message):
        return self._smtp.send(to=user_email, subject="Notification", body=message)


def get_current_user():
    """Returns the OS username (reads env var / OS)."""
    import os
    return os.environ.get("USER", os.environ.get("USERNAME", "unknown"))


def fetch_user_data(user_id: int, http_client) -> dict:
    """Fetch a user dict from an HTTP API."""
    response = http_client.get(f"/users/{user_id}")
    if response.status_code != 200:
        raise RuntimeError(f"API error: {response.status_code}")
    return response.json()


class UserRepository:
    def __init__(self, db):
        self._db = db

    def find_by_id(self, user_id):
        return self._db.query(f"SELECT * FROM users WHERE id = {user_id}")

    def save(self, user):
        return self._db.execute(f"INSERT INTO users VALUES ({user})")


async def async_fetch(url: str, client) -> dict:
    """Async function that fetches JSON from a URL."""
    response = await client.get(url)
    return await response.json()


async def process_items(items: list, processor) -> list:
    """Process a list of items concurrently."""
    tasks = [processor(item) for item in items]
    return await asyncio.gather(*tasks)


# ============================================================
# Exercise 1 — Mock the SMTP client in EmailService
# Write tests that:
#   - Verify send_welcome calls smtp.send with correct args
#   - Verify send_notification calls smtp.send with correct args
#   - Test that the return value of smtp.send is passed through
#   - Verify smtp.send is called exactly once per method call
# Use Mock() objects — do NOT create a real smtp client.
# ============================================================

# Write your code here


# ============================================================
# Exercise 2 — Monkeypatch environment variables
# Write tests for get_current_user():
#   - Returns the value of USER env var when set
#   - Returns the value of USERNAME env var as fallback
#   - Returns "unknown" when neither is set
# Use monkeypatch.setenv / monkeypatch.delenv.
# ============================================================

# Write your code here


# ============================================================
# Exercise 3 — Mock an HTTP client
# Write tests for fetch_user_data():
#   - Returns a dict when the API responds with status 200
#   - Raises RuntimeError when status is 404
#   - Raises RuntimeError when status is 500
# Build a mock http_client with mock response objects.
# ============================================================

# Write your code here


# ============================================================
# Exercise 4 — Mock a database in UserRepository
# Write tests that:
#   - find_by_id calls db.query with the correct SQL string
#   - save calls db.execute with the correct SQL string
#   - Verify the return value passes through from the mock
# Use MagicMock for the db so it supports any attribute access.
# ============================================================

# Write your code here


# ============================================================
# Exercise 5 — Testing async functions
# Write pytest tests for async_fetch and process_items.
# Use pytest-asyncio or pytest's native asyncio support:
#   @pytest.mark.asyncio
#   async def test_something(): ...
#
# For async_fetch:
#   - Mock the async client and response
#   - Verify the returned dict matches the mock response
#
# For process_items:
#   - Use a mock async processor that doubles each item
#   - Verify all items are processed and returned in order
#
# Note: you may need: pip install pytest-asyncio
# ============================================================

# Write your code here
