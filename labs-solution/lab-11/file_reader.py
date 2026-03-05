"""Lab 11: Loading Measurements from a CSV File - Complete Solution.

This script loads detector measurements from data.csv into ResultValue objects
using csv.DictReader, then prints a summary report using the analysis methods.
"""

import csv

from results_module import ResultValue


def load_results_from_csv(filename):
    """Load results from CSV and return a dict of (detector_name, date) -> ResultValue."""
    results_by_key = {}

    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                detector_name = row.get("detector_name")
                date_str = row.get("date")
                value_str = row.get("value")
                if detector_name is None or date_str is None or value_str is None:
                    continue
                try:
                    value = float(value_str)
                except ValueError:
                    continue

                key = (detector_name, date_str)
                if key not in results_by_key:
                    results_by_key[key] = ResultValue(detector_name, date_str)
                results_by_key[key].add_result(value)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Make sure it's in the same directory.")
        return {}
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}

    return results_by_key


def print_summary(results_by_key):
    """Print a summary report for all ResultValue objects."""
    if not results_by_key:
        print("No results to analyze.")
        return

    print("\n" + "=" * 60)
    print("DETECTOR RESULTS ANALYSIS")
    print("=" * 60)

    for r in results_by_key.values():
        avg = r.get_average_of_results()
        mx = r.get_maximum_of_results()
        rng = r.get_range_of_results()
        if avg is not None:
            print(f"{r.detector_name} ({r.date}): avg={avg}, max={mx}, range={rng}")
        else:
            print(f"{r.detector_name} ({r.date}): no data")


def main():
    print("Lab 11: Loading Measurements from a CSV File")
    print("=" * 60)
    print("This program reads detector results from data.csv and analyzes them.")
    print("=" * 60)

    filename = "data.csv"
    results_by_key = load_results_from_csv(filename)

    if not results_by_key:
        print("Failed to load results. Program cannot continue.")
        return

    print_summary(results_by_key)


if __name__ == "__main__":
    main()
