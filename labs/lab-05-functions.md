# Lab 5: Building a Data Analysis Toolkit with Functions

The aim of this lab is to practice writing functions to create a reusable, organized toolkit. We will refactor our previous data analysis script into a set of functions that can be easily called and tested.

This lab is made up of 4 steps:
1. Set up your script with the readings data.
2. Write a function to get the word count of a single reading.
3. Write a function to search for readings containing a keyword.
4. Write a main `analyse_all_readings` function that uses the other functions.

---

## Step 1: Getting Started

**Your Task:** Set up your workspace and prepare the readings data.

**What to do:**
1. Create a new Python file called `data_analyzer.py`
2. Copy the readings list below into your file
3. Make sure the file runs without errors

**Readings data (copy this into your file):**
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

**Expected outcome:**
- You should have a Python file with the readings list
- The file should run without errors
- You're ready to start writing functions

**Check your work:**
- Does your file contain the readings list?
- Can you run the file without errors?
- Are you ready to add functions?

---

## Step 2: A Function to Get Word Count

**Your Task:** Create a function that counts words in a single reading (e.g. a log line or measurement description).

**What to do:**
1. Write a function called `get_word_count(reading_text)`
2. The function should take a single reading string as an argument
3. It should return the number of words in that reading

**Hints:**
- Start with `def get_word_count(reading_text):`
- Use the `.split()` method to break the reading into words
- Use `len()` to count the words
- Remember to use the `return` keyword

**Expected outcome:**
- A function that can count words in any reading
- The function should work when called with different readings

**Check your work:**
- Does your function definition start with `def`?
- Does it take a parameter?
- Does it return a number?
- Can you test it with `print(get_word_count("Temperature spike in Sector 7"))`?

---

## Step 3: A Function to Find Readings with a Keyword

**Your Task:** Create a function that searches for readings containing a specific keyword.

**What to do:**
1. Write a function called `find_readings_with_keyword(list_of_readings, keyword)`
2. The function should take the full list of readings and a search term
3. It should return a new list containing only matching readings

**Hints:**
- Start with `def find_readings_with_keyword(list_of_readings, keyword):`
- Create an empty list to store matching readings
- Loop through each reading in the list
- Check if the keyword (in lowercase) is in the reading (also in lowercase)
- Add matching readings to your list
- Return the list of matches

**Expected outcome:**
- A function that can search through any list of readings
- It should return only the readings that contain the keyword
- The search should be case-insensitive

**Check your work:**
- Does your function take two parameters?
- Does it create a new list for results?
- Does it loop through the readings?
- Does it return the matching readings?

---

## Step 4: A Main Analysis Function

**Your Task:** Create a main function that orchestrates the analysis and prints results.

**What to do:**
1. Write a function called `analyse_all_readings(list_of_readings)`
2. The function should calculate and display the average reading length (words per reading)
3. Use your `get_word_count()` function from Step 2

**Hints:**
- Start with `def analyse_all_readings(list_of_readings):`
- Create a counter for total words
- Loop through each reading
- Call your `get_word_count()` function for each reading
- Calculate the average and print it

**Expected outcome:**
- A function that analyzes all readings
- It should display the average word count
- The output should be user-friendly

**Check your work:**
- Does your function call `get_word_count()`?
- Does it calculate the average correctly?
- Does it print the results clearly?

---

## Tying It All Together

**Your Task:** Call your functions to produce the final output.

**What to do:**
1. After defining all your functions, add code to call them
2. Test your `analyse_all_headlines()` function
3. Test your search function with different keywords
4. Display the results in a clear format

**Hints:**
- Call `analyse_all_readings(readings)` to see the analysis
- Test searching for different keywords like "detector", "temperature", "calibration"
- Use loops to display search results clearly
- Make your output organized and readable

**Expected outcome:**
- A complete program that demonstrates all your functions
- Clear output showing the analysis results
- Search results displayed in an organized way

**Check your work:**
- Does your program run without errors?
- Does it show the average reading length?
- Can you search for different keywords?
- Are the results displayed clearly?

---

## Checks for Understanding

Before moving to the next lab, make sure you can answer these questions:

### Basic Concepts:
- [ ] Can you explain what a function is and why we use them?
- [ ] Do you understand the difference between parameters and arguments?
- [ ] Can you explain what the `return` keyword does?
- [ ] Do you know how to call a function?

### Practical Skills:
- [ ] Can you write a function that takes parameters?
- [ ] Can you write a function that returns a value?
- [ ] Can you call functions from within other functions?
- [ ] Can you organize code into logical functions?

### If you answered "No" to any questions:
- Review the relevant sections above
- Check the solutions folder for complete code examples
- Ask for help if needed

---

## Common Issues and Solutions

### Problem: "NameError: name 'get_word_count' is not defined"
**Solution:** Make sure you've defined your function before trying to call it.

### Problem: Function doesn't return anything
**Solution:** Check that you're using the `return` keyword in your function.

### Problem: Function parameters don't work
**Solution:** Make sure your function definition matches how you're calling it.

### Problem: Search function returns empty results
**Solution:** Check that you're converting both the keyword and reading to lowercase.

---

## What's Next?

In the next lab, you'll learn about:
- More advanced function features
- Working with different data types
- Building larger, more complex programs

**Ready to continue?** Move on to Lab 6: Advanced Functions!

---

## Solutions

**Complete code examples for all exercises are available in the `solutions/lab-05` folder.**

- `solutions/data_analyzer.py` - Complete solution with all functions
- `solutions/step_by_step/` - Individual step solutions

**Try to solve the exercises yourself first, then check the solutions if you get stuck!**

---

## Questions?

If you get stuck or have questions:
1. Check the error messages carefully
2. Review the concepts in the notes
3. Look at the solutions folder for examples
4. Ask for help from your instructor or classmates
5. Remember: everyone learns at their own pace! 