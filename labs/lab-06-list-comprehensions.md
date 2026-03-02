# Lab 6: Supercharging Analysis with List Comprehensions

### **Objective**
The aim of this lab is to use **list comprehensions** to perform powerful data manipulation on your list of readings (measurement or log descriptions) in a single, readable line of code. This is a very common and powerful technique in Python, especially when processing experimental or sensor data.

---

## **What are List Comprehensions?**
A **list comprehension** is a concise way to create lists by applying operations to existing data. Think of it as a "for loop in one line" that's both readable and efficient.

### **Key Concepts**
- **Mapping**: Transform each item in a list
- **Filtering**: Select only items that meet certain criteria
- **Combining**: Map and filter in a single expression
- **Readability**: Write complex operations in clear, single lines

---

## **Step 1: Getting Started**

### **Tasks**
1. Create a new Python file, e.g., `comprehensions_analysis.py`
2. Set up your workspace with the readings data (same list as in Lab 4 or 5)
3. Verify that your data is loaded correctly

### **Expected Outcomes**
- You should have a working Python file
- The readings list should be loaded and accessible
- You should be able to print the readings to verify they're loaded

### **Check Your Work**
- Can you print the readings list?
- Does it contain all 10 readings?
- Is your file ready for the next steps?

---

## **Step 2: Mapping with List Comprehensions**

A list comprehension is a great way to create a new list by applying an operation to every item in an existing list.

### **Tasks**
1. Create a new list called `reading_lengths` that contains the word count for each reading
2. Use a list comprehension to transform the data
3. Print the result to verify your work

### **Hints**
- The basic syntax is `[expression for item in list]`
- Your `expression` will involve calling `.split()` and `len()` on each `item`
- The `item` in your case is each `reading` in the `readings` list
- Think about what operation you want to apply to each reading
- Consider how to count words in a string

### **Expected Outcomes**
- `reading_lengths` should be a list of numbers
- Each number should represent the word count of the corresponding reading
- The list should have the same length as your readings list

### **Check Your Work**
- Does your list have 10 numbers?
- Can you verify a few word counts manually (e.g. first reading "Temperature spike detected in Sector 7 cooling system" has 8 words)?
- Are the numbers in the same order as your readings?

---

## **Step 3: Filtering with List Comprehensions**

Now, let's use a list comprehension to select only the items that meet a certain criteria.

### **Tasks**
1. Create a new list called `short_readings` that contains only the readings with 7 words or fewer
2. Use a list comprehension with a condition to filter the data
3. Print the result to verify your work

### **Hints**
- The syntax for filtering is `[item for item in list if condition]`
- Your `condition` will check the word count of each `reading`
- Remember to use `.split()` and `len()` as part of your `if condition`
- Think about what makes a reading "short" (7 words or fewer)
- Consider how to combine the word counting with the filtering condition

### **Expected Outcomes**
- `short_readings` should be a list of strings (the actual readings)
- Only readings with 7 words or fewer should be included
- The list should be shorter than your original readings list

### **Check Your Work**
- Is your filtered list shorter than the original?
- Do all readings in the result have 7 words or fewer?
- Can you manually count words to verify the filtering worked?
- Are you getting the expected readings?

---

## **Step 4: Combining Mapping and Filtering**

This is where list comprehensions really shine. You can filter a list and transform the results in a single, elegant line.

### **Tasks**
1. Create a list called `specific_reading_lengths` that contains the word counts of only those readings that include the word "detector" (or "new", if you prefer)
2. Combine filtering and mapping in a single list comprehension
3. Print the result to verify your work

### **Hints**
- You'll use the combined syntax: `[expression for item in list if condition]`
- Your `expression` will get the word count of the `item` (the reading)
- Your `if condition` will check if the keyword (e.g. "detector") is in the `item`
- Remember to use `.lower()` to make your check case-insensitive
- Think about the order: filter first, then map the results

### **Expected Outcomes**
- `specific_reading_lengths` should be a list of numbers (word counts)
- Only readings containing your chosen keyword should contribute to this list
- The list should be shorter than your original readings list

### **Check Your Work**
- Is your result list shorter than the original?
- Do all the word counts correspond to readings that contain the keyword?
- Can you manually verify which readings match?
- Are you getting the expected word counts?

---

## **Common Issues to Watch Out For**

### **Syntax Errors**
- **Missing brackets**: List comprehensions must be enclosed in `[]`
- **Wrong order**: Remember it's `[expression for item in list if condition]`
- **Missing colons**: Don't forget the `:` after `for` and `if`
- **Indentation**: List comprehensions should be on one line or properly indented

### **Logic Errors**
- **Case sensitivity**: Remember to use `.lower()` for case-insensitive searches
- **Word counting**: Make sure you're splitting on whitespace correctly
- **Filtering conditions**: Double-check your comparison operators
- **Empty results**: If you get an empty list, check your filtering condition

### **Performance Considerations**
- **Large lists**: List comprehensions are efficient but can use memory
- **Complex expressions**: Keep expressions readable and simple
- **Nested comprehensions**: Avoid going too deep for readability

---

## **Testing Your Solutions**

### **Test Data Verification**
Use the same readings list as in Lab 4 or 5 (e.g. "Temperature spike detected in Sector 7 cooling system", "Pressure nominal in Detector A", etc.). Verify word counts for a few entries to ensure your comprehensions are correct.

### **Expected Results**
- **Step 2**: You should get a list of 10 numbers (word counts per reading).
- **Step 3**: Only readings with 7 words or fewer should appear in `short_readings`.
- **Step 4**: Only readings containing your keyword (e.g. "detector" or "new") should contribute word counts to `specific_reading_lengths`.

---

## **Extension Ideas (Optional)**

### **More Complex Comprehensions**
- Find readings that start with specific words (e.g. "Temperature", "Data")
- Create a list of reading lengths for readings containing multiple keywords
- Filter by word count ranges (e.g., 5-8 words)

### **Advanced Filtering**
- Find readings that contain numbers
- Select readings that mention specific detectors or sectors
- Filter by multiple conditions (e.g., contains "detector" AND has ≤8 words)

### **Data Analysis**
- Calculate the average word count of filtered readings
- Find the longest and shortest readings
- Create a frequency count of reading lengths

---

## **Solutions**

**Complete code examples for all exercises are available in the `solutions/lab-06` folder.**

- `solutions/comprehensions_analysis.py` - Complete solution with all steps

---

## **Why List Comprehensions?**

List comprehensions are powerful because they:
- **Improve readability** - Complex operations in single lines
- **Boost performance** - Often faster than equivalent loops
- **Reduce code** - Less verbose than traditional for loops
- **Express intent** - Clear what you're trying to accomplish
- **Follow Python style** - Considered "Pythonic" code

---

**Remember**: 
- Start with simple comprehensions and build complexity
- Always test with small examples first
- Keep expressions readable and simple
- Practice combining mapping and filtering
- List comprehensions are a fundamental Python skill

This lab introduces you to one of Python's most powerful and commonly used features! 