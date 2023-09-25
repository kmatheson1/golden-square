from lib.music_library import MusicLibrary
from lib.track import Track

"""
when calling #search with a key word
we get list of tracks that contains keyword in artist name or track
"""
def test_search_for_track_by_artist_or_track_name():
    music_library = MusicLibrary()
    track1 = Track("Fix You", "Coldplay")
    music_library.add(track1)
    assert music_library.search("you") == [track1]

def test_search_for_track_by_artist_or_track_name2():
    music_library = MusicLibrary()
    track1 = Track("Fix You", "Coldplay")
    music_library.add(track1)
    track2 = Track("title", "track")
    music_library.add(track2)

    assert music_library.search("play") == [track1]

"""
If no matches
returns empty list
"""
def test_search_returns_empty_if_no_matches():
    music_library = MusicLibrary()
    track1 = Track("Fix You", "Coldplay")
    music_library.add(track1)
    track2 = Track("title", "track")
    music_library.add(track2)
    assert music_library.search("pillow") == []
