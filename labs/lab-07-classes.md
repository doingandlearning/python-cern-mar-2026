# Lab 7: Structuring Data with Classes

### **Objective**

So far, we've been working with readings (measurement or log descriptions) as simple strings. This is fine, but as our data gets more complex, it's better to structure it. **Classes** are the perfect tool for this.

The aim of this lab is to create a `DataReading` class to hold not just the text of a reading, but also its source (e.g. detector name, sensor ID, or experiment). We will then add behavior to this class.

---

## Starter code 

This covers step 1 and hopefully will give you a head start!

<details>
  <summary>Starter code</summary>
  
```python
class DataReading:
    def __init__(self, text, source):
        self.text = text
        self.source = source

r = DataReading(
    "Temperature spike detected in Sector 7 cooling system",
    "Detector A"
)
```

</details>

---

## **Step 1: Defining the `DataReading` Class**

### **Tasks**

1. Create a new Python file, e.g., `reading_objects.py`
2. Define a class named `DataReading`
3. Create a constructor (`__init__` method) that accepts two arguments
4. Store the arguments as attributes of the object

### **Hints**

- Start with `class DataReading:`
- Define the constructor: `def __init__(self, text, source):`
- Inside the constructor, store the arguments as attributes
- The standard way is `self.text = text` and `self.source = source`
- Remember that `self` refers to the object being created

### **Expected Outcomes**

- You should have a working `DataReading` class
- The class should accept `text` and `source` parameters (e.g. reading description and detector/source name)
- Objects should store both pieces of information
- You should be able to create `DataReading` objects

### **Check Your Work**

- Can you create a `DataReading` object with `DataReading("Some text", "Some source")`?
- Does the object store both the text and source?
- Can you access the attributes with `object.text` and `object.source`?

---

## **Step 2: Adding a String Representation**

### **Tasks**

1. Add a `__str__` method to your `DataReading` class
2. Make the method return a clear, readable string representation
3. Test that printing the object shows useful information

### **Hints**

- Define a new method inside the class: `def __str__(self):`
- This method must `return` a string
- A good representation shows the class name and its attributes
- Consider using an f-string to format the output clearly
- Think about what information would be most helpful when debugging

<details>
  <summary>Possible solution</summary>

```python
## Add this inside your class
def __str__(self):
    return f"{self.text} ({self.source})"

# Now it should print well
print(r)

```

</details>

### **Expected Outcomes**

- Printing a `DataReading` object should show readable information
- The output should include both the text and source
- The representation should be clear and unambiguous
- You should no longer see `<__main__.DataReading object at 0x...>`

### **Check Your Work**

- Does `print(your_reading_object)` show readable text?
- Can you see both the reading text and source in the output?
- Is the output format clear and helpful?
- Try printing multiple objects to see the difference

---

## **Step 3: Adding Behavior with a Method**

### **Tasks**

1. Create a method `get_word_count()` inside the `DataReading` class
2. Make the method return the number of words in the reading's text
3. Test that the method works correctly

### **Hints**

- Define a new method: `def get_word_count(self):`
- The logic is the same as our old standalone function
- Now it uses the object's own data: `self.text`
- The method should `return len(self.text.split())`
- Think about how this method relates to the object's data

<details>
  <summary>Possible solution</summary>

```python
## Add this inside your class
def get_word_count(self):
    return len(self.text.split())

# The rule lives with the data
print(r.get_word_count())

```

</details>

### **Expected Outcomes**

- The method should return the correct word count
- It should work with any `DataReading` object
- The method should be easy to call on any object
- Results should match manual word counting

### **Check Your Work**

- Does `your_reading.get_word_count()` return the right number?
- Does it work with different readings (short and long)?
- Can you verify the word count manually?
- Does the method use the object's own text data?

---

## **Step 4: Refactoring Your Code to Use the Class** (Optional/Extension/After the course)

### **Tasks**

1. Create a list of `DataReading` objects instead of strings
2. Loop through the list and use object methods
3. Print each reading's text and word count
4. Notice how much cleaner the object-oriented approach is

### **Hints**

- Replace your old list of strings with `DataReading` objects
- Each object should have text and source information (e.g. detector or sensor name)
- Use a loop to process all readings
- Call methods directly on objects: `r.get_word_count()`
- Think about how this compares to the functional approach

### **Expected Outcomes**

- You should have a list of `DataReading` objects
- Each object should have both text and source
- The loop should work with object methods
- Output should show both reading text and word counts
- Code should be cleaner and more organized

### **Check Your Work**

- Do you have a list of `DataReading` objects?
- Does each object have text and source attributes?
- Does the loop work correctly with all objects?
- Is the output clear and informative?
- Does the code feel more organized?

---

## **Common Issues to Watch Out For**

### **Class Definition**

- **Missing colon**: Don't forget `:` after `class DataReading`
- **Wrong method names**: `__init__` and `__str__` are special names
- **Indentation**: Methods must be indented inside the class
- **Self parameter**: Don't forget `self` as the first parameter

### **Constructor Issues**

- **Missing attributes**: Make sure you store the parameters
- **Wrong attribute names**: Use `self.text` and `self.source`
- **Parameter order**: Check that you're passing arguments in the right order
- **Object creation**: Test creating objects with different values

### **Method Problems**

- **Missing return**: `__str__` must return a string
- **Wrong data access**: Use `self.text` to access the object's text
- **Method calls**: Remember to call methods on objects, not the class
- **Attribute access**: Use `object.attribute` to access data

---

## **Testing Your Solutions**

### **Test Data**

Create test readings with different sources:

- "Temperature spike detected in Sector 7 cooling system" from "Detector A"
- "Pressure nominal in Detector A" from "Detector A"
- "Calibration run completed for beam line B2" from "Beam Line B2"

### **Test Scenarios**

1. **Object Creation**: Test creating `DataReading` objects
2. **Attribute Access**: Verify text and source are stored correctly
3. **String Representation**: Check that printing shows useful information
4. **Method Functionality**: Test `get_word_count()` with different readings
5. **List Processing**: Verify the loop works with multiple objects

### **Expected Results**

- Objects should store both text and source
- `print(reading)` should show clear information
- `reading.get_word_count()` should return correct numbers
- Loop should process all objects correctly

---

## **Extension Ideas (Optional)**

### **Additional Methods**

- **`get_character_count()`**: Return the total character count
- **`get_source()`**: Return just the source information
- **`is_long_reading()`**: Return True if word count > 8
- **`contains_keyword(keyword)`**: Check if reading contains a specific word

### **Enhanced Functionality**

- **Multiple sources**: Add more detectors or sensors to your list
- **Data validation**: Check that text is not empty
- **Source categories**: Group readings by detector or experiment
- **Statistics**: Calculate average word count by source

### **Advanced Features**

- **Timestamp attributes**: Add measurement time to readings
- **Category classification**: Add tags (e.g. temperature, pressure)
- **Comparison methods**: Compare readings by length or content
- **Export functionality**: Save readings to a file

---

## **Solutions**

**Complete code examples for all exercises are available in the `solutions/lab-07` folder.**

- `solutions/reading_objects.py` - Complete solution with all class features

---

## **Why Classes?**

Classes are powerful because they:

- **Organize code** - Group related data and functions together
- **Reduce duplication** - Create reusable templates for objects
- **Improve readability** - Code is more self-documenting
- **Enable inheritance** - Build new classes from existing ones
- **Follow OOP principles** - Encapsulation, inheritance, polymorphism

---

## **Real-World Applications**

Classes are used everywhere in Python:

- **Data structures**: Lists, dictionaries, sets are all classes
- **File handling**: File objects are class instances
- **Web frameworks**: Django, Flask use classes extensively
- **Data science**: Pandas DataFrames are class instances
- **GUI programming**: Tkinter widgets are class objects

---

**Remember**:

- Start with simple classes and build complexity gradually
- Always test object creation and method calls
- Use meaningful attribute and method names
- Think about what data and behavior belong together
- Classes are the foundation of object-oriented programming

This lab introduces you to one of Python's most important concepts for organizing and structuring code!

Some people hate it - that's okay!
