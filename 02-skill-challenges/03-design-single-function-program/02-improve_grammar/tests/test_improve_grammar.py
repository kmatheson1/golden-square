# File: tests/test_improve_grammar.py
from lib.improve_grammar import improve_grammar
import pytest

"""
If we give a string with correct punctuation.
returns grammar is correct message.
"""
def test_correct_string():
    result = improve_grammar("Hello World.")
    assert result == "Your text has correct grammar."

"""
If we give a string that does not start with a capital, but does have end punctuation.
Returns grammar is not correct message.
"""
def test_start_incorrect_end_correct():
    result = improve_grammar("hello World.")
    assert result == "Your text does not have correct grammar."

"""
If we give a string that does start with a capital, but does not have correct end punctuation.
Returns grammar is not correct message.
"""
def test_start_correct_end_incorrect():
    result = improve_grammar("Hello World")
    assert result == "Your text does not have correct grammar."

"""
If we give a string that ends with a '?' and begins with a capital letter.
returns grammar is correct message.
"""
def test_start_correct_end_with_question_mark():
    result = improve_grammar("Hello World?")
    assert result == "Your text has correct grammar."

"""
If we give an empty string.
An error message is returned.
"""
def test_empty_string_gives_error_message():
    with pytest.raises(Exception) as err:
        improve_grammar("")
    error_message = str(err.value)
    assert error_message == "Cannot verify if grammar is correct if no text is given."
    