# Lab 11: Reading Data From a File - Complete Solution
# This script reads readings from data.csv instead of using hard-coded data

import csv
from reading_module import DataReading


def load_readings_from_csv(filename):
    """
    Load readings from a CSV file and return a list of DataReading objects.

    Args:
        filename (str): The name of the CSV file to read (e.g. data.csv)

    Returns:
        list: List of DataReading objects created from the CSV data
    """
    readings = []

    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # skip header

            for row in csv_reader:
                if len(row) >= 2:
                    text, source = row[0], row[1]
                    readings.append(DataReading(text, source))

        print(f"Successfully loaded {len(readings)} readings from {filename}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Make sure it's in the same directory.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

    return readings


def analyze_readings(readings):
    """Analyze the loaded readings and display statistics."""
    if not readings:
        print("No readings to analyze.")
        return

    print("\n" + "=" * 60)
    print("DATA READINGS ANALYSIS")
    print("=" * 60)

    print("All readings:")
    print("-" * 40)
    for i, r in enumerate(readings, 1):
        print(f"{i:2}. ({r.get_word_count():2} words) [{r.source}] {r.text}")

    total = len(readings)
    total_words = sum(r.get_word_count() for r in readings)
    average = total_words / total if total > 0 else 0

    print(f"\nStatistics:")
    print(f"  Total readings: {total}")
    print(f"  Total words: {total_words}")
    print(f"  Average words per reading: {average:.1f}")

    if readings:
        shortest = min(readings, key=lambda r: r.get_word_count())
        longest = max(readings, key=lambda r: r.get_word_count())
        print(f"\nShortest ({shortest.get_word_count()} words): {shortest.text}")
        print(f"Longest ({longest.get_word_count()} words): {longest.text}")


def search_readings(readings, search_term):
    """Search readings for a specific term and display matching results."""
    if not readings:
        print("No readings to search.")
        return

    print(f"\n" + "=" * 60)
    print(f"SEARCH RESULTS FOR: '{search_term}'")
    print("=" * 60)

    matching = [r for r in readings if search_term.lower() in r.text.lower()]

    if matching:
        print(f"Found {len(matching)} matching reading(s):")
        for i, r in enumerate(matching, 1):
            print(f"{i}. [{r.source}] {r.text}")
    else:
        print(f"No readings found containing '{search_term}'")


def main():
    """Main function to run the file reading and analysis program."""
    print("Lab 11: Reading Data From a File")
    print("=" * 60)
    print("This program reads readings from data.csv and analyzes them.")
    print("=" * 60)

    filename = "data.csv"
    readings = load_readings_from_csv(filename)

    if not readings:
        print("Failed to load readings. Program cannot continue.")
        return

    analyze_readings(readings)

    print("\n" + "=" * 60)
    print("INTERACTIVE SEARCH")
    print("=" * 60)

    while True:
        search_term = input("\nEnter a search term (or 'quit' to exit): ").strip()

        if search_term.lower() == "quit":
            break
        if search_term:
            search_readings(readings, search_term)
        else:
            print("Please enter a search term.")

    print("\n" + "=" * 60)
    print("Program completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
