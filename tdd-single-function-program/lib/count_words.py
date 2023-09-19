# File: lib/count_words.py
"""
A function called count_words that takes a string as an argument and returns the number of words in that string.
"""
def count_words(str):
    word_list = str.split(" ")
    return 0 if str == "" else len(word_list)