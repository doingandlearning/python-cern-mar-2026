# Lab 10: Testing a Small Class with pytest

## Goal

Write a few automated tests for the `Headline` class using `pytest`.

You are **not** changing the `Headline` code — only writing tests.

---

## Step 1: Create your test file

**Your task**

- Create a new file called `test_headline.py`
- Place it next to `headline_module.py`
- Import the `Headline` class

**Check**

- Running `pytest` should find the file (even if there are no tests yet)

---

## Step 2: Test object creation

**Your task**

- Write a test that:
  - creates a `Headline`
  - checks that the text is stored correctly
  - checks that the source is stored correctly

**Hints**

- Test function names must start with `test_`
- Use `assert`
- Use very simple text (e.g. two words)

**Check**

- The test fails if you change the expected value
- The test passes when values are correct

---

## Step 3: Test `get_word_count`

**Your task**

- Write a test for `get_word_count`
- Choose text where the word count is obvious
- Assert that the returned value is correct

**Hints**

- Don’t overthink punctuation yet
- One clear test case is enough

**Check**

- If you change the text, the expected count should change too

---

## Step 4: Add one edge case

Pick **one** edge case and write a test for it.

Examples (choose one):

- empty string
- single word
- multiple spaces between words

**Your task**

- Decide what _should_ happen
- Write a test that locks that behaviour in

**Check**

- Your test documents a decision about behaviour

---

## Step 5: Reduce duplication (choose one)

Pick **one** way to tidy your tests.

### Option A: Helper function

- Create a small helper that returns a `Headline`
- Use it in at least two tests

### Option B: Parametrised test

- Use `@pytest.mark.parametrize`
- Test multiple word-count cases with one test function

### Option C: Leave it alone

- If your tests are already clear and short, stop here

---

## Running your tests

Run tests with:

```bash
pytest
```

Optional:

```bash
pytest -v
```

---

## What matters

- Tests are just Python functions
- `assert` is the key idea
- One test = one behaviour
- Tests describe how your code _should_ behave
