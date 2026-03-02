# Lab 11: Reading Data From a File - Solutions

This folder contains solutions for Lab 11: loading readings from `data.csv` and building a list of `DataReading` objects.

## Files

| File | Description |
|------|-------------|
| `file_reader.py` | Main solution: loads from `data.csv`, creates `DataReading` objects, runs analysis and search |
| `reading_module.py` | Defines the `DataReading` class (used by `file_reader.py`) |
| `data.csv` | Sample CSV with columns `text` and `source` |

## Run

From this directory (so `data.csv` and `reading_module.py` are on the path):

```bash
python file_reader.py
```

## Requirements

- `data.csv` in the same directory (columns: text, source)
- `reading_module.py` with the `DataReading` class

## Key behaviour

- Uses `csv.reader()` and `with open(...)` for safe file handling
- Skips the header row, then creates `DataReading(row[0], row[1])` for each row
- Appends each object to a `readings` list for analysis

Try the lab yourself first, then use this for reference.
