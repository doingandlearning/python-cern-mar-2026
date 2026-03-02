# Lab 4: Analyzing Experimental Data - Complete Solution
# This program demonstrates working with lists, loops, and string operations

# Step 1: Create a list of readings (measurement/log descriptions)
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

print("=" * 60)
print("EXPERIMENTAL DATA ANALYSIS")
print("=" * 60)

# Step 2: Count the readings
total_readings = len(readings)
print(f"There are {total_readings} readings in the list.")
print()

# Step 3: Calculate the average reading length
total_words = 0
for reading in readings:
    words = reading.split()
    total_words += len(words)

average_words = total_words / total_readings
print(f"The average reading length is {average_words:.1f} words.")
print()

# Step 4: Search for readings by keyword
print("-" * 40)
search_term = input("What keyword would you like to search for? ")

matching_count = 0
print(f"\nReadings containing '{search_term}':")
print("-" * 40)

for reading in readings:
    if search_term.lower() in reading.lower():
        print(f"• {reading}")
        matching_count += 1

if matching_count == 0:
    print(f"No readings found containing '{search_term}'.")
else:
    print(f"\nFound {matching_count} reading(s) containing '{search_term}'.")

print("\n" + "=" * 60)
print("Analysis complete!")
print("=" * 60)
