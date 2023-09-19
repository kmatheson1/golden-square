# File: tests/test_count_words.py
from lib.count_words import *

"""
If an empty string is passed, returns empty string
"""
def test_count_words_for_empty_string_returns_zero():
    result = count_words("")
    assert result == 0

"""
If a single word string is passed, function returns 1
"""
def test_count_words_for_single_word_string_returns_one():
    result = count_words("one")
    assert result == 1

"""
If a two word string is passed, function returns 2
"""
def test_count_words_for_two_word_string_returns_two():
    result = count_words("one two")
    assert result == 2

"""
If a string with many words is passed, return number of words
"""
def test_count_words_returns_no_words_in_string():
    result = count_words("one two three four five six")
    assert result == 6

"""
If a string with punctuation is passed, returns no words
"""
def test_count_words_return_no_words_using_punct():
    result = count_words("one, two, three, four, five, six!")
    assert result == 6