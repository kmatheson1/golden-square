# File: tests/test_diary_entry.py
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
    assert error_message == "Cannot submit diary entry if no title orcontents given"

"""
Given title and condents
A formated string of title and content is returned
"""
def test_title_contents_format():
    diary_entry = DiaryEntry("Monday 1st September", "I went to the park with friends.")
    result = diary_entry.format()
    assert result == "Monday 1st September: I went to the park with friends."

"""
Given title and contents and readers wpm
We can see how long it would take the reader to read the contents
"""
def test_title_contents_wpm_read_time():
    diary_entry = DiaryEntry("Monday 1st September", "I went to the park with friends.")
    result = diary_entry.reading_time(1)
    assert result == 10

"""
Given wpm 2 and text length of 3
#reading_time returns 2 minutes
"""
def test_title_contents_read_time_round():
    diary_entry = DiaryEntry("Monday", "I slept")
    result = diary_entry.reading_time(2)
    assert result == 2

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
Given readers time available and wpm
returns section of contents that can be read in time available
"""
def test_reading_chunk_returns_first_chunk():
    diary_entry = DiaryEntry('Title', ' '.join('word' for i in range(0, 100)))
    result = diary_entry.reading_chunk(50, 1)
    assert result == (' '.join('word' for i in range (0, 50)))

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

"""
Given a contents of six words
If #reading_chunk is called repeadedly
The last chunk is the last words in the text, even if shorter than can be read in time.
The chunk after, is the first chunk in the text
"""
def test_reading_chunk_wraps_around_on_multiple_calls():
    diary_entry = DiaryEntry("Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 2) == 'one two three four'
    assert diary_entry.reading_chunk(2, 2) == 'five six'
    assert diary_entry.reading_chunk(2, 2) == 'one two three four'

"""
Given a contents of six words
If #reading_chunk is called repeadedly with an exact ending
The last chunk is the last words in the text, even if shorter than can be read in time.
The chunk after, is the first chunk in the text
"""
def test_reading_chunk_wraps_around_on_multiple_calls_exact_ending():
    diary_entry = DiaryEntry("Title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 2) == 'one two three four'
    assert diary_entry.reading_chunk(2, 1) == 'five six'
    assert diary_entry.reading_chunk(2, 2) == 'one two three four'