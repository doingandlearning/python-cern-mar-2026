# Lab 5: Building a Data Analysis Toolkit with Functions - Complete Solution
# This program demonstrates function definition, parameters, and return values

# Readings data (measurement / log descriptions)
readings = [
    "Temperature spike detected in Sector 7 cooling system",
    "Pressure nominal in Detector A",
    "Calibration run completed for beam line B2",
    "New baseline recorded for magnet array",
    "Anomaly detected in particle count sensor",
    "Vacuum level within acceptable range",
    "Data acquisition run finished successfully",
    "High voltage supply stable across all channels",
    "Trigger rate above threshold in forward region",
    "Shielding survey completed no issues found"
]


def get_word_count(reading_text):
    """
    Count the number of words in a reading string.

    Args:
        reading_text (str): The reading text to count words in

    Returns:
        int: The number of words in the reading
    """
    words = reading_text.split()
    return len(words)


def find_readings_with_keyword(list_of_readings, keyword):
    """
    Find readings that contain a specific keyword.

    Args:
        list_of_readings (list): List of reading strings
        keyword (str): The keyword to search for

    Returns:
        list: Readings containing the keyword
    """
    matching_readings = []

    for reading in list_of_readings:
        if keyword.lower() in reading.lower():
            matching_readings.append(reading)

    return matching_readings


def analyse_all_readings(list_of_readings):
    """
    Analyze all readings and display statistics.

    Args:
        list_of_readings (list): List of reading strings
    """
    total_words = 0

    for reading in list_of_readings:
        word_count = get_word_count(reading)
        total_words += word_count

    average_words = total_words / len(list_of_readings)

    print("=" * 50)
    print("DATA ANALYSIS RESULTS")
    print("=" * 50)
    print(f"Total readings analyzed: {len(list_of_readings)}")
    print(f"Total words across all readings: {total_words}")
    print(f"Average words per reading: {average_words:.1f}")
    print("=" * 50)


def main():
    """Main function to run the data analysis."""
    print("Welcome to the Data Analysis Toolkit!")
    print("This program demonstrates functions for analyzing experimental data.")

    analyse_all_readings(readings)

    print("\n" + "=" * 50)
    print("SEARCH DEMONSTRATION")
    print("=" * 50)

    search_keywords = ["detector", "temperature", "calibration", "data"]

    for keyword in search_keywords:
        print(f"\nSearching for '{keyword}':")
        print("-" * 30)

        matching = find_readings_with_keyword(readings, keyword)

        if matching:
            print(f"Found {len(matching)} reading(s):")
            for reading in matching:
                print(f"  • {reading}")
        else:
            print(f"No readings found containing '{keyword}'")

    print("\n" + "=" * 50)
    print("Analysis complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
