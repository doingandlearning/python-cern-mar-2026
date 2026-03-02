# Lab 5: Building a Data Analysis Toolkit with Functions

## Objective
In this lab, you'll refactor your data analysis script into a set of reusable functions. You'll define functions that take parameters and return values, so the same logic can be called from different places and tested easily.

You will:
1. Set up a script with the readings data
2. Write a function to get the word count of a single reading
3. Write a function to find readings containing a keyword
4. Write a main function that uses the others to analyse all readings

---

## Scenario: Reusable Data Analysis

Your list of readings is the same as in Lab 4. This time you'll wrap the logic in functions: one to count words in a string, one to filter by keyword, and one to run the full analysis and print results. This makes the code easier to reuse and test.

---

## Task 1: Set Up the Script and Data

Create a file `data_analyzer.py` and add the readings list.

**Your task:**

- Create `data_analyzer.py`
- Add the same `readings` list as in Lab 4 (or the list from the Lab 4 instructions)
- Run the file to confirm it has no syntax errors

**Hints:**

- You don’t need to change the list; just have it in the file so later tasks can use it

<details>
<summary>Possible readings list</summary>

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

## Task 2: Write a Function to Get Word Count

Add a function that returns the number of words in a single reading string.

**Your task:**

- Define `get_word_count(reading_text)` that takes one string argument
- Inside the function, use `.split()` and `len()` to count words
- Return the count (an integer)

**Hints:**

- Use `def get_word_count(reading_text):` and indent the body
- `return len(reading_text.split())` is enough for the body

<details>
<summary>Possible Solution for Task 2</summary>

```python
def get_word_count(reading_text):
    return len(reading_text.split())
```

</details>

---

## Task 3: Write a Function to Find Readings with a Keyword

Add a function that returns a list of readings that contain a given keyword (case-insensitive).

**Your task:**

- Define `find_readings_with_keyword(list_of_readings, keyword)` with two parameters
- Create an empty list, loop over `list_of_readings`, and for each reading check if `keyword.lower()` is in `reading.lower()`
- If it is, append that reading to the list
- Return the list of matching readings

**Hints:**

- Use a `for` loop; use `.lower()` on both the keyword and the reading when comparing
- Return the list you built

<details>
<summary>Possible Solution for Task 3</summary>

```python
def find_readings_with_keyword(list_of_readings, keyword):
    matching = []
    for reading in list_of_readings:
        if keyword.lower() in reading.lower():
            matching.append(reading)
    return matching
```

</details>

---

## Task 4: Write a Main Analysis Function

Add a function that analyses all readings and prints the average word count (and optionally calls the search function).

**Your task:**

- Define `analyse_all_readings(list_of_readings)` that takes the full list
- Use a loop and your `get_word_count()` to sum the word count of every reading
- Compute the average (total words ÷ number of readings) and print it along with the total count
- At the end of the script, call `analyse_all_readings(readings)` (and optionally test `find_readings_with_keyword` with a keyword)

**Hints:**

- Initialise `total_words = 0`, then in the loop add `get_word_count(reading)` to it
- Use `len(list_of_readings)` for the number of readings
- Use an f-string or multiple `print()` calls to show the results

<details>
<summary>Possible Solution for Task 4</summary>

```python
def analyse_all_readings(list_of_readings):
    total_words = 0
    for reading in list_of_readings:
        total_words += get_word_count(reading)
    average = total_words / len(list_of_readings)
    print(f"Total readings: {len(list_of_readings)}")
    print(f"Total words: {total_words}")
    print(f"Average words per reading: {average:.1f}")

# Call it when the script runs
if __name__ == "__main__":
    analyse_all_readings(readings)
    matches = find_readings_with_keyword(readings, "detector")
    print(f"Readings containing 'detector': {len(matches)}")
```

</details>

---

## Key Concepts Demonstrated

- **Function definition**: `def name(params):` and indented body
- **Parameters and return**: Passing data in, returning a value with `return`
- **Reuse**: One function (`get_word_count`) used inside another (`analyse_all_readings`)

---

## Next Steps

In the next lab, you’ll use list comprehensions to do similar operations in a more compact way.
