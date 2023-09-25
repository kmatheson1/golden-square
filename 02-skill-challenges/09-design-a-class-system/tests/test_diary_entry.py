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

def test_contents_and_title_set_public():
    entry = DiaryEntry("Monday", "Walked the dog.")
    assert entry.title == "Monday"
    assert entry.contents == "Walked the dog."

def test_empty_list_if_entry_contains_no_numbers():
    entry = DiaryEntry("Monday", "Walked the dog.")
    assert entry.extract_numbers() == []

def test_number_not_extracted_if_doest_start_with_zero():
    entry = DiaryEntry("Note", "Kieran's number is 77777777777")
    assert entry.extract_numbers() == []

def test_number_not_extracted_if_longer_than_ten_digits():
    entry = DiaryEntry("Note", "Kieran's number is 7777777777788")
    assert entry.extract_numbers() == []

def test_number_not_extracted_if_shorter_than_ten_digits():
    entry = DiaryEntry("Note", "Kieran's number is 7777777")
    assert entry.extract_numbers() == []

def test_multiple_numbers_extracted():
    entry = DiaryEntry("Note", "Kieran's number is 08930000000, Hannah's number is 07900000000")
    assert entry.extract_numbers() == ["08930000000", "07900000000"]

"""
when a DiaryEntry is instanciated 
#count_words returns a count of the contents 
"""
def test_count_contents_of_diary_entry():
    diary_entry = DiaryEntry("Monday", "I walked the dog.")
    assert diary_entry.count_words() == 4

"""
When diary entry with contents length 4 and readers wpm is 1
An estimate of reading time in minutes of 4 is returned
"""
def test_estimate_reading_time_of_contents():
    diary_entry = DiaryEntry("Tuesday", "I walked the dog.")
    assert diary_entry.reading_time(1) == 4

"""
When diary entry with contents length 3 and readers wpm is 2
An estimate of reading time in minutes of 2 is returned
"""
def test_estimate_reading_time_of_contents():
    diary_entry = DiaryEntry("Tuesday", "I went shopping.")
    assert diary_entry.reading_time(2) == 2

"""
Given a wpm of 0
#reading_time Raises an error
"""
def test_wpm_zero_returns_error():
    diary_entry = DiaryEntry("Monday", "I slept")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    error_message = str(e.value)
    assert error_message == "Cannot calculate reading time if reader cannot read"