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
    #   a string detailing if a string has correct initial capitalization AND end punctuation.
    #   E.g. "Your text has correct grammar."

'''

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

'''python
# EXAMPLE 
"""
If we give a string with correct punctuation.
returns grammar is correct message.
"""
improve_grammar("Hello World.")
# => "Your text has correct grammar."

"""
If we give a string that does not start with a capital, but does have end punctuation.
Returns grammar is not correct message.
"""
improve_grammar(hello World.)
# => "Your text does not have correct grammar."

"""
If we give a string that does start with a capital, but does not have correct end punctuation.
Returns grammar is not correct message.
"""
improve_grammar(Hello World)
# => "Your text does not have correct grammar."

"""
If we give a string that ends with a '?' and begins with a capital letter.
returns grammar is correct message.
"""
improve_grammar("Hello World?")
# => "Your text has correct grammar."

"""
If we give an empty string.
An error message is returned.
"""
improve_grammar(")
# => "Cannot verify if grammar is correct if no text is given."

'''

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._