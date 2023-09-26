# File: tests/test_diary.py
from lib.diary import Diary

def test_read_diary_returns_contents():
    diary = Diary("This is a secret.")
    assert diary.read() == "This is a secret."