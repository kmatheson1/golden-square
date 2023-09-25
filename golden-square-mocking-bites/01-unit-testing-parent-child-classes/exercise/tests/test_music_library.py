
from lib.music_library import MusicLibrary
from unittest.mock import Mock


"""
When calling #add 
an instance of track is added to a internal list
"""

def test_add_track():
    music_library = MusicLibrary()
    fake_track1 = Mock()
    music_library.add(fake_track1)
    assert music_library.track_list == [fake_track1]

"""
when calling #search with a key word
we get list of tracks that contains keyword in artist name or track
"""

def test_search_for_track_by_artist_or_track_name_fake():
    music_library = MusicLibrary()
    faketrack1 = Mock()
    faketrack1.matches.return_value = True
    music_library.add(faketrack1)
    assert music_library.search("blue") == [faketrack1]

def test_search_for_track_by_artist_or_track_name2_fake():
    music_library = MusicLibrary()
    faketrack1 = Mock()
    faketrack1.matches.return_value = True
    music_library.add(faketrack1)
    faketrack2 = Mock()
    faketrack2.matches.return_value = False
    music_library.add(faketrack2)

    assert music_library.search("blue") == [faketrack1]

"""
Nothing returns if music library empty
"""
def test_search_returns_empty_list_if_empty_library():
    music_library = MusicLibrary()
    assert music_library.search("blue") == []

"""
If no matches
returns empty list
"""
def test_search_returns_empty_if_no_matches_fake():
    music_library = MusicLibrary()
    faketrack1 = Mock()
    faketrack1.matches.return_value = False
    music_library.add(faketrack1)
    faketrack2 = Mock()
    faketrack2.matches.return_value = False
    music_library.add(faketrack2)
    assert music_library.search("blue") == []


