# File: tests/test_integration_secret_diary.py
from lib.secret_diary import SecretDiary
from lib.diary import Diary
import pytest

"""
If diary is locked
raises the error "Go away!"
"""
def test_error_if_diary_locked():
    diary = Diary("This is a secret.")
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == "Go away!"

"""
If diary is unlocked and then read
Returns contents
"""
def test_read_if_diary_is_unlocked():
    diary = Diary("This is a secret.")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "This is a secret."

"""
If diary is unlocked and then locked again
returns error
"""
def test_unlocks_then_locks_read_error():
    diary = Diary("This is a secret.")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    assert str(e.value) == "Go away!"