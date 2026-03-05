# Lab 11: Loading Measurements from a CSV File

## Objective

So far, your result data (for `ResultValue` objects) has been created directly in code. Real programs usually load measurements from files. In this lab you’ll load detector results from a `data.csv` file using Python’s `csv` module, group them into `ResultValue` objects, and then reuse your existing analysis methods to print a summary.

You will:
1. Import `csv` and prepare a structure to hold your `ResultValue` objects
2. Open the CSV file, skip the header, and loop over rows
3. For each (detector_name, date, value) row, update or create a `ResultValue` and call `add_result`
4. Use the loaded objects with your existing analysis code to print a report

---

## Scenario: Detector Results in a File

**Prerequisite:** You have an analysis class from Labs 7–8 (e.g. `ResultValue` in `results_module.py`) with methods like `add_result`, `get_average_of_results`, `get_maximum_of_results`, and `get_range_of_results` (plus any extra analysis methods you added).

Now you have a `data.csv` file with **one result per row**, with columns:

```csv
detector_name,date,value
Detector A,2026-03-03,123
Detector A,2026-03-03,414
Detector B,2026-03-02,12
Detector B,2026-03-02,15
Detector A,2026-03-04,200
```

You’ll read this file, group rows by `(detector_name, date)`, and build one `ResultValue` per group, filling `results` with the corresponding `value` numbers.

---

## Task 1: Prepare to Load from File

**Your task:**

- In your analysis script (e.g. `main_analysis.py`), add `import csv` at the top
- Import your analysis class: `from results_module import ResultValue`
- Remove or comment out any hard-coded `ResultValue` objects you created before
- Decide how to store the loaded objects, e.g.:
  - a dictionary `results_by_key = {}` where the key is `(detector_name, date)` and the value is a `ResultValue` object

**Hints:**

- A dict keyed by `(detector_name, date)` makes it easy to group multiple measurements for the same detector and date.

<details>
<summary>Possible setup</summary>

```python
import csv
from results_module import ResultValue

def main():
    results_by_key = {}  # (detector_name, date) -> ResultValue
    # ... open file and fill results_by_key ...
```

</details>

---

## Task 2: Open the File and Loop Over Rows

**Your task:**

- Use `with open("data.csv", "r", newline="", encoding="utf-8") as f:`
- Create a reader with `csv.DictReader(f)`
- Write a `for` loop over the reader to process each row; each row will be a dict with keys `"detector_name"`, `"date"`, and `"value"`

**Hints:**

- DictReader automatically uses the header row for field names, so you can write `row["detector_name"]`, `row["date"]`, and `row["value"]`.

<details>
<summary>Possible pattern for Task 2</summary>

```python
with open("data.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        detector_name = row.get("detector_name")
        date_str = row.get("date")
        value_str = row.get("value")
        if detector_name is None or date_str is None or value_str is None:
            continue  # skip malformed rows
        # you'll turn value_str into a number and fill results_by_key in Task 3
```

</details>

---

## Task 3: Build `ResultValue` Objects from Each Row

**Your task:**

- Inside the loop:
  - Turn `value_str` into a number (e.g. `float(value_str)` or `int(value_str)`)
  - Use `(detector_name, date_str)` as a key in `results_by_key`
  - If the key is not in the dict yet, create a new `ResultValue(detector_name, date_str)` and store it
  - Call `add_result(value)` on the corresponding object
- After the loop, you should have one `ResultValue` per `(detector_name, date)` pair, each with a `results` list filled from the file

**Hints:**

- Use `if key not in results_by_key:` to decide when to create a new object
- Decide whether you want `int` or `float` for your values; be consistent

<details>
<summary>Possible Solution for Task 3</summary>

```python
results_by_key = {}

with open("data.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        detector_name = row.get("detector_name")
        date_str = row.get("date")
        value_str = row.get("value")
        if detector_name is None or date_str is None or value_str is None:
            continue
        try:
            value = float(value_str)
        except ValueError:
            continue  # skip rows with non-numeric values

        key = (detector_name, date_str)
        if key not in results_by_key:
            results_by_key[key] = ResultValue(detector_name, date_str)

        results_by_key[key].add_result(value)
```

</details>

---

## Task 4: Print an Analysis Report from Loaded Data

Now that your `ResultValue` objects are built from the file, reuse your analysis methods to print a report.

**Your task:**

- Loop over the `ResultValue` objects (e.g. `for r in results_by_key.values():`)
- For each object, call methods like:
  - `get_average_of_results()`
  - `get_maximum_of_results()`
  - `get_range_of_results()`
  - and any extra analysis methods you added in Lab 7 (e.g. `count_results_above`)
- Print a line per object, e.g.:  
  `Detector A (2026-03-03): avg=220.0, max=414, range=291`

**Hints:**

- You can reuse or adapt the report loop from Lab 7
- Consider skipping or marking detectors with no data (if your class allows empty `results`)

<details>
<summary>Possible pattern for Task 4</summary>

```python
for r in results_by_key.values():
    avg = r.get_average_of_results()
    mx = r.get_maximum_of_results()
    rng = r.get_range_of_results()
    if avg is not None:
        print(f"{r.detector_name} ({r.date}): avg={avg}, max={mx}, range={rng}")
    else:
        print(f"{r.detector_name} ({r.date}): no data")
```

</details>

---

## Example `data.csv` Format

```csv
detector_name,date,value
Detector A,2026-03-03,123
Detector A,2026-03-03,414
Detector B,2026-03-02,12
Detector B,2026-03-02,15
Detector A,2026-03-04,200
Detector C,2026-03-01,50
```

Put `data.csv` in the same directory as your script (or adjust the path in `open(...)`).

---

**You're done when** the program loads measurements from `data.csv` into a mapping of `(detector_name, date) -> ResultValue` objects and your existing analysis prints a report based on the file data instead of hard-coded values.

---

## Key Concepts Demonstrated

- **File I/O**: `open()` with `with` so the file is closed automatically
- **CSV**: `csv.reader()` to parse rows; first row is the header
- **Grouping**: Using a dict keyed by `(detector_name, date)` to group related measurements
- **Separation of data and code**: Change the data by editing `data.csv`, not the program

---

## Common Issues

- **FileNotFoundError** — Run the script from the directory that contains `data.csv`, or use the full path to the file.
- **Wrong columns** — Ensure the CSV has a header `detector_name,date,value` and that you use `row[0]`, `row[1]`, `row[2]` in the right order.
- **ValueError when converting to float** — If `value_str` is not numeric, `float(value_str)` will raise `ValueError`; decide whether to skip that row or handle it differently.

---

## Next Steps

In the final case study or in a Pandas/matplotlib session, you can load the same `data.csv` into a DataFrame, compute statistics, and compare them with what your `ResultValue` class computes.

