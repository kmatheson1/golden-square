# File: design.md

# Diary Multi-Class Planned Design Recipe


## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can record my experiences
> I want to keep a regular diary

> As a user
> So that I can reflect on my experiences
> I want to read my past diary entries

> As a user
> So that I can reflect on my experiences in my busy day
> I want to select diary entries to read based on how much time I have and my reading speed

> As a user
> So that I can keep track of my tasks
> I want to keep a todo list along with my diary

> As a user
> So that I can keep track of my contacts
> I want to see a list of all of the mobile phone numbers in all my diary entries.

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_
'''
# Nouns
diary
diary entries
time
reading speed
todo list
list of mobile phone numbers

# Verbs
read past entries (list all past entries)
select best diary entry based on read speed and time available 
see task list (complete/incomplete)
see a list of all mobile phone numbers
 ┌───────────────────────────────┐
 │Task (Todo)                    │
 │                               │
 │-task                          │
 │-complete or not complete      │
 │                               │
 │-mark complete                 │
 │                               │
 └───────────────────────────────┘
              ▲
              │
              │Owns a list of
 ┌────────────┴──────────────────┐
 │ Diary                         │
 │                               │
 │-list diary entries            │
 │-list phone numbers            │
 │-list tasks                    │
 │   - complete                  │
 │   - incomplete                │
 │-add diary entry and number    │
 │-add task                      │
 │                               │
 │-filter diary entries          │
 │     -using time and wpm       │
 │-mark all complete             │
 └─────────────┬─────────────────┘
               │
               │owns a list of
               │
               ▼
 ┌───────────────────────────────┐
 │ DiaryEntry                    │
 │                               │
 │ -title                        │
 │ -contents                     │
 │ -phonenumber                  │
 │                               │
 │ -extract number               │
 | -count words                  |
 | -reading time                 |
 │                               │
 └───────────────────────────────┘
'''

_Also design the interface of each class in more detail._
'''python
# EXAMPLE 

class Diary():
    def add_entry(self, diary_entry):
        # Parameters:
        #     diary_entry: an instance of the DiaryEntry class
        # Side-effects:
        #      Adds the diary entry to an intrnal list of task
        #      Adds any phone numbers to internal list of numbers
        pass

    def add_task(self, task):
        # Parameters:
        #       task: an instance of Todo class
        # Side-effects:
                Adds task to an internal ist of tasks
        pass

    def list_entries(self):
        # Returns:
        #       A list of all diary entries

    def list_numbers(self):
        # Returns:
        #       A list of phone numbers from diary entries
        pass
    
    def list_tasks_incomplete(self):
        # Returns:
        #       A list of tasks that have not been completed.
        pass

    def list_tasks_complete(self):
        # Returns:
        #       A list of tasks that have been completed
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #       wpm:     an integer representing the number of words the user can read per minute
        #       minutes: an integer representing the number of minutes the user has to read       
        # Returns: 
        #       An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass

    def mark_all_complete(self):
        # Side-effect:
        #       marks all tasks as complete
        pass
'''

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used._
'''python
# EXAMPLE 
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
    assert todo_list.list_tasks_incomplete() == [todo1.task, todo2.task]

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
    assert diary.list_numbers == ["07930000000", "07900000000"]

"""
If 3 diary entries containing numbers are added, 2 containing numbers
#list_numbers will return a list of the 2 numbers.
"""
def test_diary_entries_containing_numbers_return_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("Note", "Kieran's number is 07930000000")
    entry_2 = DiaryEntry("Note", "Hannah's number is 07900000000")
    entry_3 = DiaryEntry("Monday", "I walked the dog")
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    assert diary.list_numbers == ["07930000000", "07900000000"]

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
    diary_entry_3 = DiaryEntry("Tuesday", "I went for a walk with my sister.")
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
    todo_list = TodoList()
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
    assert todo_list.complete() == [todo1.task, todo2.task, todo3.task, todo4.task]
    assert diary.list_tasks_complete()

"""
If user calls #mark_all_complte when some classes are complete
All tasks are set to complete and list updated
"""
def test_mark_all_complte_when_some_complete_returns_all_in_complete_list():
    todo_list = TodoList()
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
    assert todo_list.complete() == [todo1.task, todo2.task, todo3.task, todo4.task]
    assert diary.list_tasks_complete()
    
'''

_Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail._
'''python
# EXAMPLE 

'''


_Encode each example as a test. You can add to the above list as you go._



## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._