# File: tests/test_make_snippet.py
from lib.make_snippet import *
"""
A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.
"""

"""
If passed empty string
Return empty string
"""
def test_empty_str_returns_empty_str():
    assert make_snippet("") == ""

"""
Given a string of 4 words
The 4 word string is returned
"""

def test_four_word_string():
    result = make_snippet("Hello my name is")
    assert result == "Hello my name is"

"""
Given a string of 5 words
The 5 word string is returned
"""
def test_five_word_string():
    result = make_snippet("Hello my name is Kieran")
    assert result == "Hello my name is Kieran"

"""
Given a string of 6 words
5 of the words are returned, followed by an elipsis (...)
"""
def test_six_word_string_returns_five_words_elipsis():
    result = make_snippet("Hello my name is Kieran and")
    assert result == "Hello my name is Kieran..."