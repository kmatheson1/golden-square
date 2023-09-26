class TaskFormatter:
    def __init__(self, task): # task is an instance of Task
        self._task = task

    def format(self):
        if not self._task.complete:
            return f"- [ ] {self._task.title}"
        return f"- [x] {self._task.title}"
        