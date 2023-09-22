# File: tests/test_integration_todo_list.py
from lib.todo_list import TodoList
from lib.todo import Todo

"""
If two todo entries have been added and not complted
#incomplete returns a list of the two todo entries
"""
def test_list_incomplete_when_two_todos_added():
    todo_list = TodoList()
    todo1 = Todo("Mow the lawn.")
    todo2 = Todo("Empty the bins")
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.incomplete() == [todo1.task, todo2.task]

"""
If three todos are created.  One is marked as comlete. And added
#incomplete incomplte list and complte list correct
"""
def test_only_returns_incomplete_when_one_task_marked_complete():
    todo_list = TodoList()
    todo1 = Todo("Mow the lawn.")
    todo2 = Todo("Empty the bins")
    todo3 = Todo("Wash the car.")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    todo3.mark_complete()
    assert todo_list.incomplete() == [todo1.task, todo2.task]
    assert todo_list.complete() == [todo3.task]

"""
If all tasks are marked as complete
#incomplete returns empty, #complte returns all complete tasks
"""
def test_all_tasks_marked_complete_returns_correct_lists():
    todo_list = TodoList()
    todo1 = Todo("Mow the lawn.")
    todo2 = Todo("Empty the bins")
    todo3 = Todo("Wash the car.")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    todo1.mark_complete()
    todo2.mark_complete()
    todo3.mark_complete()
    assert todo_list.incomplete() == []
    assert todo_list.complete() == [todo1.task, todo2.task, todo3.task]

"""
If user calls #give_up when no tasks are complete
All tasks are set to complete and list updated
"""
def test_give_up_returns_all_in_complete_list():
    todo_list = TodoList()
    todo1 = Todo("Mow the lawn.")
    todo2 = Todo("Empty the bins")
    todo3 = Todo("Wash the car.")
    todo4 = Todo("Walk the dog.")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    todo_list.add(todo4)
    todo_list.give_up()
    assert todo_list.incomplete() == []
    assert todo_list.complete() == [todo1.task, todo2.task, todo3.task, todo4.task]

"""
If user calls #give_up when some classes are complete
All tasks are set to complete and list updated
"""
def test_give_up_when_some_tasks_are_complete():
    todo_list = TodoList()
    todo1 = Todo("Mow the lawn.")
    todo2 = Todo("Empty the bins")
    todo3 = Todo("Wash the car.")
    todo4 = Todo("Walk the dog.")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)
    todo_list.add(todo4)
    todo2.mark_complete()
    todo4.mark_complete()
    todo_list.give_up()
    assert todo_list.incomplete() == []
    assert todo_list.complete() == [todo1.task, todo2.task, todo3.task, todo4.task]