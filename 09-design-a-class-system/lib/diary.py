# File: lib/diary.py
from lib.diary_entry import DiaryEntry
from lib.todo import Todo

class Diary():
    def __init__(self):
        self._diary_entries = []
        self._tasks = []
        self._phonebook = []

    def add_entry(self, diary_entry):
        self._diary_entries.append(diary_entry)

    def add_task(self, task):
        self._tasks.append(task)

    def list_entries(self):
        return self._diary_entries

    def list_numbers(self):
        for entry in self._diary_entries:
            numbers = entry.extract_numbers()
            self._phonebook.extend(numbers)
        return self._phonebook
    
    def list_tasks_incomplete(self):
        return [task.task for task in self._tasks if task.complete == False]

    def list_tasks_complete(self):
        return [task.task for task in self._tasks if task.complete == True]

    def find_best_entry_for_reading_time(self, wpm, minutes):
        readable_words = minutes * wpm
        most_readable_entry = None
        longest_so_far = 0
        for entry in self._diary_entries:
            if entry.reading_time(wpm) <= readable_words:
                if entry.count_words() > longest_so_far:
                    most_readable_entry = entry
                    longest_so_far = entry.count_words()
        return most_readable_entry

    def mark_all_complete(self):
        if self._tasks == []:
            raise Exception("No tasks to give up.")

        for task in self._tasks:
            if task.complete == False:
                task.mark_complete()

diary = Diary()
entry_1 = DiaryEntry("Note", "Kieran's number is 07930000000")
entry_2 = DiaryEntry("Note", "Hannah's number is 07900000000")
diary.add_entry(entry_1)
diary.add_entry(entry_2)
print(diary.list_numbers())