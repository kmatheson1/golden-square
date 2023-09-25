# File: lib/diary_entry.py
import re

class DiaryEntry():
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Cannot make entry if no title or contets is given.")

        self.title = title
        self.contents = contents 

    def extract_numbers(self):
        number_list = []
        numbers = re.findall(r'\b0[0-9]{10}\b', self.contents)
        number_list += numbers
        return number_list

