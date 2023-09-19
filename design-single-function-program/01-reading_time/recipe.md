# Reading Time Method Design Recipe


## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can manage my time
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Method Signature

_Include the name of the function, its parameters, return value, and side effects._

'''python
# EXAMPLE 

def reading_time(text):
    # Parameters:
    #   text: a string containing words e.g. a piece of text containing 4000 words
    #Return:
    #   a string detailing how many minutes it will take to read the given text
    #   E.g. "Reading time will be: 0:20:00"

'''

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

'''python
# EXAMPLE 
"""
If we give an empty string.
It will return an error "Cannot give reading time when no text is given"
"""
reading_time("")
# => ""Reading time will be: 0:00:00"

"""
If we give a string containing 1 word.
It will return time in minutes ""Reading time will be: 0:00:00".
"""
reading_time("word")
# => ""Reading time will be: 0:00:00"

"""
If we give a string containing 50 words.
It will return time in minutes ""Reading time will be: 0:00:15".
"""
reading_time("word")
# => ""Reading time will be: 0:00:15"

"""
If we give a string containing 200 words.
It will return time in minutes ""Reading time will be: 0:01:00".
"""
reading_time("word")
# => ""Reading time will be: 0:01:00"

"""
If we give a string containing 50 words in paragraphs
It will return time in minutes ""Reading time will be: 0:00:15".
"""
# => ""Reading time will be: 0:00:15"

'''

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


