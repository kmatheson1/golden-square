# File tests/test_contains_todo.py
from lib.contains_todo import contains_todo
import pytest

"""
If given a string that does not contain '#TODO'
return string confirming text does not contain '#TODO'
"""
def test_text_does_not_contain_todo():
    result = contains_todo("Take the bins out")
    assert result == "Your text does not contain #TODO."

"""
If given a string that contains '#TODO'
return string confirming that text does contain '#TODO'
"""
def test_text_first_word_is_todo():
    result = contains_todo("#TODO Take the bins out.")
    assert result == "Your text contains #TODO."

"""
If given a string where '#TODO' is in the text but not the first word
return string confirming that text does contain '#TODO'
"""
def test_text_contains_todo_any_position():
    result = contains_todo("Take the #TODO bins out.")
    assert result == "Your text contains #TODO."

"""
If given a string where '#TODO' is directly followed by punctuation e.g. '#TODO:'
return string confirming that text does contain '#TODO'
"""
def test_text_contains_todo_with_punct():
    result = contains_todo("#TODO: Take the bins out.")
    assert result == "Your text contains #TODO."

"""
If given an empty string
Return error message
"""
def test_empty_string_returns_error():
    with pytest.raises(Exception) as err:
        contains_todo("")
    error_message = str(err.value)
    assert error_message == "Cannot check if text contains #TODO if no text is given."
