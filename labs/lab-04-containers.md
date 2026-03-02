# Lab 4: Analyzing Experimental Data with Lists

## Objective
In this lab, you'll get comfortable working with lists by analysing a list of measurement or log descriptions (e.g. sensor readings, experiment notes). You'll count items, compute simple statistics, and search by keyword - the kind of task you might do when summarising lab data.

You will:
1. Create and populate a list of readings
2. Count readings and calculate average word count per reading
3. Search the list for readings that contain a keyword
4. Display results in a clear format

---

## Scenario: Analysing a List of Readings

You have a collection of short text readings (log lines, sensor messages, or experiment notes). You want to know how many there are, how long they are on average (in words), and which ones mention a given keyword. This uses lists, loops, and string methods.

---

## Task 1: Set Up the File

Create a new Python file `data_analysis.py` for this lab.

**Your task:**

- Create the file (you likely don’t need any imports for the basic steps)
- You’ll add the list and logic in the next tasks

**Hints:**

- A new empty `.py` file is enough to start; add the list in Task 2

<details>
<summary>Possible Solution for Task 1</summary>

Create a file named `data_analysis.py`. No code required yet.

</details>

---

## Task 2: Create a List of Readings

In `data_analysis.py`, create a variable `readings` containing 8–10 short strings (measurement or log descriptions).

**Your task:**

- Create a variable called `readings` assigned to a list
- Add at least 8–10 strings (e.g. sensor alerts, detector status, calibration messages)
- Use a variety of topics (temperature, pressure, detector, calibration, etc.)

**Hints:**

- Lists use square brackets `[]`; each item is a string in quotes
- Use realistic lab-style messages so that keyword search (Task 4) is interesting

<details>
<summary>Possible list of readings</summary>

```python
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
```

</details>

---

## Task 3: Count Readings and Average Word Length

Analyse basic statistics over your list.

**Your task:**

- Count how many readings are in the list
- Calculate the average number of words per reading (total words ÷ number of readings)
- Print the count and the average in a clear way

**Hints:**

- Use `len(readings)` for the count
- Loop over each reading, use `.split()` to get words, and sum the word counts
- Initialise a variable (e.g. `total_words = 0`) before the loop and add each reading’s word count to it

<details>
<summary>Possible Solution for Task 3</summary>

```python
total_readings = len(readings)
print(f"There are {total_readings} readings in the list.")

total_words = 0
for reading in readings:
    total_words += len(reading.split())
average_words = total_words / total_readings
print(f"The average reading length is {average_words:.1f} words.")
```

</details>

---

## Task 4: Search for Readings by Keyword

Let the user search for a keyword and show which readings contain it.

**Your task:**

- Use `input()` to ask for a search keyword
- Loop through `readings` and find every reading that contains that keyword (case-insensitive)
- Print each matching reading and the total number of matches

**Hints:**

- Use `keyword.lower() in reading.lower()` for case-insensitive matching
- Use a counter (e.g. `matching_count = 0`) and increment it for each match
- If there are no matches, print a message saying so

<details>
<summary>Possible Solution for Task 4</summary>

```python
search_term = input("What keyword would you like to search for? ")
matching_count = 0
print(f"\nReadings containing '{search_term}':")
for reading in readings:
    if search_term.lower() in reading.lower():
        print(f"  • {reading}")
        matching_count += 1
if matching_count == 0:
    print(f"No readings found containing '{search_term}'.")
else:
    print(f"\nFound {matching_count} reading(s) containing '{search_term}'.")
```

</details>

---

## Example Interaction

```
There are 10 readings in the list.
The average reading length is 5.8 words.

What keyword would you like to search for? detector

Readings containing 'detector':
  • Pressure nominal in Detector A
  • Anomaly detected in particle count sensor
  • High voltage supply stable across all channels
  • Trigger rate above threshold in forward region

Found 4 reading(s) containing 'detector'.
```

---

## Key Concepts Demonstrated

- **Lists**: Creating and indexing a list of strings
- **`len()`**: Number of items in a list
- **Loops**: Iterating over each item in a list
- **String methods**: `.split()` for words, `.lower()` for case-insensitive search
- **`in`**: Checking if a substring is in a string

---

## Common Issues

- **NameError: name 'readings' is not defined** — Define the list before you use it.
- **Average is 0 or wrong** — Initialise `total_words = 0` before the loop and add each reading’s word count inside the loop.
- **Search misses obvious matches** — Use `.lower()` on both the search term and each reading when comparing.

---

## Next Steps

In the next lab, you’ll wrap this logic in functions to build a reusable data analysis toolkit.
