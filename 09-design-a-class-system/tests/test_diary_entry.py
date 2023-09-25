# File: tests.test_diary_entry.py
from lib.diary_entry import DiaryEntry
import pytest

"""
If empty string for title or contents give
raises error
"""
def test_error_if_no_title_or_contents_provided():
    with pytest.raises(Exception) as e:
        entry_1 = DiaryEntry("", "")
    assert str(e.value) == "Cannot make entry if no title or contets is given."