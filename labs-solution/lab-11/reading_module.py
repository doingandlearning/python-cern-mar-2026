# Lab 11: Reading Module
# DataReading class for file-based data analysis

class DataReading:
    """A class to represent a measurement or log reading with its source."""

    def __init__(self, text, source):
        self.text = text
        self.source = source

    def __str__(self):
        return f"{self.text} ({self.source})"

    def get_word_count(self):
        return len(self.text.split())
