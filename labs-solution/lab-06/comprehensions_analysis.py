# Lab 6: Supercharging Analysis with List Comprehensions - Complete Solution
# This program demonstrates list comprehensions for mapping, filtering, and combining operations

# Readings data (same as Lab 4/5)
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


def main():
    """Main function to demonstrate all list comprehension techniques."""
    print("Lab 6: List Comprehensions Analysis")
    print("=" * 50)

    # Step 2: Mapping with List Comprehensions
    print("\nStep 2: Mapping with List Comprehensions")
    print("-" * 40)

    reading_lengths = [len(reading.split()) for reading in readings]

    print("Reading lengths (word counts):")
    for i, (reading, length) in enumerate(zip(readings, reading_lengths)):
        print(f"{i+1:2}. ({length:2} words) {reading}")

    print(f"\nAll reading lengths: {reading_lengths}")

    # Step 3: Filtering with List Comprehensions
    print("\n\nStep 3: Filtering with List Comprehensions")
    print("-" * 40)

    short_readings = [reading for reading in readings if len(reading.split()) <= 7]

    print("Readings with 7 words or fewer:")
    for i, reading in enumerate(short_readings):
        word_count = len(reading.split())
        print(f"{i+1}. ({word_count} words) {reading}")

    print(f"\nTotal short readings: {len(short_readings)}")

    # Step 4: Combining Mapping and Filtering (e.g. keyword "detector")
    print("\n\nStep 4: Combining Mapping and Filtering")
    print("-" * 40)

    specific_reading_lengths = [
        len(reading.split()) for reading in readings if "detector" in reading.lower()
    ]

    print("Word counts of readings containing 'detector':")
    for reading in readings:
        if "detector" in reading.lower():
            word_count = len(reading.split())
            print(f"  • '{reading}' -> {word_count} words")

    print(f"\nAll word counts for 'detector' readings: {specific_reading_lengths}")

    # Additional analysis
    print("\n\nAdditional Analysis")
    print("-" * 40)

    average_words = sum(len(reading.split()) for reading in readings) / len(readings)
    print(f"Average words per reading: {average_words:.1f}")

    longest_reading = max(readings, key=lambda x: len(x.split()))
    shortest_reading = min(readings, key=lambda x: len(x.split()))
    print(f"Longest: '{longest_reading}' ({len(longest_reading.split())} words)")
    print(f"Shortest: '{shortest_reading}' ({len(shortest_reading.split())} words)")

    print("\n" + "=" * 50)
    print("List comprehensions analysis complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
