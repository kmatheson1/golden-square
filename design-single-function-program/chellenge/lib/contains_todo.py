# File: lib/contains_todo.py

def contains_todo(text):
    words = text.split()
    if '#TODO' in words:
        return "Your text contains #TODO."
    else:
        return "Your text does not contain #TODO."