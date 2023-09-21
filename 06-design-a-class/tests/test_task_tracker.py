# File: tests/test_task_tracker.py
from lib.task_tracker import TaskTracker
import pytest 

"""
initially there are no tasks
"""
def test_list_if_no_tasks():
    task_tracker = TaskTracker()
    result = task_tracker.list_incomplete() 
    assert result == []

"""
When we add a task
It is reflected in the list of tasks
"""
def test_list_one_tasks():
    task_tracker = TaskTracker()
    task_tracker.add("Do the washing up.")
    result = task_tracker.list_incomplete()
    assert result == ["Do the washing up."]

"""
When we add multiple tasks task
All are reflected in the list of tasks
"""
def test_list_multiple_tasks_added():
    task_tracker = TaskTracker()
    task_tracker.add("Do the washing up.")
    task_tracker.add("Walk the dog.")
    result = task_tracker.list_incomplete()
    assert result == ["Do the washing up.", "Walk the dog."]

"""
When we mark a task as complete
The task is removed from the list
"""
def test_remove_complete_task_from_list():
    task_tracker = TaskTracker()
    task_tracker.add("Do the washing up.")
    task_tracker.add("Walk the dog.")
    task_tracker.add("Wash the car.")
    task_tracker.mark_complete(1)
    result = task_tracker.list_incomplete()
    assert result == ["Do the washing up.", "Wash the car."]

"""
If we try to mark a task that does not exist as complte
Raises an error (too low)
"""
def test_remove_index_too_low_returns_error():
    task_tracker = TaskTracker()
    task_tracker.add("Do the washing up.")
    with pytest.raises(Exception) as e: 
        task_tracker.mark_complete(-1)
    error_message = str(e.value)
    assert error_message == "Cannot mark a task that does not exist as complete."
    result = task_tracker.list_incomplete()
    assert result == ["Do the washing up."]

"""
If we try to mark a task that does not exist as complte
Raises an error (too high)
"""
def test_remove_index_too_low_returns_error():
    task_tracker = TaskTracker()
    task_tracker.add("Do the washing up.")
    task_tracker.add("Wash the car.")
    with pytest.raises(Exception) as e: 
        task_tracker.mark_complete(2)
    error_message = str(e.value)
    assert error_message == "Cannot mark a task that does not exist as complete."
    result = task_tracker.list_incomplete()
    assert result == ["Do the washing up.", "Wash the car."]