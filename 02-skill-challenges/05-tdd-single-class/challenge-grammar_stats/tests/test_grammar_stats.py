# File: tests/test_grammar_stats.py
from lib.grammar_stats import GrammarStats
import pytest

"""
If empty string is given as text
return error message
"""
def test_error_message_for_empty_string():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check("")
    error_message = str(e.value)
    assert error_message == "Cannot assess grammar if no text is given."

"""
If we give a string with correct punctuation.
#check returns True
"""
def test_correct_string():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello World.")
    assert result == True

"""
If we give a string that does not start with a capital, but does have end punctuation.
#check returns False
"""
def test_text_start_correct_end_incorrect():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hello World.")
    assert result == False

"""
If we give a string that does start with a capital, but does not have correct end punctuation.
#check returns False
"""
def test_text_start_incorrect_end_correct():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello World")
    assert result == False

"""
For 1/1 tests checked pass
#percentage_good returns 100
"""
def test_1_success_out_of_1_is_100():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello World.")
    result = grammar_stats.percentage_good()
    assert result == 100

"""
For 0/1 tests checked pass
#percentage_good returns 0
"""
def test_1_success_out_of_1_is_100():
    grammar_stats = GrammarStats()
    grammar_stats.check("hello World")
    result = grammar_stats.percentage_good()
    assert result == 0

"""
For 1/2 tests checked pass
#percentage_good returns 50
"""
def test_1_success_out_of_2_is_50():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello World.")
    grammar_stats.check("hello World")
    result = grammar_stats.percentage_good()
    assert result == 50

"""
For 1/3 tests checked pass
#percentage_good returns int to nearest whole number
"""
def test_1_success_out_of_2_is_50():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello World.")
    grammar_stats.check("hello World")
    grammar_stats.check("hello World#")
    result = grammar_stats.percentage_good()
    assert result == 33