# Lab 6: Supercharging Analysis with List Comprehensions

## Objective
In this lab, you'll use **list comprehensions** to transform and filter your list of readings in a single line of code. List comprehensions are a concise, Pythonic way to build new lists from existing ones - very common when processing experimental or sensor data.

You will:
1. Use a list comprehension to map each reading to its word count
2. Use a list comprehension to filter readings (e.g. 7 words or fewer)
3. Combine mapping and filtering in one comprehension (e.g. word counts of readings containing a keyword)

---

## Scenario: Same Data, New Syntax

**Prerequisite:** Same `readings` list as in Lab 4 (or from Lab 5). This time you'll build new lists using comprehensions: `[expression for item in list]` for mapping and `[item for item in list if condition]` for filtering. The result is shorter, readable code.

---

## Task 1: Set Up the File and Data

Create a file `comprehensions_analysis.py` and add the readings list (same as in Lab 4/5).

**Your task:**

- Create the file and define or paste in the `readings` list
- Optionally print `readings` or `len(readings)` to confirm the data is there

**Hints:**

- Use the same list of 8–10 reading strings as in previous labs

<details>
<summary>Possible setup</summary>

```python
readings = [
    "Temperature spike detected in Sector 7 cooling system",
    "Pressure nominal in Detector A",
    "Calibration run completed for beam line B2",
    # ... add the rest from Lab 4 ...
]
print(f"Loaded {len(readings)} readings")
```

</details>

---

## Task 2: Mapping with a List Comprehension

Build a list of word counts, one per reading.

**Your task:**

- Create a variable `reading_lengths` that is a list of the word count of each reading
- Use a list comprehension: for each `reading` in `readings`, the expression should be the number of words in that reading
- Print `reading_lengths` to verify (e.g. first value should be the word count of the first reading)

**Hints:**

- Syntax: `[expression for item in list]`
- For each `reading`, the number of words is `len(reading.split())`

<details>
<summary>Possible Solution for Task 2</summary>

```python
reading_lengths = [len(reading.split()) for reading in readings]
print("Word counts per reading:", reading_lengths)
```

</details>

---

## Task 3: Filtering with a List Comprehension

Build a list of only the "short" readings (e.g. 7 words or fewer).

**Your task:**

- Create a variable `short_readings` that contains only readings with 7 words or fewer
- Use the filtering form: `[item for item in list if condition]`
- The condition should use the word count of each reading
- Print `short_readings` or its length to verify

**Hints:**

- Condition: `len(reading.split()) <= 7`

<details>
<summary>Possible Solution for Task 3</summary>

```python
short_readings = [reading for reading in readings if len(reading.split()) <= 7]
print(f"Readings with 7 words or fewer: {len(short_readings)}")
print(short_readings)
```

</details>

---

## Task 4: Combining Mapping and Filtering

Build a list of word counts for only the readings that contain a certain keyword.

**Your task:**

- Create a variable `specific_reading_lengths` that contains the word counts of only those readings that contain the word `"detector"` (or another keyword you choose)
- Use the form `[expression for item in list if condition]`: the expression is the word count, the condition is that the keyword appears in the reading (case-insensitive)
- Print the result

**Hints:**

- Expression: `len(reading.split())`
- Condition: `"detector" in reading.lower()`

<details>
<summary>Possible Solution for Task 4</summary>

```python
specific_reading_lengths = [
    len(reading.split()) for reading in readings
    if "detector" in reading.lower()
]
print("Word counts of readings containing 'detector':", specific_reading_lengths)
```

</details>

---

**You're done when** the comprehensions produce the expected lists and the script runs without errors.

---

## Extensions (Optional)

If you finish the main tasks, try one or more of these. They reuse the same `readings` list and give you more practice with comprehensions.

- **Extension 1: Long readings only**
  - Build a list of readings that have **more than** 7 words (the opposite of Task 3).
  - Use the same filtering form; change the condition.

- **Extension 2: Keyword from the user**
  - Use `input()` to ask for a keyword, then build the "word counts of readings containing this keyword" list using that variable instead of the literal `"detector"`.
  - Remember case-insensitive matching (e.g. `.lower()`).

- **Extension 3: First word of each reading**
  - Build a list of the **first word** of each reading (e.g. `"Temperature"`, `"Pressure"`, `"Calibration"`).
  - Use a mapping comprehension; the expression can use `.split()` and indexing.

**You're done with the extensions when** your script still satisfies the main "You're done when" and you've tried at least one of the ideas above.

<details>
<summary>Possible approaches for extensions</summary>

- **Long readings:** Same as Task 3 but condition `len(reading.split()) > 7` (or `>= 8`).
- **Keyword from user:** Store `keyword = input("Keyword? ").strip()` then use `keyword.lower() in reading.lower()` in the condition.
- **First word:** Expression `reading.split()[0]` (assumes every reading has at least one word).

</details>

---

## Key Concepts Demonstrated

- **Mapping**: `[expression for item in list]` — build a new list by applying an expression to each item
- **Filtering**: `[item for item in list if condition]` — keep only items that satisfy the condition
- **Combining**: `[expression for item in list if condition]` — filter then map in one line

---

## Common Issues

- **SyntaxError or unexpected result** — In a comprehension the order is `[expression for item in list if condition]`. The `if` comes after the `for ... in ...`; the expression is first.
- **Empty list when you expect matches** — Check that your condition uses the same case as the data (e.g. `keyword.lower() in reading.lower()`).
- **IndexError when taking first word** — If you use `.split()[0]`, make sure every reading has at least one word, or add a condition to skip empty strings.

---

## Next Steps

In the next lab, you’ll introduce a `DataReading` class so each reading can hold both text and source (e.g. detector name).
