# File: tests/test_diary_integration.py
from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
When we have added 2 diary entries
We get a list of all diary entries back
"""
def test_list_2_diary_entries():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Monday", "I walked the dog.")
    diary_entry_2 = DiaryEntry("Tuesday", "I walked the cat.")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.all() == [diary_entry_1, diary_entry_2]

"""
When we have added 2 diary entries
call #count_words
A total wordcount across all diary entries can be returned
"""
def test_total_word_count_of_multiple_entries():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Monday", "I walked the dog.")
    diary_entry_2 = DiaryEntry("Tuesday", "I walked the cat, then went home.")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.count_words() == 11

"""
If our reader wants to read all diary entries
An estimated reading time can be returned
"""
def test_total_reading_time_of_all_entries():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Monday", "I walked the dog.")
    diary_entry_2 = DiaryEntry("Tuesday", "I walked the cat.")
    diary_entry_3 = DiaryEntry("Tuesday", "I went for a walk with my sister.")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    assert diary.reading_time(1) == 16

"""
If our reader wants to read all diary entries and they have a total length of 15.  My readers wpm is 2
An estimated reading time of 8 is returned
"""
def test_total_reading_time_of_all_entries_odd_length():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Monday", "I walked the dog.")
    diary_entry_2 = DiaryEntry("Tuesday", "I walked the cat.")
    diary_entry_3 = DiaryEntry("Tuesday", "I went for a walk with Jason.")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    assert diary.reading_time(2) == 8

"""
If our reader has an amount of time they can read for
The diary entry best suited for that amount of time will be returned
"""
def test__time_eight_wpm_one_entry_closest_to_eight_returned():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Monday", "I walked the dog.")
    diary_entry_2 = DiaryEntry("Tuesday", "I walked the cat.")
    diary_entry_3 = DiaryEntry("Tuesday", "I went for a walk with my sister.")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    result = diary.find_best_entry_for_reading_time(1, 8)
    assert result == diary_entry_3

"""
If no readable entries in the time given are found
return none
"""
def test_return_none_if_no_entries_readable():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Monday", "I walked the dog.")
    diary_entry_2 = DiaryEntry("Tuesday", "I walked the cat.")
    diary_entry_3 = DiaryEntry("Tuesday", "I went for a walk with my sister.")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    result = diary.find_best_entry_for_reading_time(1, 1)
    assert result == None