# Lab 8: Reading Module
# This module contains the DataReading class definition for use in other files

class DataReading:
    """
    A class to represent a measurement or log reading with its source.

    Attributes:
        text (str): The reading description
        source (str): The source (e.g. detector name, sensor ID)
    """

    def __init__(self, text, source):
        """Initialize a new DataReading object."""
        self.text = text
        self.source = source

    def __str__(self):
        """Return a string representation of the DataReading object."""
        return f"{self.text} ({self.source})"

    def get_word_count(self):
        """Get the number of words in the reading text."""
        return len(self.text.split())

    def get_character_count(self):
        """Get the total character count of the reading text."""
        return len(self.text)

    def is_long_reading(self):
        """Check if the reading is considered long (more than 8 words)."""
        return self.get_word_count() > 8

    def contains_keyword(self, keyword):
        """Check if the reading contains a specific keyword."""
        return keyword.lower() in self.text.lower()
