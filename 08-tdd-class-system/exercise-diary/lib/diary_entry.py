# File: lib/diary_entry.py
import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Cannot submit diary entry if no title or contents given.")

        self.title = title
        self.contents = contents
        self._read_so_far = 0

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Cannot calculate reading time if reader cannot read")

        reading_time = self.count_words() / wpm
        return math.ceil(reading_time)

    def reading_chunk(self, wpm, minutes):
        read_in_time = wpm * minutes
        words = self.contents.split()
        if self._read_so_far >= len(words):
            self._read_so_far = 0

        chunk_start = self._read_so_far
        chunk_end = self._read_so_far + read_in_time
        chunk = words[chunk_start:chunk_end]
        self._read_so_far = chunk_end
        return ' '.join(chunk)
