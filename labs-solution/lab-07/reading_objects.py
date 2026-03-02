# Lab 7: Structuring Data with Classes - Complete Solution
# This program demonstrates creating and using a DataReading class

class DataReading:
    """
    A class to represent a measurement or log reading with its source.

    Attributes:
        text (str): The reading description (e.g. log line, measurement text)
        source (str): The source (e.g. detector name, sensor ID, experiment)
    """

    def __init__(self, text, source):
        """
        Initialize a new DataReading object.

        Args:
            text (str): The reading text
            source (str): The source (e.g. detector, sensor)
        """
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


def main():
    """Main function to demonstrate the DataReading class."""
    print("Lab 7: Structuring Data with Classes")
    print("=" * 50)

    # Create DataReading objects
    r1 = DataReading(
        "Temperature spike detected in Sector 7 cooling system", "Detector A"
    )
    r2 = DataReading("Pressure nominal in Detector A", "Detector A")
    r3 = DataReading("Calibration run completed for beam line B2", "Beam Line B2")

    print("\nCreated reading objects:")
    print(f"1. {r1}")
    print(f"2. {r2}")
    print(f"3. {r3}")

    print("\nWord counts:")
    print(f"Reading 1: {r1.get_word_count()} words")
    print(f"Reading 2: {r2.get_word_count()} words")
    print(f"Reading 3: {r3.get_word_count()} words")

    # List of DataReading objects
    readings = [
        DataReading("Temperature spike detected in Sector 7 cooling system", "Detector A"),
        DataReading("Pressure nominal in Detector A", "Detector A"),
        DataReading("Calibration run completed for beam line B2", "Beam Line B2"),
        DataReading("New baseline recorded for magnet array", "Magnet Lab"),
        DataReading("Anomaly detected in particle count sensor", "Detector A"),
        DataReading("Vacuum level within acceptable range", "Beam Line B2"),
        DataReading("Data acquisition run finished successfully", "Data Centre"),
        DataReading("High voltage supply stable across all channels", "Detector A"),
        DataReading("Trigger rate above threshold in forward region", "Detector A"),
        DataReading("Shielding survey completed no issues found", "Safety Office"),
    ]

    print(f"\nProcessing {len(readings)} readings:")
    for i, r in enumerate(readings, 1):
        print(f"{i:2}. ({r.get_word_count():2} words) [{r.source}] {r.text}")

    print("\n" + "=" * 50)
    print("Class demonstration complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
