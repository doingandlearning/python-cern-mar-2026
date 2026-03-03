# Lab 8: Organizing Your Code with Modules

## Objective
As projects grow, one big file becomes hard to maintain. **Modules** let you split code into separate files: one file can define the `DataReading` class, and another can import it and run the analysis. This keeps responsibilities clear and makes the class reusable.

You will:
1. Put the `DataReading` class in its own file (`reading_module.py`)
2. Create a main script (`main_analysis.py`) that imports `DataReading` and runs the analysis
3. Use `if __name__ == "__main__":` so the main script only runs when executed directly

---

## Scenario: Two Files Instead of One

You already have a `DataReading` class and code that builds a list of readings and analyses them. Here you’ll move the class into `reading_module.py` and keep the list + analysis logic in `main_analysis.py`, importing the class from the module.

---

## Task 1: Create `reading_module.py`

**Your task:**

- Create a new file named `reading_module.py`
- Move the entire `DataReading` class (including `__init__`, `__str__`, and `get_word_count`) into this file
- Do not put any code that creates readings or runs analysis in this file — only the class definition

**Hints:**

- Copy the `class DataReading:` block and all its methods from your previous lab
- The file should contain nothing else (no list of readings, no `print` calls that run on import)

<details>
<summary>Possible Solution for Task 1</summary>

```python
# reading_module.py
class DataReading:
    def __init__(self, text, source):
        self.text = text
        self.source = source

    def __str__(self):
        return f"{self.text} ({self.source})"

    def get_word_count(self):
        return len(self.text.split())
```

</details>

---

## Task 2: Create `main_analysis.py` and Import the Class

**Your task:**

- Create a file named `main_analysis.py`
- At the top, add: `from reading_module import DataReading`
- Add your list of `DataReading` objects (create them with `DataReading(text, source)`) and your analysis loop (e.g. print each reading and its word count, or reuse logic from earlier labs)
- Run `main_analysis.py` and confirm the output matches what you had before

**Hints:**

- After the import, use `DataReading(...)` exactly as you did when the class was in the same file
- Keep the readings data and the loop in `main_analysis.py`, not in the module

<details>
<summary>Possible Solution for Task 2</summary>

```python
# main_analysis.py
from reading_module import DataReading

readings = [
    DataReading("Temperature spike detected in Sector 7 cooling system", "Detector A"),
    DataReading("Pressure nominal in Detector A", "Detector A"),
    # ... more ...
]
for r in readings:
    print(r.get_word_count(), r.text)
```

</details>

---

## Task 3: Use `if __name__ == "__main__"`

**Your task:**

- Wrap the main script logic (creating the list and running the analysis) in a function, e.g. `def main():`
- At the bottom of `main_analysis.py`, add:
  - `if __name__ == "__main__":`
  - On the next line, indented, call `main()`
- Run the file again and confirm behaviour is unchanged

**Hints:**

- Code inside `if __name__ == "__main__":` runs only when the file is executed (e.g. `python main_analysis.py`), not when it is imported
- This keeps the script runnable while still allowing other files to import from it without running the analysis

<details>
<summary>Possible Solution for Task 3</summary>

```python
def main():
    readings = [
        DataReading("Temperature spike detected in Sector 7 cooling system", "Detector A"),
        # ...
    ]
    for r in readings:
        print(r.get_word_count(), r.text)

if __name__ == "__main__":
    main()
```

</details>

---

**You're done when** the class lives in `reading_module.py`, `main_analysis.py` imports it and runs the analysis, and the script only runs when executed directly (not when imported).

---

## Key Concepts Demonstrated

- **Module**: A Python file that can be imported (`import reading_module` or `from reading_module import DataReading`)
- **Separation of concerns**: Class definition in one file, usage in another
- **`if __name__ == "__main__"`**: Run code only when the file is executed, not when imported

---

## Next Steps

In the next lab, you’ll add error handling so that programs cope gracefully with invalid input.
