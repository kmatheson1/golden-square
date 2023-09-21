# File:  lib/task_tracker.py

class TaskTracker():
    def __init__(self):
        self._list_tasks = []
        

    def add(self, task):
        self._list_tasks.append(task)

    def list_incomplete(self):
        return self._list_tasks

    def mark_complete(self, index):
        if len(self._list_tasks) == 1 and index < 0:
            raise Exception("Cannot mark a task that does not exist as complete.")
        elif index >= len(self._list_tasks):
            raise Exception("Cannot mark a task that does not exist as complete.")

        self._list_tasks.pop(index)