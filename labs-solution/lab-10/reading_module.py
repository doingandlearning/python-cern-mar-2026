# Lab 10: Reading Module (for Testing lab)
# This module contains the DataReading class for use in tests and other files

class DataReading:
    """
    A class to represent a measurement or log reading with its source.
    """

    def __init__(self, text, source):
        self.text = text
        self.source = source

    def __str__(self):
        return f"{self.text} ({self.source})"

    def get_word_count(self):
        return len(self.text.split())
