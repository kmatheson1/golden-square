# File: lib/diary_entry.py
import math

class DiaryEntry():
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Cannot submit diary entry if no title orcontents given")
        
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def format(self):
        return f'{self.title}: {self.contents}'
    
    def count_words(self):
        words = len(self.format().split())
        return words
    
    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Cannot calculate reading time if reader cannot read")
        reading_time = self.count_words() / wpm
        return math.ceil(reading_time)
    
    def reading_chunk(self, wpm, minutes):
        read_in_time = wpm * minutes
        words = self.contents.split()
        if self.read_so_far >= len(words):
            self.read_so_far = 0

        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + read_in_time
        chunk = words[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return ' '.join(chunk)