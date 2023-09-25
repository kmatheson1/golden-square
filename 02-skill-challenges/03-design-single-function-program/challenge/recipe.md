# File: recipe.md

# Contains #TODO Method Design Recipe


## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So I can keep track of my tasks
> I want to check if a text includes the string #TODO

## 2. Design the Method Signature

_Include the name of the function, its parameters, return value, and side effects._

'''python
# EXAMPLE 
    # Parameters:
    #   text: a string containing words
    #Return:
    #   A confirmation if the text contains or does not contain '#TODO' in the form of a string.
    #   E.g. 'Your text contains #TODO.'
    #   E.g. 'Your text does not contain #TODO.'

'''

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

'''python
# EXAMPLE 

"""
If given a string that does not contain '#TODO'
return string confirming text does not contain '#TODO'
"""
contains_todo("Take the bins out.")
# => 'Your text does not contain #TODO.'

"""
If given a string that contains '#TODO'
return string confirming that text does contain '#TODO'
"""
contains_todo("#TODO Take the bins out.")
# => 'Your text contains #TODO.'

"""
If given a string where '#TODO' is in the text but not the first word
return string confirming that text does contain '#TODO'
"""
contains_todo("Take the #TODO bins out.")
# => 'Your text contains #TODO.'

"""
If given a string where '#TODO' is directly followed by punctuation e.g. '#TODO:'
return string confirming that text does contain '#TODO'
"""
contains_todo("#TODO: Take the bins out.")
# => 'Your text contains #TODO.'

"""
If given an empty string
Return error message
"""
contains_todo("")
# => 'Cannot check if text contains #TODO if no text is given'

'''

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._