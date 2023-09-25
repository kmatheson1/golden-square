# File: tests.test_diary.py
from lib.diary import Diary
import pytest

"""
When diary is initialized
#list_entries returns an empty list
#list_tasks_incomplete returns an empty list
#list_tasks_complete returns an empty list
#list_numbers returns an empty list
"""
def test_list_entries_empty_when_diary_initialized():
    diary = Diary()
    assert diary.list_entries() == []
    assert diary.list_numbers() == []
    assert diary.list_tasks_incomplete() == []
    assert diary.list_tasks_complete() == []

"""
If #give_up called on empty task list
raises error
"""
def test_error_if_mark_all_complete_called_on_empty_list():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.mark_all_complete()
    assert str(e.value) == "No tasks to give up."
