# File: tests.test_diary.py
from lib.diary import Diary

"""
When diary is initialized
#list_entries returns an empty list
"""
def test_list_entries_empty_when_diary_initialized():
    diary = Diary()
    assert diary.list_entries() == []
