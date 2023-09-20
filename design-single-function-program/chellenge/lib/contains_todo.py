# File: lib/contains_todo.py

def contains_todo(text):
    if text == "":
        raise Exception("Cannot check if text contains #TODO if no text is given.")
    
    filtered_words = []
    for word in text.split():
        filtered_letters = [letter for letter in word if letter.isalpha() or letter == '#']
        filtered_word = ''.join(filtered_letters)
        filtered_words.append(filtered_word)

    return "Your text contains #TODO." if '#TODO' in filtered_words else "Your text does not contain #TODO."
