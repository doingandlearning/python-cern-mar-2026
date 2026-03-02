# Lab 4: Analyzing Experimental Data

The aim of this lab is to get comfortable working with lists, one of the most common data structures in Python. We'll use a list of measurement or log descriptions (e.g. sensor readings, experiment notes) to perform some simple, real-world text analysis—the kind of task you might do when summarising lab data.

This lab is made up of 4 steps:
1. Start with a list of readings
2. Count the readings
3. Calculate the average reading length
4. Search for readings by keyword or topic

---

## Step 1: Create a New File

**Your Task:** Set up your workspace for the data analysis lab.

**What to do:**
1. Create a new Python file called `data_analysis.py`
2. Think about what you'll need to import (hint: you probably don't need any special imports for this lab)

**Expected outcome:**
- You should have an empty Python file ready to work with
- The file should be named appropriately for this lab

---

## Step 2: Start with a list of readings

**Your Task:** Create a list of measurement or log descriptions to work with.

**What to do:**
1. Create a variable called `readings`
2. Add at least 8-10 short descriptions to your list (e.g. sensor alerts, experiment notes, detector status messages)
3. Make sure each item is a string (enclosed in quotes)
4. Use a variety of topics (temperature, pressure, detector status, calibration, etc.)

**Hints:**
- Remember that lists use square brackets `[]`
- Each reading should be a separate string
- You can use realistic lab-style messages or make them up
- Include a variety of topics to make your analysis interesting

**Expected outcome:**
- You should have a list with multiple readings
- Each reading should be a short, descriptive string
- The list should contain different types of data or sources

**Check your work:**
- Does your list have the right number of readings?
- Are all the readings properly formatted as strings?
- Do you have a good variety of topics?

<details>
<summary>Possible list</summary>

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

## Step 3: Count the Readings and Average Length

**Your Task:** Analyze basic statistics about your readings.

**What to do:**
1. Count how many readings you have in your list
2. Calculate the average number of words per reading
3. Display both results in a user-friendly format

**Hints:**
- Think about what function tells you how many items are in a list
- To count words, you'll need to loop through each reading
- The `.split()` method can help you break a string into words
- Remember to initialize a counter variable before your loop

**Expected outcome:**
- Your program should tell you how many readings there are
- It should calculate and display the average word count
- The output should be clear and readable

**Check your work:**
- Does the reading count match what you expect?
- Is the average word count reasonable?
- Are your results displayed clearly?

---

## Step 4: Search for readings by keyword

**Your Task:** Create a search so users can find readings that mention a specific keyword or topic.

**What to do:**
1. Ask the user what keyword they want to search for
2. Look through all readings to find matches
3. Count how many readings mention that keyword
4. Display the matching readings and the final count

**Hints:**
- Use the `input()` function to get the search term from the user
- You'll need another loop to check each reading
- Think about how to check if one string contains another
- Consider making your search case-insensitive for better results
- Keep track of how many matches you find

**Expected outcome:**
- Users should be able to search for any keyword (e.g. "temperature", "detector", "calibration")
- The program should find and display matching readings
- It should show the total count of matches
- The search should work regardless of capitalization

**Check your work:**
- Try searching for different keywords (some common, some rare)
- Does the search find the right readings?
- Does it handle capitalization correctly?
- Are the results displayed clearly?

---

## Putting It All Together

**Final Challenge:** Make sure all parts work together smoothly.

**What to do:**
1. Test your complete program with different search terms
2. Make sure all the statistics are calculated correctly
3. Verify that the output is clear and professional
4. Consider adding some formatting to make results easier to read

**Hints:**
- Test with keywords you know are in your readings
- Test with keywords that aren't in your readings
- Make sure your average calculation is mathematically correct
- Consider adding some visual separation between different sections

---

## Checks for Understanding

Before moving to the next lab, make sure you can answer these questions:

### Basic Concepts:
- [ ] Can you explain how lists work in Python?
- [ ] Do you understand how to loop through a list?
- [ ] Can you explain what the `.split()` method does?
- [ ] Do you know how to check if one string contains another?

### Practical Skills:
- [ ] Can you create and populate a list with data?
- [ ] Can you calculate statistics from list data?
- [ ] Can you search through a list for specific content?
- [ ] Can you handle user input and provide meaningful output?

### If you answered "No" to any questions:
- Review the relevant sections above
- Check the solutions folder for complete code examples
- Ask for help if needed

---

## Common Issues and Solutions

### Problem: "NameError: name 'readings' is not defined"
**Solution:** Make sure you've created your readings list before trying to use it.

### Problem: Average calculation gives 0 or wrong results
**Solution:** Check that you're initializing your counter variable to 0 before the loop.

### Problem: Search doesn't find obvious matches
**Solution:** Make sure you're using `.lower()` on both the reading and search term.

### Problem: Program crashes when searching
**Solution:** Make sure you're properly handling the case where no matches are found.

---

## What's Next?

In the next lab, you'll learn about:
- More advanced list operations
- Working with other container types (tuples, sets)
- List comprehensions and advanced data processing

**Ready to continue?** Move on to Lab 5: Advanced Container Operations!

---

## Solutions

**Complete code examples for all exercises are available in the `solutions/` folder.**

- `solutions/data_analysis.py` - Complete data analysis solution
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