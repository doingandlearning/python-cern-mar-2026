# Lab 7: Structuring Data with Classes

## Objective

In class you built a **class** (e.g. `ResultValue`) that holds detector name, date, and a list of numeric results, with methods like `add_result`, `get_average_of_results`, `get_maximum_of_results`, and `get_range_of_results`. You don’t need to implement those again here.

In this lab you’ll **use** that class for analysis: create several result objects, add data to each, and produce a short **report** (average, max, range per detector). You’ll also extend the class with one or two extra analysis methods that are useful for your context.

You will:
1. Use the `ResultValue` (or similar) class from class and create one object with some results
2. Create several such objects (different detectors/dates), add results to each, and put them in a list
3. Loop over the list and print an analysis report (average, max, range for each)
4. Add at least one extra analysis method that answers a question you care about (e.g. minimum, count above a threshold)
5. (Optional) Add or improve `__str__` so each object prints nicely in the report

---

## Scenario: Analysis Report from Result Objects

**Prerequisite:** You have a class from the lesson that holds detector name, date, and a list of results, with methods to add a result and to compute average, maximum, and range. Here you’ll use it to build a small “analysis report”: multiple detectors (or multiple dates), each with its own list of values, and you’ll print the key stats for each.

---

## Starter: The Class from Class

If you saved the class from the lesson, use it. If not, you can use the following so you can do the lab without re-implementing the methods.

<details>
<summary>Starter: ResultValue class (use this if you don't have the class from class)</summary>

```python
class ResultValue:
    def __init__(self, detector_name, date):
        self.detector_name = detector_name
        self.date = date
        self.results = []

    def add_result(self, value):
        self.results.append(value)

    def get_average_of_results(self):
        if not self.results:
            return None
        return sum(self.results) / len(self.results)

    def get_maximum_of_results(self):
        return max(self.results) if self.results else None

    def get_range_of_results(self):
        if not self.results:
            return None
        return max(self.results) - min(self.results)
```

</details>

---

## Task 1: One Object and Its Stats

Create a file `result_analysis.py` (or similar).

**Your task:**

- Use the `ResultValue` class (from class or from the starter above)
- Create one object (e.g. detector name `"Detector A"`, date `"2026-03-03"`)
- Call `add_result(...)` several times with different numbers
- Print the average, maximum, and range by calling `get_average_of_results()`, `get_maximum_of_results()`, and `get_range_of_results()`

**Hints:**

- Create the object, then call `obj.add_result(100)`, `obj.add_result(200)`, etc.
- Use the methods to get the values and `print()` them

<details>
<summary>Possible Solution for Task 1</summary>

```python
result = ResultValue("Detector A", "2026-03-03")
result.add_result(123)
result.add_result(123)
result.add_result(414)
print("Average:", result.get_average_of_results())
print("Max:", result.get_maximum_of_results())
print("Range:", result.get_range_of_results())
```

</details>

---

## Task 2: Several Objects in a List

Create multiple result objects (different detector names and/or dates), add different numeric results to each, and put the objects in a list.

**Your task:**

- Create at least 2–3 `ResultValue` objects (e.g. different detectors or different dates)
- For each, call `add_result(...)` with a few values (they can be realistic measurements or simple numbers)
- Put all the objects in one list (e.g. `results_list`)

**Hints:**

- Build the list by appending each object after you’ve added its results
- You can use the same detector name with different dates, or different detector names

<details>
<summary>Possible Solution for Task 2</summary>

```python
r1 = ResultValue("Detector A", "2026-03-03")
r1.add_result(123)
r1.add_result(123)
r1.add_result(414)

r2 = ResultValue("Detector B", "2026-03-03")
r2.add_result(12)
r2.add_result(12)
r2.add_result(12)

results_list = [r1, r2]
```

</details>

---

## Task 3: Print an Analysis Report

Loop over the list of result objects and, for each one, print a short line of analysis: detector name, date, average, max, and range.

**Your task:**

- Loop over the list you built in Task 2
- For each object, call its methods and print something like:  
  `Detector A (2026-03-03): avg=220.0, max=414, range=291`
- Handle the case where a result list might be empty (e.g. print `"no data"` or skip)

**Hints:**

- Use a `for` loop; for each item call `get_average_of_results()`, `get_maximum_of_results()`, `get_range_of_results()` and format the output

<details>
<summary>Possible Solution for Task 3</summary>

```python
for r in results_list:
    avg = r.get_average_of_results()
    mx = r.get_maximum_of_results()
    rng = r.get_range_of_results()
    if avg is not None:
        print(f"{r.detector_name} ({r.date}): avg={avg}, max={mx}, range={rng}")
    else:
        print(f"{r.detector_name} ({r.date}): no data")
```

</details>

<details>
<summary>Possible extensions to Task 3</summary>

- Sort the list before printing (e.g. by average or by maximum) to see the “top-performing” detector first.
- Add units to your printout if your results represent something real (e.g. `events`, `counts`, `°C`).

</details>

---

## Task 4: Add an Extra Analysis Method

Now that you have basic stats (average, max, range), add at least one **extra analysis method** to the class that answers a question you care about.

**Your task:**

- Pick **one (or more)** of these ideas and add a method for it:
  - `get_minimum_of_results(self)` — return the minimum value (similar to max).
  - `count_results_above(self, threshold)` — return how many results are strictly above a given threshold.
  - `has_anomaly(self, threshold)` — return `True` if any result is above a threshold, otherwise `False`.
- Update your report loop to use your new method(s) and print the result.

**Hints:**

- For minimum: you can mirror the max implementation but use `min(self.results)`.
- For counts: start a counter at 0, loop over `self.results`, and increment when the condition is true.
- For yes/no: you can either loop and return early when you see an anomalous value, or reuse an existing method (e.g. `get_maximum_of_results() > threshold`).

<details>
<summary>Possible Solution for Task 4</summary>

```python
def get_minimum_of_results(self):
    return min(self.results) if self.results else None

def count_results_above(self, threshold):
    count = 0
    for value in self.results:
        if value > threshold:
            count += 1
    return count
```

In your report loop you might do:

```python
for r in results_list:
    avg = r.get_average_of_results()
    mx = r.get_maximum_of_results()
    rng = r.get_range_of_results()
    above = r.count_results_above(200)  # example threshold
    if avg is not None:
        print(f"{r.detector_name} ({r.date}): avg={avg}, max={mx}, range={rng}, >200={above}")
    else:
        print(f"{r.detector_name} ({r.date}): no data")
```

</details>

---

## Task 5 (Optional): Add or Improve `__str__`

If your class doesn’t have a `__str__` method yet, add one so that `print(r)` shows a useful one-line summary (e.g. detector name, date, and maybe count of results or average). Then in your report loop you can use `print(r)` or combine `str(r)` with the stats.

**Hints:**

- Define `def __str__(self):` inside the class and `return` a string using `self.detector_name`, `self.date`, and optionally `len(self.results)` or `get_average_of_results()`

<details>
<summary>Possible approach for Task 4</summary>

```python
def __str__(self):
    return f"{self.detector_name} ({self.date}): {len(self.results)} results"
```

Then in the loop you might do: `print(r, "->", r.get_average_of_results(), r.get_maximum_of_results(), r.get_range_of_results())`.

</details>

---

**You're done when** you have a script that creates multiple result objects, adds results to each, prints an analysis report (average, max, range per object), and uses at least one extra analysis method of your own (e.g. minimum or count-above-threshold).

---

## Key Concepts Demonstrated

- **Using a class**: Creating instances and calling methods instead of reaching into dicts
- **Encapsulation**: Data (detector name, date, results list) and analysis (average, max, range, your extra methods) live together
- **Collections of objects**: A list of result objects lets you run the same analysis over many detectors or dates (and apply new analysis methods consistently)

---

## Common Issues

- **AttributeError or empty stats** — If you never call `add_result`, the results list is empty; your get_* methods should handle that (e.g. return `None`) and your report loop should check before printing.
- **Class not defined** — Use the starter class in the collapsible section above if you don’t have the one from class.

---

## Next Steps

In the next lab, you’ll move your class into its own module and import it from a main script. We’ll also introduce a small class for text-based readings when we load data from files.
