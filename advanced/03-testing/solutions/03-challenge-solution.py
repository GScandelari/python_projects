# ============================================================
# advanced/03-testing/solutions/03-challenge-solution.py
# Run: pytest solutions/03-challenge-solution.py -v
# Requires: pip install pytest pytest-asyncio
# ============================================================

import pytest
import asyncio
from unittest.mock import Mock, patch, AsyncMock

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
    import os
    return os.environ.get("USER", os.environ.get("USERNAME", "unknown"))


def fetch_user_data(user_id, http_client):
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


async def async_fetch(url, client):
    response = await client.get(url)
    return await response.json()


async def process_items(items, processor):
    tasks = [processor(item) for item in items]
    return await asyncio.gather(*tasks)


# ============================================================
# Exercise 1 — Mock SMTP client
# ============================================================

@pytest.fixture
def smtp_mock():
    return Mock()

@pytest.fixture
def email_service(smtp_mock):
    return EmailService(smtp_mock)

def test_send_welcome_calls_smtp(email_service, smtp_mock):
    email_service.send_welcome("alice@test.com", "Alice")
    smtp_mock.send.assert_called_once_with(
        to="alice@test.com",
        subject="Welcome!",
        body="Hi Alice, welcome to our platform.",
    )

def test_send_welcome_returns_smtp_result(email_service, smtp_mock):
    smtp_mock.send.return_value = {"status": "sent", "id": "abc123"}
    result = email_service.send_welcome("bob@test.com", "Bob")
    assert result == {"status": "sent", "id": "abc123"}

def test_send_notification(email_service, smtp_mock):
    email_service.send_notification("carol@test.com", "Your order shipped!")
    smtp_mock.send.assert_called_once_with(
        to="carol@test.com",
        subject="Notification",
        body="Your order shipped!",
    )

def test_send_welcome_called_exactly_once(email_service, smtp_mock):
    email_service.send_welcome("x@test.com", "X")
    assert smtp_mock.send.call_count == 1


# ============================================================
# Exercise 2 — Monkeypatch env vars
# ============================================================

def test_get_current_user_from_USER(monkeypatch):
    monkeypatch.setenv("USER", "alice")
    monkeypatch.delenv("USERNAME", raising=False)
    assert get_current_user() == "alice"

def test_get_current_user_fallback_USERNAME(monkeypatch):
    monkeypatch.delenv("USER", raising=False)
    monkeypatch.setenv("USERNAME", "bob")
    assert get_current_user() == "bob"

def test_get_current_user_unknown(monkeypatch):
    monkeypatch.delenv("USER", raising=False)
    monkeypatch.delenv("USERNAME", raising=False)
    assert get_current_user() == "unknown"


# ============================================================
# Exercise 3 — Mock HTTP client
# ============================================================

def make_mock_response(status_code, data):
    response = Mock()
    response.status_code = status_code
    response.json.return_value = data
    return response

def test_fetch_user_data_success():
    client = Mock()
    client.get.return_value = make_mock_response(200, {"id": 1, "name": "Alice"})
    result = fetch_user_data(1, client)
    assert result == {"id": 1, "name": "Alice"}
    client.get.assert_called_once_with("/users/1")

def test_fetch_user_data_404():
    client = Mock()
    client.get.return_value = make_mock_response(404, {})
    with pytest.raises(RuntimeError, match="API error: 404"):
        fetch_user_data(99, client)

def test_fetch_user_data_500():
    client = Mock()
    client.get.return_value = make_mock_response(500, {})
    with pytest.raises(RuntimeError, match="API error: 500"):
        fetch_user_data(1, client)


# ============================================================
# Exercise 4 — Mock database in UserRepository
# ============================================================

@pytest.fixture
def mock_db():
    from unittest.mock import MagicMock
    return MagicMock()

@pytest.fixture
def repo(mock_db):
    return UserRepository(mock_db)

def test_find_by_id_calls_query(repo, mock_db):
    repo.find_by_id(42)
    mock_db.query.assert_called_once_with("SELECT * FROM users WHERE id = 42")

def test_find_by_id_returns_db_result(repo, mock_db):
    mock_db.query.return_value = {"id": 42, "name": "Alice"}
    result = repo.find_by_id(42)
    assert result == {"id": 42, "name": "Alice"}

def test_save_calls_execute(repo, mock_db):
    repo.save("test_user")
    mock_db.execute.assert_called_once_with("INSERT INTO users VALUES (test_user)")

def test_save_returns_db_result(repo, mock_db):
    mock_db.execute.return_value = True
    assert repo.save("user") is True


# ============================================================
# Exercise 5 — Testing async functions
# ============================================================

@pytest.mark.asyncio
async def test_async_fetch_success():
    mock_response = AsyncMock()
    mock_response.json.return_value = {"key": "value"}

    mock_client = AsyncMock()
    mock_client.get.return_value = mock_response

    result = await async_fetch("http://example.com/api", mock_client)
    assert result == {"key": "value"}
    mock_client.get.assert_called_once_with("http://example.com/api")

@pytest.mark.asyncio
async def test_process_items_doubles():
    async def double(x):
        return x * 2

    result = await process_items([1, 2, 3, 4, 5], double)
    assert result == [2, 4, 6, 8, 10]

@pytest.mark.asyncio
async def test_process_items_empty():
    async def identity(x):
        return x

    result = await process_items([], identity)
    assert result == []

@pytest.mark.asyncio
async def test_process_items_preserves_order():
    async def slow_double(x):
        await asyncio.sleep(0.01 * (5 - x))   # slower for smaller x
        return x * 2

    result = await process_items([1, 2, 3, 4, 5], slow_double)
    assert result == [2, 4, 6, 8, 10]   # gather preserves input order
