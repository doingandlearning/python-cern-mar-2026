# Lab 2: Types

## Objective
In this lab, you'll extend the hello world application to make it interactive and to handle different types of data. You'll use `input()`, type conversion, and variables - similar to how lab tools or data loggers collect and display information.

You will:
1. Capture user input using `input()`
2. Store data in variables
3. Convert between data types (`int()`, `float()`, `str()`)
4. Use string concatenation and display results
5. Work with the `None` value and type checks

---

## Scenario: Interactive Data Entry

You're building simple interactive programs that collect user input and display results. These might be the first steps toward a lab data logger or script that asks for parameters. The system needs to handle names, numbers, strings, and optional values - and to convert types correctly so that maths and formatting work.

---

## Task 1: Make the Application Interactive

Create a file `interactive_hello.py`:

**Your task:**

- Print a welcome message (e.g. "Hello World!")
- Ask the user for their name using `input()`
- Store the user's input in a variable
- Greet the user personally using their name

**Hints:**

- `input()` always returns a string
- Use a variable to store the result of `input("Please enter your name: ")`
- You can combine strings with `+` or pass multiple arguments to `print()`

<details>
<summary>Possible Solution for Task 1</summary>

```python
print("Hello World!")
name = input("Please enter your name: ")
print("Welcome", name)
```

</details>

---

## Task 2: Input Some Numbers

Create a file `number_calculator.py`:

**Your task:**

- Ask the user for two numbers using `input()`
- Convert the input strings to numbers using `int()` or `float()`
- Add the two numbers together
- Display the result and show the type of the result variable

**Hints:**

- `input()` returns a string even when the user types digits; you must convert before doing maths
- Use `int(input('prompt'))` or `float(input('prompt'))` to get and convert in one step
- Use `type(result)` to show the type

<details>
<summary>Possible Solution for Task 2</summary>

```python
first = int(input("Please enter a number: "))
second = int(input("Please enter another number: "))
result = first + second
print(f"The result of {first} + {second} is {result}")
print(f"The type of the value is {type(result)}")
```

</details>

---

## Task 3: Input Two Strings and Concatenate

Create a file `string_explorer.py` (or add to an existing file):

**Your task:**

- Ask the user to input two strings (e.g. two words or names)
- Use the `+` operator to concatenate the strings
- Display the combined result and its type

**Hints:**

- Think about spacing when concatenating (e.g. `first + " " + second`)
- The result is still a string; use `type()` to confirm

<details>
<summary>Possible Solution for Task 3</summary>

```python
first_string = input("Please enter a string: ")
second_string = input("Please enter another string: ")
combined_value = first_string + second_string
print("The new value is", combined_value)
print(f"The type of the value is {type(combined_value)}")
```

</details>

---

## Task 4: Concatenate a Number and a String

In `string_explorer.py`, add code that combines a string with a number:

**Your task:**

- Create a version number (e.g. `1.0`) as a number
- Try concatenating a string with that number directly - observe the error
- Use `str()` to convert the number to a string, then concatenate
- Print the result (e.g. "The title of this app is Lab Data Logger Version 1.0")

**Hints:**

- Python cannot concatenate strings and numbers with `+`; one type must be converted
- `str(1.0)` produces the string `"1.0"`

<details>
<summary>Possible Solution for Task 4</summary>

```python
# Wrong: title = 'Lab Data Logger Version ' + 1.0   # TypeError!
title = "Lab Data Logger Version " + str(1.0)
print(f"The title of this app is {title}")
```

</details>

---

## Task 5: Using `None`

Create a file `none_explorer.py`:

**Your task:**

- Create a variable that holds the value `None`
- Print the variable
- Test whether it is `None` using `is None` and `is not None`
- Print the type of the variable

**Hints:**

- Use `is` and `is not` to compare with `None` (not `==`)
- The type of `None` is `NoneType`

<details>
<summary>Possible Solution for Task 5</summary>

```python
user = None
print("user:", user)
print("user is None:", user is None)
print("user is not None:", user is not None)
print("The type of the user:", type(user))
```

</details>

---

## Task 6: Put It All Together (Optional)

Create a file `types_demo.py` that combines the concepts above:

**Your task:**

- Greet the user and get their name
- Ask for two numbers and display their sum and the type
- Get two strings and show the concatenated result
- Build a string like "Lab Data Logger Version " + str(version) and print it
- Demonstrate a variable set to `None` and print its type

**Hints:**

- Reuse patterns from Tasks 1–5
- Use separators (e.g. `print("=" * 50)`) to make output readable

<details>
<summary>Possible Solution for Task 6</summary>

```python
print("=" * 50)
print("Welcome to the Lab Data Logger / Types Demo!")
print("=" * 50)

user_name = input("Please enter your name: ")
print("Welcome,", user_name, "!")

first_num = float(input("Please enter a number: "))
second_num = float(input("Please enter another number: "))
print(f"The result of {first_num} + {second_num} is {first_num + second_num}")
print(f"The type of the value is {type(first_num + second_num)}")

first_string = input("Please enter a string: ")
second_string = input("Please enter another string: ")
print("The new value is", first_string + " " + second_string)

version_number = 1.0
app_title = "Lab Data Logger Version " + str(version_number)
print(f"The title of this app is {app_title}")

user_preference = None
print("user_preference:", user_preference)
print("user_preference is None:", user_preference is None)
print("The type of user_preference:", type(user_preference))
```

</details>

---

## Example Interaction

```
Hello World!
Please enter your name: Alex
Welcome Alex

Please enter a number: 2
Please enter another number: 3
The result of 2 + 3 is 5
The type of the value is <class 'int'>
```

---

**You're done when** your program prompts for two numbers and prints their sum and the type of the result.

---

## Key Concepts Demonstrated

- **`input()`**: Get user input (always returns a string)
- **Type conversion**: `int()`, `float()`, `str()` to convert between types
- **Variables**: Storing and reusing values
- **`type()`**: Inspecting the type of a value
- **`None`**: Representing "no value"; compare with `is None` / `is not None`
- **String concatenation**: Using `+` (both operands must be strings when using `+`)

---

## Common Issues

- **TypeError: can only concatenate str (not "int") to str** — Convert the number with `str(...)` before concatenating.
- **ValueError: invalid literal for int()** — The user entered something that isn’t a valid number; we don’t handle that yet.

---

## Next Steps

In the next lab, you’ll use control flow (`if`, `for`, `while`, `break`) to build a calibration value guessing game.
