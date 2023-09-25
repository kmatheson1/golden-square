# File: tests/test_todo_list.py
from lib.todo_list import TodoList
import pytest

"""
Upon initializing
task list contains no complete or incomplet
"""
def test_todo_list_empty_when_created():
    todo_list = TodoList()
    assert todo_list.incomplete() == []
    assert todo_list.complete() == []

"""
If #give_up called on empty task list
raises error
"""
def test_error_if_give_up_called_on_empty_list():
    todo_list = TodoList()
    with pytest.raises(Exception) as e:
        todo_list.give_up()
    assert str(e.value) == "No tasks to give up."



