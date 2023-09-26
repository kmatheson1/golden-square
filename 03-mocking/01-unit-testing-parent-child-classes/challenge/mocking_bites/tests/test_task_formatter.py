from lib.task_formatter import TaskFormatter
from unittest.mock import Mock

"""
If task is incomplete
Formatter returns - [ ] Task title
"""
def test_format_correct_if_incomplete_mock():
    mock_task = Mock()
    mock_task.title = "Walk the dog."
    mock_task.complete = False
    formatter = TaskFormatter(mock_task)
    assert formatter.format() == "- [ ] Walk the dog."

"""
If task is complete
Formatter returns - [x] Task title
"""
def test_format_correct_if_complete_mock():
    mock_task = Mock()
    mock_task.title = "Walk the dog."
    mock_task.complete = True
    formatter = TaskFormatter(mock_task)
    assert formatter.format() == "- [x] Walk the dog."
