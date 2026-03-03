# Lab 5: Building a Data Analysis Toolkit with Functions

## Objective
In this lab, you'll refactor your data analysis script into a set of reusable functions. You'll define functions that take parameters and return values, so the same logic can be called from different places and tested easily.

You will:
1. Set up a script with the readings data
2. Write a function to get the word count of a single reading
3. Write a function to find readings containing a keyword
4. Write a main function that uses the others to analyse all readings
5. Write a function to find the longest reading (or its word count)
6. Write a function to filter readings by minimum word count
7. (Optional) Try the extensions for more practice

---

## Scenario: Reusable Data Analysis

**Prerequisite:** Use the same `readings` list as in Lab 4. This time you'll wrap the logic in functions: one to count words in a string, one to filter by keyword, and one to run the full analysis and print results. This makes the code easier to reuse and test.

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

## Task 5: Write a Function to Find the Longest Reading

Add a function that returns the reading with the most words (or its word count, depending on how you design it).

**Your task:**

- Define a function that takes the list of readings and returns either:
  - the **text** of the longest reading, or
  - a **tuple** `(reading_text, word_count)` for the longest one
- Use your `get_word_count()` inside the function
- If the list is empty, decide what to return (e.g. `None` or an empty string) and document it in a comment

**Hints:**

- Loop over the readings and keep track of the maximum word count seen so far (and the reading that had it)
- Initialise your “best so far” before the loop; update it whenever you find a reading with more words

<details>
<summary>Possible Solution for Task 5</summary>

```python
def get_longest_reading(list_of_readings):
    if not list_of_readings:
        return None
    longest = list_of_readings[0]
    for reading in list_of_readings:
        if get_word_count(reading) > get_word_count(longest):
            longest = reading
    return longest
```

</details>

---

## Task 6: Write a Function to Filter by Word Count

Add a function that returns only the readings that have at least a given number of words.

**Your task:**

- Define `readings_with_at_least_n_words(list_of_readings, n)` (or a similar name)
- Loop over the list and keep only readings where `get_word_count(reading) >= n`
- Return a new list of those readings

**Hints:**

- Build an empty list and append each reading that passes the test
- Reuse `get_word_count()` so you don’t duplicate logic

<details>
<summary>Possible Solution for Task 6</summary>

```python
def readings_with_at_least_n_words(list_of_readings, n):
    result = []
    for reading in list_of_readings:
        if get_word_count(reading) >= n:
            result.append(reading)
    return result
```

</details>

---

**You're done when** all functions work and running the main script prints the full analysis (count, average, keyword search), and you’ve written and tested at least the longest-reading and filter-by-word-count functions.

---

## Extensions (Optional)

If you finish the main tasks, try one or more of these. They give you more practice with parameters, return values, and reusing your existing functions.

- **Extension 1: Short readings**
  - Write a function that returns readings with **at most** N words (e.g. 5 words or fewer).
  - Reuse `get_word_count()` and the same “loop and append” pattern as in Task 6.

- **Extension 2: Return the average**
  - Write a function `average_word_count(list_of_readings)` that **returns** the average as a float (instead of printing it).
  - Use it inside `analyse_all_readings()` so the main analysis still prints the same info, but the number is computed by the new function.

- **Extension 3: Formatted line for one reading**
  - Write a function `format_reading(reading_text, index)` that returns a single formatted string for one reading, e.g. `"  1. Temperature spike detected in Sector 7..."`.
  - Use it in a loop to print a numbered list of readings (or of matching readings from a keyword search).

**You're done with the extensions when** your script still passes the main “You're done when” and you’ve tried at least one of the ideas above.

<details>
<summary>Possible approaches for extensions</summary>

- **Short readings:** Same structure as Task 6, but condition is `get_word_count(reading) <= n`.
- **Return the average:** Sum words in a loop (or reuse logic from `analyse_all_readings`), then `return total_words / len(list_of_readings)` (handle empty list if you like).
- **Formatted line:** `return f"  {index}. {reading_text}"` (or add a word count: `f"  {index}. {reading_text} ({get_word_count(reading_text)} words)"`).

</details>

---

## Key Concepts Demonstrated

- **Function definition**: `def name(params):` and indented body
- **Parameters and return**: Passing data in, returning a value with `return`
- **Reuse**: One function (e.g. `get_word_count`) used inside others (`analyse_all_readings`, `get_longest_reading`, filter functions)
- **Filtering and searching**: Functions that loop and build a new list (e.g. by keyword or by word count)

---

## Next Steps

In the next lab, you’ll use list comprehensions to do similar operations in a more compact way.
