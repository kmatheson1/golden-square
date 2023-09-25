# File: tests.test_integration_diary.py
from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.todo import Todo

"""
When we have added 2 diary entries
We get a list of all diary entries back
"""
def test_list_2_diary_entries():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Monday", "I walked the dog.")
    diary_entry_2 = DiaryEntry("Tuesday", "I walked the cat.")
    diary.add_entry(diary_entry_1)
    diary.add_entry(diary_entry_2)
    assert diary.list_entries() == [diary_entry_1, diary_entry_2]

"""
If two todo entries have been added and not complted
#incomplete returns a list of the two todo entries
"""
def test_list_incomplete_when_two_todos_added():
    diary = Diary()
    todo1 = Todo("Mow the lawn.")
    todo2 = Todo("Empty the bins")
    diary.add_task(todo1)
    diary.add_task(todo2)
    assert diary.list_tasks_incomplete() == [todo1.task, todo2.task]

"""
If three todos are created.  One is marked as complete.
#incomplete incomplete list and complete list correct
"""
def test_only_returns_incomplete_when_one_task_marked_complete():
    diary = Diary()
    todo1 = Todo("Mow the lawn.")
    todo2 = Todo("Empty the bins")
    todo3 = Todo("Wash the car.")
    diary.add_task(todo1)
    diary.add_task(todo2)
    diary.add_task(todo3)
    todo3.mark_complete()
    assert diary.list_tasks_incomplete() == [todo1.task, todo2.task]
    assert diary.list_tasks_complete() == [todo3.task]

"""
If 2 diary entries containing numbers are added.
#list_numbers will return a list of those numbers.
"""
def test_diary_entries_containing_numbers_return_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("Note", "Kieran's number is 07930000000")
    entry_2 = DiaryEntry("Note", "Hannah's number is 07900000000")
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    assert diary.list_numbers() == ["07930000000", "07900000000"]



"""
If 3 diary entries containing numbers are added, 2 containing numbers
#list_numbers will return a list of the 2 numbers.
"""
def test_3_diary_entries_containing_2_numbers_return_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("Note", "Kieran's number is 07930000000")
    entry_2 = DiaryEntry("Note", "Hannah's number is 07900000000")
    entry_3 = DiaryEntry("Monday", "I walked the dog")
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    assert diary.list_numbers() == ["07930000000", "07900000000"]


"""
If our reader has an amount of time they can read for
The diary entry best suited for that amount of time will be returned
"""
def test__time_eight_wpm_one_entry_closest_to_eight_returned():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Monday", "I walked the dog.")
    diary_entry_2 = DiaryEntry("Tuesday", "I walked the cat.")
    diary_entry_3 = DiaryEntry("Tuesday", "I went for a walk with my sister.")
    diary.add_entry(diary_entry_1)
    diary.add_entry(diary_entry_2)
    diary.add_entry(diary_entry_3)
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
    diary_entry_3 = DiaryEntry("Tuesday", "I went for a walk with #my sister.")
    diary.add_entry(diary_entry_1)
    diary.add_entry(diary_entry_2)
    diary.add_entry(diary_entry_3)
    result = diary.find_best_entry_for_reading_time(1, 1)
    assert result == None



"""
If user calls #mark_all_complete when no tasks are complete
All tasks are set to complete and list updated
"""
def test_mark_all_complete_returns_all_in_complete_list():
    diary = Diary()
    todo1 = Todo("Mow the lawn.")
    todo2 = Todo("Empty the bins")
    todo3 = Todo("Wash the car.")
    todo4 = Todo("Walk the dog.")
    diary.add_task(todo1)
    diary.add_task(todo2)
    diary.add_task(todo3)
    diary.add_task(todo4)
    diary.mark_all_complete()
    assert diary.list_tasks_incomplete() == []
    assert diary.list_tasks_complete() == [todo1.task, todo2.task, todo3.task, todo4.task]
    assert diary.list_tasks_complete()

"""
If user calls #mark_all_complte when some classes are complete
All tasks are set to complete and list updated
"""
def test_mark_all_complte_when_some_complete_returns_all_in_complete_list():
    diary = Diary()
    todo1 = Todo("Mow the lawn.")
    todo2 = Todo("Empty the bins")
    todo3 = Todo("Wash the car.")
    todo4 = Todo("Walk the dog.")
    diary.add_task(todo1)
    diary.add_task(todo2)
    diary.add_task(todo3)
    diary.add_task(todo4)
    diary.mark_all_complete()
    assert diary.list_tasks_incomplete() == []
    assert diary.list_tasks_complete() == [todo1.task, todo2.task, todo3.task, todo4.task]
    assert diary.list_tasks_complete()