# File: tests/test_reading_time.py
from lib.reading_time import reading_time
import pytest
"""
If we give an empty string.
It will return an error "Cannot give reading time when no text is given."
"""
def test_reading_time_empty_string():
    with pytest.raises(Exception) as e:
        reading_time("")
    error_message = str(e.value)
    assert error_message == "Cannot give reading time when no text is given."

"""
If we give a string containing 1 word.
It will return time in minutes ""Reading time will be: 0:00:00".
"""
def test_reading_time_one_word():
    assert reading_time("word") == "Reading time will be: 0:00:00"

"""
If we give a string containing 50 words.
It will return time in minutes ""Reading time will be: 0:00:15".
"""
def test_reading_time_50_words():
    text ="Cubilia viverra semper pede ut. Eros odio elementum penatibus mi, fermentum imperdiet erat nam cum eu penatibus fermentum mauris ad cum accumsan malesuada est. Primis justo nibh. Varius condimentum a. Class. Integer dolor senectus accumsan egestas, porttitor litora parturient donec ridiculus quis. Sapien accumsan. Habitant sit dictum mauris sem taciti."

    assert reading_time(text) == "Reading time will be: 0:00:15"

"""
If we give a string containing 200 words.
It will return time in minutes ""Reading time will be: 0:01:00".
"""
def test_reading_time_200_words():
    text ="Luctus dictumst quis dis, risus conubia amet nonummy rhoncus odio. Arcu quis sit primis. Pulvinar commodo. Aptent sociis fusce facilisi suspendisse varius. Iaculis pretium rutrum facilisis natoque risus condimentum adipiscing blandit. Nisi Sociosqu aliquet dictum dictumst Amet Aenean rutrum molestie fames metus. Commodo hendrerit at dapibus viverra curae; nulla morbi senectus et pretium eu nec phasellus nonummy commodo facilisi, habitant rutrum tincidunt suspendisse tristique nec tempus lacus. Nullam nisi consequat blandit duis suscipit magna nonummy nonummy quam risus lectus eget litora fames facilisi taciti, congue. Posuere imperdiet orci etiam accumsan. Venenatis, tristique erat nisi. Pretium montes conubia elementum. Praesent, velit, aliquam fermentum cum morbi vehicula a tristique dignissim feugiat sociis purus. Mauris conubia Inceptos pharetra justo rhoncus. Odio est. Montes vulputate dis. Sapien sem malesuada arcu mus suscipit. Condimentum sociosqu quam convallis dapibus porta. Suspendisse elementum sociosqu cras. Pharetra. Laoreet dignissim montes dolor suscipit Erat. Mauris vulputate libero quis mauris suscipit. Primis nullam vulputate cras ligula taciti odio nibh elementum viverra ullamcorper nullam dui. Etiam volutpat congue vestibulum litora ullamcorper enim posuere quisque ipsum hac curabitur. Tortor sit accumsan. Pharetra sodales mattis litora, diam praesent ultricies sit cras. Fringilla iaculis metus dui. Hac Sit class leo habitant hac nulla aptent."
    assert reading_time(text) == "Reading time will be: 0:01:00"

"""
If we give a string containing 50 words in paragraphs
It will return time in minutes ""Reading time will be: 0:00:15".
"""
def test_reading_time_50_words_in_paragraphs():
    text ="Cubilia viverra semper pede ut. Eros odio elementum penatibus mi, fermentum imperdiet erat nam cum eu penatibus fermentum mauris ad cum accumsan malesuada est. \nPrimis justo nibh. Varius condimentum a. Class. Integer dolor senectus accumsan egestas, porttitor litora parturient donec ridiculus quis. \nSapien accumsan. Habitant sit dictum mauris sem taciti."

    assert reading_time(text) == "Reading time will be: 0:00:15"