# File: tests/test_todo.
from lib.todo import Todo
import pytest

"""
If task is given as empty string 
returns error message
"""
def test_empty_string_as_task_returns_error():
    with pytest.raises(Exception) as e:
        todo1 = Todo("")
    assert str(e.value) == "Cannot create task is no task is gibven."

"""
When initialized
task is set to task and complete is set to False
"""
def test_task_and_complete_false_when_instance_created():
    todo1 = Todo("Wash the car.")
    assert todo1.task == "Wash the car."
    assert todo1.complete == False

"""
When #mark_complete is called
complete property is set to true
"""
def test_mark_complete_sets_complete_to_true():
    todo1 = Todo("Wash the car.")
    todo1.mark_complete()
    assert todo1.complete == True

"""
If #mark_complete called on tasks already complete
returns error
"""
def test_error_if_mark_complete_on_complete_taks():
    todo1 = Todo("Wash the car.")
    todo1 = Todo("Wash the car.")
    todo1.mark_complete()
    with pytest.raises(Exception) as e:
        todo1.mark_complete()
    assert str(e.value) == "Task has already been marked as complete."