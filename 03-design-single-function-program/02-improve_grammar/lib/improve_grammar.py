# File: lib/improve_grammar.py

def improve_grammar(text:str):
    if not text:
        raise Exception("Cannot verify if grammar is correct if no text is given.")
    if text[0].isupper() and text[-1] in '?!.':
        return "Your text has correct grammar."
    return "Your text does not have correct grammar."
