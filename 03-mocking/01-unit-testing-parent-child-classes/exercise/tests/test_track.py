from lib.track import Track

"""
upon initializing
public properties set as title and artist
"""
def test_title_and_artist():
    track = Track("Fix You", "Coldplay")
    assert track.title == "Fix You"
    assert track.artist == "Coldplay"

"""
#matches returns true
when artist matches keyword
"""
def test_matches_artist():
    track = Track("Fix You", "Coldplay")
    assert track.matches("play") == True

"""
#matches returns False
when artist doesn't match keyword
"""
def test_doe_not_match_artist():
    track = Track("Fix You", "Coldplay")
    assert track.matches("britney") == False

"""
#matches returns true
when title matches keyword
"""
def test_matches_title():
    track = Track("Fix You", "Coldplay")
    assert track.matches("you") == True

"""
#matches returns False
when title doesn't match keyword
"""
def test_doe_not_match_title():
    track = Track("Fix You", "Coldplay")
    assert track.matches("britney") == False
