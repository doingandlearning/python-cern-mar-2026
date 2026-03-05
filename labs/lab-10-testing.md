# Lab 10: Testing Your Analysis Class with pytest

## Objective

Write automated tests for your **result-analysis class** (e.g. `ResultValue` from Labs 7–8) using `pytest`. You are **not** changing the class here — only writing tests that check it behaves as expected. This locks in behaviour and catches regressions when you change code later.

You will:
1. Create a test file and import your class from `results_module`
2. Test that object creation stores detector name and date
3. Test analysis methods like `get_average_of_results`, `get_maximum_of_results`, and `get_range_of_results`
4. Add at least one edge-case test (e.g. no results yet)
5. (Optional) Reduce duplication with a helper or `@pytest.mark.parametrize`

---

## Scenario: Testing Without Changing the Class

You have a class (e.g. `ResultValue` in `results_module.py`) that holds detector name, date, and a list of numeric results, with methods to add a result and compute average, maximum, range, and any extra analysis you added in Lab 7. Here you’ll write tests that create objects, call those methods, and use `assert` to check behaviour. Running `pytest` will run all those tests.

**Setup:** If pytest isn’t installed, run `pip install pytest`.

---

## Task 1: Create the Test File

**Your task:**

- Create a new file named `test_results.py` next to `results_module.py`
- At the top, import the class: `from results_module import ResultValue` (or whatever you named it)
- Run `pytest` and confirm it discovers the file (you can have no tests at first, or one dummy test)

**Hints:**

- Test file names often start with `test_` so pytest finds them
- Test functions must start with `test_` (e.g. `def test_something():`)

<details>
<summary>Possible setup</summary>

```python
# test_results.py
import pytest
from results_module import ResultValue
```

</details>

---

## Task 2: Test Object Creation

**Your task:**

- Write a test function that creates a `ResultValue` with a known detector name and date
- Use `assert` to check that the attributes on the object match what you passed in (and that `results` starts empty)

**Hints:**

- Function name: e.g. `def test_result_stores_name_date_and_starts_empty():`
- Use simple values, e.g. `ResultValue("Detector A", "2026-03-03")`

<details>
<summary>Possible Solution for Task 2</summary>

```python
def test_result_stores_name_date_and_starts_empty():
    r = ResultValue("Detector A", "2026-03-03")
    assert r.detector_name == "Detector A"
    assert r.date == "2026-03-03"
    assert r.results == []
```

</details>

---

## Task 3: Test `add_result` and Basic Stats

**Your task:**

- Write a test that:
  - creates a `ResultValue`
  - calls `add_result(...)` a few times with known numbers
  - asserts that:
    - `results` contains those numbers
    - `get_average_of_results()` returns the expected average
    - `get_maximum_of_results()` returns the expected max
    - `get_range_of_results()` returns the expected range (max − min)

**Hints:**

- Choose small, easy-to-check numbers (e.g. 10, 20, 30 → avg 20, max 30, range 20)
- Call the methods and compare with the values you would compute by hand

<details>
<summary>Possible Solution for Task 3</summary>

```python
def test_basic_stats_after_adding_results():
    r = ResultValue("Detector A", "2026-03-03")
    r.add_result(10)
    r.add_result(20)
    r.add_result(30)

    assert r.results == [10, 20, 30]
    assert r.get_average_of_results() == 20
    assert r.get_maximum_of_results() == 30
    assert r.get_range_of_results() == 20
```

</details>

---

## Task 4: Add One Edge Case

**Your task:**

- Pick one or more edge cases and decide what the methods *should* return, for example:
  - A new object with no results yet
  - A single result only
  - All results equal (e.g. [5, 5, 5])
- Write tests that assert that behaviour (e.g. `get_average_of_results()` returns `None` or a specific value when there are no results, depending on how you wrote the class)

**Hints:**

- If your implementation returns `None` for empty `results`, assert exactly that
- For a single result `[42]`, you might expect average 42, max 42, range 0

<details>
<summary>Possible Solution for Task 4</summary>

```python
def test_stats_on_empty_results_are_none():
    r = ResultValue("Detector A", "2026-03-03")
    assert r.get_average_of_results() is None
    assert r.get_maximum_of_results() is None
    assert r.get_range_of_results() is None
```

</details>

---

## Task 5: Reduce Duplication (Optional)

**Your task:**

- Either: introduce a small helper that creates a `ResultValue` and use it in two or more tests, or
- Use `@pytest.mark.parametrize` to run one test function with several (list_of_results, expected_average, expected_max, expected_range) cases

**Hints:**

- A helper might look like:

  ```python
  def make_result(values):
      r = ResultValue("Detector A", "2026-03-03")
      for v in values:
          r.add_result(v)
      return r
  ```

- A parametrized test could pass different lists and expected stats

<details>
<summary>Possible parametrized test</summary>

```python
@pytest.mark.parametrize("values, avg, mx, rng", [
    ([10], 10, 10, 0),
    ([1, 2, 3], 2, 3, 2),
    ([5, 5, 5], 5, 5, 0),
])
def test_stats_for_various_sets_of_results(values, avg, mx, rng):
    r = ResultValue("Detector A", "2026-03-03")
    for v in values:
        r.add_result(v)

    assert r.get_average_of_results() == avg
    assert r.get_maximum_of_results() == mx
    assert r.get_range_of_results() == rng
```

</details>

---

## Running Tests

```bash
pytest
```

For more detail:

```bash
pytest -v
```

---

**You're done when** pytest discovers and runs your tests and they all pass (including at least one edge-case test and at least one test that checks one of your analysis methods).

---

## Key Concepts Demonstrated

- **Test**: A function that uses `assert` to check one behaviour of the class
- **pytest**: Discovers and runs functions whose names start with `test_`
- **Edge cases**: Tests for empty results, single result, all-equal lists, etc., document and protect behaviour
- **Regression safety**: Once tests pass, you can change the implementation of `ResultValue` later and re-run tests to ensure behaviour stays consistent

---

## Next Steps

In the next lab, you’ll load data from a CSV file instead of hard-coding it in the script, and you can later combine that with your analysis class for end‑to‑end testing.

