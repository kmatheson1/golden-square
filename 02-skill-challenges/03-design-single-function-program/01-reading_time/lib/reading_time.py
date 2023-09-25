# File: lib/reaing_time.py
import datetime

def reading_time(text):
    #read rate is 200 words per minute (or 60 seconds)
    seconds_per_word = 60 / 200
    #reading time in seconds to nearest second
    if text == "":
        raise Exception("Cannot give reading time when no text is given.")
    reading_time_seconds = int(len(text.split()) * seconds_per_word)
    reading_time = datetime.timedelta(seconds=reading_time_seconds)
    return f'Reading time will be: {reading_time}'
