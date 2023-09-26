# File: tests/test_secret_diary.py
from unittest.mock import Mock
from lib.secret_diary import SecretDiary
import pytest

def test_error_if_locked_mock():
    mock_diary = Mock()
    secret_diary = SecretDiary(mock_diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == "Go away!"

def test_diary_read_if_unlocked_mock():
    mock_diary = Mock()
    secret_diary = SecretDiary(mock_diary)
    mock_diary.read.return_value = "This is a secret."
    secret_diary.unlock()
    assert secret_diary.read() == "This is a secret."

def test_unlocks_then_locks_read_error_mock():
    mock_diary = Mock()
    secret_diary = SecretDiary(mock_diary)
    mock_diary.read.return_value = "This is a secret."
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == "Go away!"