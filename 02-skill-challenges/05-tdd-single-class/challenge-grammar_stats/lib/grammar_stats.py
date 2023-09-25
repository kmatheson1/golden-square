# File: lib/grammar_stats.py

class GrammarStats():
    def __init__(self):
        self.total_checked = 0
        self.total_passed = 0

    def check(self, text):
        if not text:
            raise Exception("Cannot assess grammar if no text is given.")

        if text[0].isupper() and text[-1] in '?!.':
            self.total_checked += 1
            self.total_passed += 1
            return True
        else:
            self.total_checked += 1
            return False
        
    def percentage_good(self):
        percentage_good = (self.total_passed / self.total_checked) * 100
        return round(percentage_good)