# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self._task_list = []

    def add(self, todo):
            self._task_list.append(todo)

    def incomplete(self):
        return [task.task for task in self._task_list if task.complete == False]

    def complete(self):
        return [task.task for task in self._task_list if task.complete == True]

    def give_up(self):
        if self._task_list == []:
            raise Exception("No tasks to give up.")

        for task in self._task_list:
            if task.complete == False:
                task.mark_complete()