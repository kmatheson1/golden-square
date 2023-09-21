# File: tests/test_music_tracker.py
from lib.music_tracker import MusicTracker
import pytest

"""
List when there are no tracks
Returns empty list
"""
def test_list_when_no_tracks_added():
    music_tracker = MusicTracker()
    assert music_tracker.list_tracks() == []

"""
List when one track has been added
Returns list containing one track
"""
def test_list_if_one_track_added():
    music_tracker = MusicTracker()
    music_tracker.add("Oasis", "Wonderwall")
    assert music_tracker.list_tracks() == [{"Oasis": "Wonderwall"}]

"""
List when multiple tracks have been added
Returns list of all tracks added
"""
def test_list_if_multiple_tracks_added():
    music_tracker = MusicTracker()
    music_tracker.add("Oasis", "Wonderwall")
    music_tracker.add("Coldplay", "Fix You")
    music_tracker.add("Kanye West", "Good Life")
    result = music_tracker.list_tracks()
    assert result == [{"Oasis": "Wonderwall"}, {"Coldplay": "Fix You"}, {"Kanye West": "Good Life"}]

"""
If either Artist or Track are given as an empty string
Return Error message
"""
def test_error_when_empty_strings():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.add("", "")
    assert str(e.value) == "Cannot add track if track name or artist isn't provided."

"""
If track has already been added
A repitition is not added to the list
"""
def test_repeat_track():
    music_tracker = MusicTracker()
    music_tracker.add("Oasis", "Wonderwall")
    music_tracker.add("Coldplay", "Fix You")
    music_tracker.add("Coldplay", "Fix You")
    result = music_tracker.list_tracks()
    assert result == [{"Oasis": "Wonderwall"}, {"Coldplay": "Fix You"}]