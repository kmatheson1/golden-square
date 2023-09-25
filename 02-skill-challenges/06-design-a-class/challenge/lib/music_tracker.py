# File: lib/music_tracker.py

class MusicTracker():
    def __init__(self):
        self.track_list = []

    def add(self, artist, track):
        if artist == "" or track == "":
            raise Exception("Cannot add track if track name or artist isn't provided.")
        
        if {artist: track} not in self.track_list:
            self.track_list.append({artist: track})
        else:
            return "Track already added to list."

    def list_tracks(self):
        return self.track_list