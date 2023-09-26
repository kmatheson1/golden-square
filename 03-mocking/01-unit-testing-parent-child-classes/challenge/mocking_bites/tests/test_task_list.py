from unittest.mock import Mock
from lib.task_list import TaskList


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour

def test_adds_tasks_to_list_mock():
    task_list = TaskList()
    task_1_mock = Mock()
    task_2_mock = Mock()
    task_1_mock.add.return_value = "Walk the dog."
    task_2_mock.add.return_value = "Walk the cat."
    task_list.add(task_1_mock)
    task_list.add(task_2_mock)
    assert task_list.tasks == [task_1_mock, task_2_mock]


def test_all_complete_false_when_not():
    task_list = TaskList()
    task_1_mock = Mock()
    task_2_mock = Mock()
    task_1_mock.is_complete.return_value = True
    task_1_mock.is_complete.return_value = False
    task_list.add(task_1_mock)
    task_list.add(task_2_mock)
    task_1_mock.mark_complete()
    assert task_list.all_complete() == False

def test_all_complete_false_when_all():
    task_list = TaskList()
    task_1_mock = Mock()
    task_2_mock = Mock()
    task_1_mock.is_complete.return_value = True
    task_1_mock.is_complete.return_value = True
    task_list.add(task_1_mock)
    task_list.add(task_2_mock)
    task_1_mock.mark_complete()
    assert task_list.all_complete() == True