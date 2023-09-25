# File: lib/diary.py


class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)

    def all(self):
        return self._entries

    def count_words(self):
        word_counts = [entry.count_words() for entry in self._entries]
        return sum(word_counts)

    def reading_time(self, wpm):
        if self._entries == []:
            raise Exception("Cannot give reading time when there are no diary entries.")

        reading_times = [entry.reading_time(wpm) for entry in self._entries]
        return sum(reading_times)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        readable_words = minutes * wpm
        most_readable_entry = None
        longest_so_far = 0
        for entry in self._entries:
            if entry.reading_time(wpm) <= readable_words:
                if entry.count_words() > longest_so_far:
                    most_readable_entry = entry
                    longest_so_far = entry.count_words()
        return most_readable_entry
        
