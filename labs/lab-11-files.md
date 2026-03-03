# Lab 11: Reading Data From a File

## Objective
So far, readings have been hard-coded in the script. Real programs usually load data from files. In this lab you’ll modify your program to read measurements or log data from a `data.csv` file using Python’s `csv` module, and build a list of `DataReading` objects from the file.

You will:
1. Import `csv` and prepare an empty list for readings
2. Open the CSV file, skip the header, and loop over rows
3. Create a `DataReading` from each row (text, source) and append it to the list
4. Use the loaded list with your existing analysis code

---

## Scenario: Data in a File

**Prerequisite:** Your `data.csv` can use the same readings data (text and source) as in Lab 4. The file has two columns: `text` and `source` (with a header row). Each following row is one reading. You’ll open the file, skip the header, and for each row create `DataReading(row[0], row[1])` and append it to a list. The rest of your program (analysis, printing) stays the same but works on this list instead of a hard-coded one.

---

## Task 1: Prepare to Load from File

**Your task:**

- In `main_analysis.py` (or your main script), add `import csv` at the top
- Remove or comment out the hard-coded list of `DataReading` objects
- Create an empty list, e.g. `readings = []`, where you will put the loaded objects
- Ensure `data.csv` is in the same directory as your script (or adjust the path)

**Hints:**

- The CSV should have a header line: `text,source`
- You’ll fill `readings` in Task 3

<details>
<summary>Possible setup</summary>

```python
import csv
from reading_module import DataReading

def main():
    readings = []  # will load from file
    # ... open file and fill readings ...
```

</details>

---

## Task 2: Open the File and Loop Over Rows

**Your task:**

- Use `with open("data.csv", "r", newline="", encoding="utf-8") as f:`
- Create a reader with `csv.reader(f)`
- Call `next(reader)` once to skip the header row
- Write a `for` loop over the reader to process each row (you’ll add the object creation in Task 3)

**Hints:**

- `newline=""` is recommended for `csv.reader`
- After `next(reader)`, each `row` is a list of strings; `row[0]` is text, `row[1]` is source

<details>
<summary>Possible Solution for Task 2</summary>

```python
with open("data.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        if len(row) >= 2:
            text, source = row[0], row[1]
            readings.append(DataReading(text, source))
```

</details>

---

## Task 3: Create DataReading Objects from Each Row

**Your task:**

- Inside the loop, take `row[0]` as the reading text and `row[1]` as the source
- Create `DataReading(text, source)` and append it to `readings`
- Optionally check that each row has at least two columns before using it
- After the loop, the rest of your code can use `readings` as before (e.g. print word counts, run analysis)

**Hints:**

- Handle malformed rows (e.g. `if len(row) >= 2:`) to avoid index errors
- If the file is missing, `open(...)` will raise `FileNotFoundError`; you can add a `try...except` later if you want

<details>
<summary>Possible Solution for Task 3</summary>

```python
for row in reader:
    if len(row) >= 2:
        readings.append(DataReading(row[0], row[1]))
```

</details>

---

## Example `data.csv` Format

```csv
text,source
"Temperature spike detected in Sector 7 cooling system",Detector A
"Pressure nominal in Detector A",Detector A
```

---

**You're done when** the program loads readings from `data.csv` into a list of `DataReading` objects and your existing analysis runs on the loaded list.

---

## Key Concepts Demonstrated

- **File I/O**: `open()` with `with` so the file is closed automatically
- **CSV**: `csv.reader()` to parse rows; first row is often the header
- **Separation of data and code**: Change the data by editing the file, not the program

---

## Common Issues

- **FileNotFoundError** — Run the script from the directory that contains `data.csv`, or use the full path to the file.
- **Wrong columns** — Ensure the CSV has a header and that you use `row[0]` and `row[1]` in the right order (text, source).

---

## Next Steps

In the final case study, you’ll tie together file loading, the `DataReading` class, analysis by source, and writing a report to a file.
