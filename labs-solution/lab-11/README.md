# Lab 11: Loading Measurements from a CSV File — Solutions

This folder contains solutions for Lab 11: loading detector measurements from `data.csv` and building `ResultValue` analysis objects.

## Files

| File | Description |
|------|-------------|
| `file_reader.py` | Main solution: loads from `data.csv` using `csv.DictReader`, creates `ResultValue` objects, and prints a summary report |
| `results_module.py` | Defines the `ResultValue` class (used by `file_reader.py`) |
| `data.csv` | Sample CSV with columns `detector_name,date,value` |

## Run

From this directory (so `data.csv` and `results_module.py` are on the path):

```bash
python file_reader.py
```

## Requirements

- `data.csv` in the same directory (columns: `detector_name,date,value`)
- `results_module.py` with the `ResultValue` class

## Key behaviour

- Uses `csv.DictReader()` and `with open(...)` for safe file handling
- Groups rows by `(detector_name, date)` and fills each `ResultValue`'s `results` list via `add_result`
- Prints a one-line summary per object using its analysis methods (average, max, range)

Try the lab yourself first, then use this for reference.
