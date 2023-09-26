# File: lib/music_library.py

class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.track_list = []

    def add(self, track):
        self.track_list.append(track)

    def search(self, keyword):
        return [track for track in self.track_list if track.matches(keyword)]

