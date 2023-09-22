# File: tests/test_unit_diary.py
from lib.diary import Diary
import pytest

"""
List of entries is initially empty
"""
def test_entries_initially_empty_list():
    diary = Diary()
    assert diary.all() == []

"""
If list of entries empty
#count_words will return 0
"""
def test_entries_empty_word_count_zero():
    diary = Diary()
    assert diary.count_words() == 0

"""
If #reading_time called initially
retuns error
"""
def test_returns_error_if_reading_time_called_initially():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(1)
    assert str(e.value) == "Cannot give reading time when there are no diary entries."