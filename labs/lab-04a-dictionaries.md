# Lab 4a - Summarising Readings with Dictionaries

## Objective

In this lab, you’ll use **dictionaries** to organise and summarise experimental readings by detector or source.

You will:
1. Use a dictionary to map detector names to event counts
2. Look up values safely using keys
3. Loop over dictionary items to print a summary report
4. Update and extend the dictionary with new data

---

## Scenario: Counts per Detector

You’ve run a short experiment and noted how many events each detector recorded. You want a quick way to:

- see the count for a specific detector,
- see a summary for all detectors,
- update the counts if you re‑run part of the experiment,
- add a new detector to the setup.

Dictionaries are a good fit for this: they map a **key** (detector name) to a **value** (event count).

---

## Starter Data Structure

Use the following data structure as your starting point. You don’t need to change these values unless a task tells you to.

```python
# Starting data structure: detector -> event count
detector_counts = {
    "Detector A": 120,
    "Detector B": 95,
    "Detector C": 143,
}
```

(You can paste this near the top of your Python file.)

---

## Task 1: Explore the Dictionary

Create a new Python file, for example `detector_counts.py`.

**Your task:**

- Paste the `detector_counts` dictionary from the starter data structure into your file.
- Print the whole dictionary.
- Print the count for one detector directly using its key (e.g. `"Detector A"`).

**Hints:**

- Access by key with square brackets:

  ```python
  # shape only
  print(detector_counts["Detector A"])
  ```

- Be careful with spelling and capitalisation in the key.

**You're done when** running the script prints:
- the entire dictionary, and  
- the count for one specific detector.

<details>
<summary>Possible Solution for Task 1</summary>

```python
detector_counts = {
    "Detector A": 120,
    "Detector B": 95,
    "Detector C": 143,
}

print(detector_counts)
print(detector_counts["Detector A"])
```

</details>

---

## Task 2: Look Up Counts Safely

Now you’ll look up the count for a detector name entered by the user, and handle the case where it doesn’t exist.

**Your task:**

- Ask the user for a detector name using `input()`.
- If the name exists as a key in `detector_counts`, print its count.
- If it does **not** exist, print a friendly message (don’t crash).

**Hints:**

- Use `in` to test for a key:

  ```python
  # shape only
  if name in detector_counts:
      ...
  ```

- Or use `.get()` with a default value and test that:

  ```python
  # shape only
  count = detector_counts.get(name)
  ```

- Decide what you want the “not found” message to say.

**You're done when**:

- Entering `"Detector A"` (or another known key) prints its count.
- Entering some other name prints your “not found” message instead of an error.

<details>
<summary>Possible Solution for Task 2</summary>

```python
name = input("Which detector? ")

if name in detector_counts:
    print(f"{name} has {detector_counts[name]} events.")
else:
    print(f"No data for detector '{name}'.")
```

</details>

---

## Task 3: Print a Summary Report

You want a short report listing all detectors and their counts, plus some totals.

**Your task:**

- Loop over the dictionary and print one line per detector, like:  
  `Detector A: 120 events`
- While looping, keep a running **total** of all events across detectors.
- After the loop, print:
  - the total number of events
  - the number of detectors in the dictionary.

**Hints:**

- Use `.items()` to get both key and value:

  ```python
  # shape only
  for name, count in detector_counts.items():
      ...
  ```

- Start a `total_events` variable at 0 and add each `count`.
- Use `len(detector_counts)` for the number of detectors.

**You're done when** running the script prints:
- one readable line per detector, and
- a final line (or two) showing the overall total and how many detectors there are.

<details>
<summary>Possible Solution for Task 3</summary>

```python
total_events = 0

for name, count in detector_counts.items():
    print(f"{name}: {count} events")
    total_events += count

print(f"Total events: {total_events}")
print(f"Number of detectors: {len(detector_counts)}")
```

</details>

---

## Task 4: Add or Update a Detector

In real experiments, you might add a new detector or re‑run part of the experiment and increase a count.

**Your task:**

- Ask the user for a detector name and a number of events.
- If the detector **already exists**:
  - Decide whether to **replace** the count or **add** to it (your choice), and update the dictionary.
- If the detector **does not exist**:
  - Add a new entry to the dictionary with that name and count.
- After updating, re‑run your summary report from Task 3 to show the new state.

**Hints:**

- You can use the same `in` check as in Task 2.
- Updating an existing value might look like:

  ```python
  # shape only
  detector_counts[name] = detector_counts[name] + extra_events
  ```

- Adding a brand new detector is just assigning to a new key:

  ```python
  # shape only
  detector_counts[name] = new_count
  ```

**You're done when**:

- Adding events for an existing detector changes its count in the report.
- Adding a completely new detector makes it appear in the report with the correct value.

<details>
<summary>Possible Solution for Task 4</summary>

```python
name = input("Detector name: ")
events = int(input("Number of events: "))

if name in detector_counts:
    detector_counts[name] = detector_counts[name] + events
else:
    detector_counts[name] = events

# Reuse the summary code from Task 3 here
```

</details>

---

## Optional Extension: Start from Tuples

If you want to connect this with tuples and lists, try this extra step.

**Your task (optional):**

- Create a list of `(detector_name, count)` tuples, for example:

  ```python
  # example shape – choose your own values
  raw_readings = [
      ("Detector A", 120),
      ("Detector B", 95),
      ("Detector C", 143),
  ]
  ```

- Build a new dictionary from `raw_readings` by looping over the tuples and filling in a fresh `detector_counts_from_tuples` dict.
- Print a summary report using this new dictionary.

**Hints:**

- Unpack each tuple in the loop:

  ```python
  # shape only
  for name, count in raw_readings:
      ...
  ```

- Assign into the dictionary inside the loop.

**You're done with the extension when** you can generate the same kind of summary report starting from the list of tuples instead of the original dictionary literal.

<details>
<summary>Possible Solution for Optional Extension</summary>

```python
raw_readings = [
    ("Detector A", 120),
    ("Detector B", 95),
    ("Detector C", 143),
]

detector_counts_from_tuples = {}

for name, count in raw_readings:
    detector_counts_from_tuples[name] = count

# Then reuse your summary-report code on detector_counts_from_tuples
```

</details>

---

## Check Your Understanding

Ask yourself:

- When would I choose a **dictionary** instead of a **list** or **tuple**?
- Can I:
  - create a dictionary literal,
  - look up values by key without crashing,
  - loop over keys and values,
  - update existing entries and add new ones?

If yes, you’re in good shape for using dictionaries in the later labs.