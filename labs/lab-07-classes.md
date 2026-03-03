# Lab 7: Structuring Data with Classes

## Objective
So far you've worked with readings as plain strings. As data gets more complex, it helps to group related data and behaviour. **Classes** let you define a type that holds both the text of a reading and its source (e.g. detector name, sensor ID), plus methods like word count.

You will:
1. Define a `DataReading` class with `__init__(self, text, source)`
2. Add a `__str__` method for readable output
3. Add a `get_word_count()` method
4. (Optional) Build a list of `DataReading` objects and process them

---

## Scenario: Readings with a Source

**Prerequisite:** Use the same readings data (text and source) as in Lab 4 when building your `DataReading` objects. Each reading has two pieces of information: the text (e.g. "Temperature spike in Sector 7") and the source (e.g. "Detector A"). A class keeps these together and can provide behaviour (e.g. word count) that uses the object’s own data.

---

## Task 1: Define the `DataReading` Class

Create a file `reading_objects.py` (or similar).

**Your task:**

- Define a class named `DataReading`
- Add an `__init__(self, text, source)` method that stores `text` and `source` as attributes on the object (`self.text`, `self.source`)
- Create at least one object to test: e.g. `DataReading("Temperature spike in Sector 7", "Detector A")`

**Hints:**

- Start with `class DataReading:` and indent the method
- In `__init__`, assign `self.text = text` and `self.source = source`

<details>
<summary>Possible Solution for Task 1</summary>

```python
class DataReading:
    def __init__(self, text, source):
        self.text = text
        self.source = source

r = DataReading("Temperature spike detected in Sector 7 cooling system", "Detector A")
```

</details>

---

## Task 2: Add a String Representation

Add a `__str__` method so that `print(r)` shows something readable instead of a default object address.

**Your task:**

- Inside the class, define `def __str__(self):` that returns a string (e.g. the text and source combined)
- Use `return` with an f-string or concatenation
- Call `print(r)` to verify the output

**Hints:**

- The method must return a string
- e.g. `return f"{self.text} ({self.source})"`

<details>
<summary>Possible Solution for Task 2</summary>

```python
def __str__(self):
    return f"{self.text} ({self.source})"
```

</details>

---

## Task 3: Add a `get_word_count` Method

Add a method that returns the number of words in the reading’s text.

**Your task:**

- Define `def get_word_count(self):` inside the class
- Use `self.text` and the same logic as before (e.g. `len(self.text.split())`)
- Return the integer count
- Test with e.g. `print(r.get_word_count())`

**Hints:**

- Methods that use the object’s data take `self` and use `self.text`

<details>
<summary>Possible Solution for Task 3</summary>

```python
def get_word_count(self):
    return len(self.text.split())
```

</details>

---

## Task 4: Use a List of `DataReading` Objects (Optional)

Replace a list of strings with a list of `DataReading` objects and loop over them.

**Your task:**

- Build a list of several `DataReading` objects (each with text and source)
- Loop over the list and, for each object, print its text (or `str` representation) and its word count using `.get_word_count()`

**Hints:**

- Each list element is a `DataReading` instance; call methods on it
- You can use the same reading strings and sources as in earlier labs

<details>
<summary>Possible Solution for Task 4</summary>

```python
readings = [
    DataReading("Temperature spike detected in Sector 7 cooling system", "Detector A"),
    DataReading("Pressure nominal in Detector A", "Detector A"),
]
for r in readings:
    print(r, "->", r.get_word_count(), "words")
```

</details>

---

**You're done when** the `DataReading` class has `__init__`, `__str__`, and `get_word_count`, and you can create and print objects (and optionally run analysis on a list of them).

---

## Key Concepts Demonstrated

- **Class**: Blueprint for objects with attributes and methods
- **`__init__`**: Constructor that runs when you create an instance
- **`self`**: Refers to the instance; used to store and access attributes
- **`__str__`**: Special method used by `print()` for a readable string
- **Methods**: Functions defined on the class that take `self` and use instance data

---

## Next Steps

In the next lab, you’ll move the `DataReading` class into its own module and import it from a main script.
