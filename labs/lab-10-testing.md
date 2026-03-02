# Lab 10: Testing the DataReading Class with pytest

## Objective
Write automated tests for the `DataReading` class using `pytest`. You are **not** changing the class — only writing tests that check it behaves as expected. This locks in behaviour and catches regressions when you change code later.

You will:
1. Create a test file and import `DataReading`
2. Test that object creation stores `text` and `source`
3. Test `get_word_count()` with clear cases
4. Add at least one edge-case test (e.g. empty string)
5. (Optional) Reduce duplication with a helper or `@pytest.mark.parametrize`

---

## Scenario: Testing Without Changing the Class

You have a `DataReading` class (e.g. in `reading_module.py`). You’ll create `test_reading.py` (or `test_reading_module.py`) in the same directory, import the class, and write functions that create objects and use `assert` to check behaviour. Running `pytest` will run all those tests.

---

## Task 1: Create the Test File

**Your task:**

- Create a new file named `test_reading.py` (or `test_reading_module.py`) next to `reading_module.py`
- At the top, import the class: `from reading_module import DataReading`
- Run `pytest` and confirm it discovers the file (you can have no tests at first, or one dummy test)

**Hints:**

- Test file names often start with `test_` so pytest finds them
- Test functions must start with `test_` (e.g. `def test_something():`)

<details>
<summary>Possible setup</summary>

```python
# test_reading.py
import pytest
from reading_module import DataReading
```

</details>

---

## Task 2: Test Object Creation

**Your task:**

- Write a test function that creates a `DataReading` with known text and source
- Use `assert` to check that `r.text` and `r.source` match what you passed in

**Hints:**

- Function name: e.g. `def test_reading_stores_text_and_source():`
- Use simple values, e.g. `DataReading("One two three", "Detector A")`

<details>
<summary>Possible Solution for Task 2</summary>

```python
def test_reading_stores_text_and_source():
    r = DataReading("Temperature nominal", "Detector A")
    assert r.text == "Temperature nominal"
    assert r.source == "Detector A"
```

</details>

---

## Task 3: Test `get_word_count`

**Your task:**

- Write a test that creates a `DataReading` with text where the word count is obvious (e.g. "One two three" → 3)
- Call `r.get_word_count()` and assert the result equals the expected number

**Hints:**

- One clear test is enough to start
- Choose text you can count by hand

<details>
<summary>Possible Solution for Task 3</summary>

```python
def test_get_word_count_counts_words():
    r = DataReading("One two three", "Detector A")
    assert r.get_word_count() == 3
```

</details>

---

## Task 4: Add One Edge Case

**Your task:**

- Pick one edge case (e.g. empty string `""`, single word, or multiple spaces) and decide what the method *should* return
- Write a test that asserts that behaviour

**Hints:**

- Empty string: `len("".split())` is 0 in Python — so you might assert `get_word_count()` returns 0 for `DataReading("", "X")`
- Document the decision in a short comment if it’s not obvious

<details>
<summary>Possible Solution for Task 4</summary>

```python
def test_get_word_count_empty_string_is_zero():
    r = DataReading("", "Detector A")
    assert r.get_word_count() == 0
```

</details>

---

## Task 5: Reduce Duplication (Optional)

**Your task:**

- Either: introduce a small helper that creates a `DataReading` and use it in two or more tests, or
- Use `@pytest.mark.parametrize` to run one test function with several (text, expected_count) pairs

**Hints:**

- Parametrize example: `@pytest.mark.parametrize("text,expected", [("One", 1), ("One two", 2), ("", 0)])` then `def test_get_word_count_cases(text, expected): ... assert DataReading(text, "X").get_word_count() == expected`

<details>
<summary>Possible parametrized test</summary>

```python
@pytest.mark.parametrize("text, expected", [
    ("One", 1),
    ("One two", 2),
    ("One two three", 3),
    ("", 0),
])
def test_get_word_count_cases(text, expected):
    r = DataReading(text, "Detector A")
    assert r.get_word_count() == expected
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

## Key Concepts Demonstrated

- **Test**: A function that uses `assert` to check one behaviour
- **pytest**: Discovers and runs functions whose names start with `test_`
- **Edge cases**: Tests for empty input, single item, etc., document and protect behaviour

---

## Next Steps

In the next lab, you’ll load readings from a CSV file instead of hard-coding them in the script.
