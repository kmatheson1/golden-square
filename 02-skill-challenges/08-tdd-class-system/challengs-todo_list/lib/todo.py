# File: lib/todo.py
class Todo:
    def __init__(self, task):
        if task == "":
            raise Exception("Cannot create task is no task is gibven.")

        self.task = task
        self.complete = False

    def mark_complete(self):
        if self.complete == True:
            raise Exception("Task has already been marked as complete.")
        self.complete = True
        