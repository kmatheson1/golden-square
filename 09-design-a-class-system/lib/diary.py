# File: lib/diary.py
from lib.diary_entry import DiaryEntry
from lib.todo import Todo

class Diary():
    def __init__(self):
        self.diary_entries = []
        self.tasks = []
        self.phonebook = []

    def add_entry(self, diary_entry):
        self.diary_entries.append(diary_entry)

    def add_task(self, task):
        self.tasks.append(task)

    def list_entries(self):
        return self.diary_entries

    def list_numbers(self):
        for entry in self.diary_entries:
            numbers = entry.extract_numbers()
            self.phonebook.extend(numbers)
        return self.phonebook
    
    def list_tasks_incomplete(self):
        return [task.task for task in self.tasks if task.complete == False]

    def list_tasks_complete(self):
        return [task.task for task in self.tasks if task.complete == True]

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

diary = Diary()
entry_1 = DiaryEntry("Note", "Kieran's number is 07930000000")
entry_2 = DiaryEntry("Note", "Hannah's number is 07900000000")
diary.add_entry(entry_1)
diary.add_entry(entry_2)
print(diary.list_numbers())