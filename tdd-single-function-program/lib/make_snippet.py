# File: lib/make_snippet.py

def make_snippet(str):
    words = str.split(" ")
    if len(words) > 5:
        snippet = " ".join(words[:5]) + "..."
        return snippet
    else:
        return str