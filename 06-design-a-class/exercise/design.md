# File: design.md

# x Class Design Recipe


## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can keep track of my tasks
> I want a program that I can add todo tasks to and see a list of them.

> As a user
> So that I can focus on tasks to complete.
> I want to mark tasks as complete and have them disappear from the list.

* Only at tasks that contain '#TODO'
* Can return a list of tasks added.
* If task is marked as complete, task is removed from the list of tasks.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

'''python
# EXAMPLE 

class TaskTracker():
    def add(self, task):
        # Parameters:
        #   a human-readable text as a string representing a task
        # Returns nothing
        pass

    def list_incomplete(self):
        # parameters:
        #   none
        # Returns:
        #   A list of incomplete tasks
        pass

    def mark_complete(self, index):
        # parameters:
        #   An integer representing the task to mark complete
        # Side-effect:
        #   removes task from index at list of tasks
        pass

'''

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._
_Encode each example as a test. You can add to the above list as you go._

'''python
# EXAMPLE 

"""
initially there are no tasks
"""
task_tracker = TaskTracker()
task_tracker.list_incomplete() 
# => []

"""
When we add a task
It is reflected in the list of tasks
"""
task_tracker = TaskTracker()
task_tracker.add("Do the washing up.")
task_tracker.list_incomplete()
# => ["Do the washing up."]

"""
When we add multiple tasks task
All are reflected in the list of tasks
"""
task_tracker = TaskTracker()
task_tracker.add("Do the washing up.")
task_tracker.add("Walk the dog.")
task_tracker.list_incomplete()
# => ["Do the washing up.", "Walk the dog."]

"""
When we mark a task as complete
The task is removed from the list
"""
task_tracker = TaskTracker()
task_tracker.add("Do the washing up.")
task_tracker.add("Walk the dog.")
task_tracker.add("Wash the car.")
task_tracker.mark_complete(1)
task_tracker.list_incomplete()
# => ["Do the washing up.", "Wash the car."]

"""
If we try to mark a task that does not exist as complte
Raises an error (too low)
"""
task_tracker = TaskTracker()
task_tracker.add("Do the washing up.")
task_tracker.mark_complete(-1)
task_tracker.list_incomplete()
# => Exception("Cannot mark a task that does not exist as complete")
# => ["Do the washing up."]

"""
If we try to mark a task that does not exist as complte
Raises an error (too high)
"""
task_tracker = TaskTracker()
task_tracker.add("Do the washing up.")
task_tracker.add("Wash the car.")
task_tracker.mark_complete(2)
task_tracker.list_incomplete()
# => Exception("Cannot mark a task that does not exist as complete")
# => ["Do the washing up.", "Wash the car."]

'''

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._