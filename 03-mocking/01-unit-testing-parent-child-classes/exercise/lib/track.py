# File: lib/track.py

class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        return keyword.lower() in self.artist.lower() or keyword in self.title.lower()
        