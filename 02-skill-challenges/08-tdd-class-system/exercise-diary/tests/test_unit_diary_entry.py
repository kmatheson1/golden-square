# File: tests/test_unit_diary_entry
from lib.diary_entry import DiaryEntry
import pytest

"""
Given an empty title and contents
Raises an error
"""
def test_errors_on_empty_title_and_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "")
    error_message = str(e.value)
    assert error_message == "Cannot submit diary entry if no title or contents given."

"""
When DiaryEntry initialized
Title and contents are stored as public variables
"""
def test_title_contents_accessed_once_initialized():
    diary_entry = DiaryEntry("Monday", "I walked the dog.")
    assert diary_entry.title == "Monday"
    assert diary_entry.contents == "I walked the dog."

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

"""
Given readers time, 1, available and wpm, 50, and contents of 100 words
First time, #reading_chunk returns first 50 words
Second time, #reading_chunk returns second 50 words
"""
def test_reading_chunk_returns_second_chunk():
    diary_entry = DiaryEntry("Title", (' '.join('one' for i in range(0, 50))) + ' ' + (' '.join('two' for i in range(0, 50))))
    assert diary_entry.reading_chunk(50, 1) == (' '.join('one' for i in range (0, 50)))
    assert diary_entry.reading_chunk(50, 1) == (' '.join('two' for i in range (0, 50)))

"""
Return correct chunks when wpm varies each #reading_chunk
"""
def test_reading_chunk_returns_chunks_with_varied_wpm():
    diary_entry = DiaryEntry("Title", 'one two three four five six seven eight nine ten eleven twelve')
    assert diary_entry.reading_chunk(2, 1) == 'one two'
    assert diary_entry.reading_chunk(1, 1) == 'three'
    assert diary_entry.reading_chunk(2, 1) == 'four five'
    assert diary_entry.reading_chunk(3, 1) == 'six seven eight'

"""
Return correct chunks when time varies between #reading_chunk
"""
def test_reading_chunk_returns_chunks_with_varied_time():
    diary_entry = DiaryEntry("Title", 'one two three four five six seven eight nine ten eleven twelve')
    assert diary_entry.reading_chunk(2, 1) == 'one two'
    assert diary_entry.reading_chunk(1, 1) == 'three'
    assert diary_entry.reading_chunk(2, 1) == 'four five'
    assert diary_entry.reading_chunk(3, 1) == 'six seven eight'
    assert diary_entry.reading_chunk(2, 2) == 'nine ten eleven twelve'