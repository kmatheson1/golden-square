# File: design.md

# x Music Tracker Design Recipe


## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can keep track of my music listening 
> I want to add tracks I've listened to and see a list of them.

* clearly see tracks (artist and track)
* errors for incorrect input
* view list of all tracks added

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

'''python
# EXAMPLE 

class MusicTracker():
    def add(self, artist, track):
    # Parameters:
    #   an artist as a strin, a track as a string
    # Returns:
    #   None

    def list_tracks(self):
    # Parameters:
    #   None
    # Returns:
    #   list of all tracks listned to and by which artist

'''

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._
_Encode each example as a test. You can add to the above list as you go._

'''python
# EXAMPLE 

"""
List when there are no tracks
Returns empty list
"""
music_tracker = MusicTracker()
music_tracker.list_tracks()
# => []

"""
List when one track has been added
Returns list containing one track
"""
music_tracker = MusicTracker()
music_tracker.add("Oasis", "Wonderwall")
music_tracker.list_tracks()
# => [{"Oasis": "Wonderwall"}]

"""
List when multiple tracks have been added
Returns list of all tracks added
"""
music_tracker = MusicTracker()
music_tracker.add("Oasis", "Wonderwall")
music_tracker.add("Cold Play", "Fix You")
music_tracker.add("Kanye West", "Good Life")
music_tracker.list_tracks()
# => [{"Oasis": "Wonderwall"}, {"Coldplay": "Fix You"}, {"Kanye West": "Good Life"}]

"""
If either Artist or Track are given as an empty string
Return Error message
"""
music_tracker = MusicTracker()
music_tracker.add("", "")
# => "Cannot add track if track name or artist isn't provided."


'''

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._