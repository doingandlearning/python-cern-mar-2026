# Lab 8: Main Analysis Script
# This script imports the DataReading class from reading_module and uses it for analysis

from reading_module import DataReading


def main():
    """Main function to run the data analysis using the imported DataReading class."""
    print("Lab 8: Organizing Your Code with Modules")
    print("=" * 50)

    # Create a list of DataReading objects using the imported class
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

    print(f"Created {len(readings)} DataReading objects using imported class")

    # Process all readings
    print("\nProcessing all readings:")
    print("-" * 40)

    for i, r in enumerate(readings, 1):
        word_count = r.get_word_count()
        char_count = r.get_character_count()
        print(f"{i:2}. ({word_count:2} words, {char_count:3} chars) [{r.source}] {r.text}")

    # Group readings by source
    print("\nAnalysis by source:")
    print("-" * 40)

    source_groups = {}
    for r in readings:
        if r.source not in source_groups:
            source_groups[r.source] = []
        source_groups[r.source].append(r)

    for source, group in source_groups.items():
        total_words = sum(r.get_word_count() for r in group)
        avg_words = total_words / len(group)
        print(f"\n{source}: {len(group)} readings, avg {avg_words:.1f} words")

    # Keyword search
    print("\nReadings containing 'detector':")
    for r in readings:
        if r.contains_keyword("detector"):
            print(f"  • [{r.source}] {r.text}")

    print("\n" + "=" * 50)
    print("Module-based analysis complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
