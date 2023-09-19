# File: recipe.md
# Improve Grammar Method Design Recipe


## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can improve my grammar
> I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Method Signature

_Include the name of the function, its parameters, return value, and side effects._

'''python
# EXAMPLE 
    # Parameters:
    #   text: a string containing words
    #Return:
    #   a string detailing if a string has correct initial capitalization and end punctuation.
    #   E.g. "Your text starts with a capital letter and ends with suitable punctuation."

'''

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

'''python
# EXAMPLE 
"""
If we give a string with correct punctuation.
it will return verification message.
"""
improve_grammar(Hello World!)
# => "Your text starts with a capital letter and ends with suitable punctuation."

"""
If we give a string that does not start with a capital, but does have end punctuation.
Returns not verified message.
"""
improve_grammar(hello World!)
# => "Your text does not start with a capital letter and end with suitable punctuation."

"""
If we give a string that does start with a capital, but does not have correct end punctuation.
Returns not verified message.
"""
improve_grammar(hello World!)
# => "Your text does not start with a capital letter and end with suitable punctuation."

"""
If we give an empty string.
An error message is returned.
"""
improve_grammar(")
# => "Cannot verify if grammar is correct if no text is given"

'''

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._