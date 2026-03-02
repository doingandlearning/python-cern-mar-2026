"""
Solution for the Final Case Study: Experimental Data Report.
Loads readings from data.csv, analyses by source, and writes report.txt.
Run from labs-solution/ so that reading_module.py and data.csv are in the same directory.
"""

import csv
from reading_module import DataReading


def load_readings_from_csv(filename="data.csv"):
    """
    Load readings from a CSV file. Returns a list of DataReading objects.
    """
    readings = []

    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                if len(row) >= 2:
                    readings.append(DataReading(row[0], row[1]))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

    return readings


def analyze_sources(list_of_readings):
    """Count readings per source and return a dictionary."""
    source_counts = {}
    for r in list_of_readings:
        if r.source in source_counts:
            source_counts[r.source] += 1
        else:
            source_counts[r.source] = 1
    return source_counts


def generate_report(analysis, total_readings):
    """Generate a formatted report string from the analysis."""
    report_lines = [
        "--- DATA SOURCE REPORT ---",
        f"There are {total_readings} total readings.",
        "The following sources were found:",
        "",
    ]

    sorted_analysis = sorted(analysis.items(), key=lambda item: item[1], reverse=True)

    for source, count in sorted_analysis:
        report_lines.append(f"* {source}: {count} readings")

    return "\n".join(report_lines)


def main():
    """Main function to run the data report pipeline."""
    print("Loading readings from data.csv...")
    readings = load_readings_from_csv("data.csv")

    if not readings:
        print("No readings loaded. Exiting.")
        return

    print(f"Loaded {len(readings)} readings.")

    analysis = analyze_sources(readings)
    report = generate_report(analysis, len(readings))

    try:
        with open("report.txt", "w", encoding="utf-8") as f:
            f.write(report)
        print("Report generated successfully as report.txt")
    except IOError as e:
        print(f"Error writing report to file: {e}")


if __name__ == "__main__":
    main()
