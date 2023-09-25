# File: test_design.md

"""
When we have added 2 diary entries
We get a list of all diary entries back
"""
diary = Diary()
diary_entry_1 = DiaryEntry("Monday", "I walked the dog.")
diary_entry_2 = DiaryEntry("Tuesday", "I walked the cat.")
diary.add(diary_entry_1)
diary.add(diary_entry_2)
diary.all()
# => ["Monday: I walked the dog.", "Tuesday", "I walked the cat."]

"""
When we have added 2 diary entries
A total wordcount across all diary entries can be returned
"""
diary = Diary()
diary_entry_1 = DiaryEntry("Monday", "I walked the dog.")
diary_entry_2 = DiaryEntry("Tuesday", "I walked the cat.")
diary.add(diary_entry_1)
diary.add(diary_entry_2)
diary.count_words()
# => 10

"""
If our reader wants to read all diary entries
An estimated reading time can be returned
"""
diary = Diary()
diary_entry_1 = DiaryEntry("Monday", "I walked the dog.")
diary_entry_2 = DiaryEntry("Tuesday", "I walked the cat.")
diary_entry_3 = DiaryEntry("Tuesday", "I went for a walk with my sister.")
diary.add(diary_entry_1)
diary.add(diary_entry_2)
diary.reading_time(1)
# => 18

"""
If our reader has an amount of time they can read for
The diary entry best suited for that amount of time will be returned
"""
diary = Diary()
diary_entry_1 = DiaryEntry("Monday", "I walked the dog.")
diary_entry_2 = DiaryEntry("Tuesday", "I walked the cat.")
diary_entry_3 = DiaryEntry("Tuesday", "I went for a walk with my sister.")
diary.add(diary_entry_1)
diary.add(diary_entry_2)
diary.find_best_entry_for_reading_time(1, 8)
# => "Tuesday: I went for a walk with my sister"