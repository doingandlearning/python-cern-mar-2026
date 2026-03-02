# Lab 2: Types - Complete combined solution
# Demonstrates all concepts from the lab (interactive, numbers, strings, conversion, None)

print("=" * 50)
print("Welcome to the Lab Data Logger / Types Demo!")
print("=" * 50)

# Step 1: Interactive greeting
print("\n--- Step 1: Interactive Greeting ---")
user_name = input("Please enter your name: ")
print("Welcome,", user_name, "!")

# Step 2: Number calculations
print("\n--- Step 2: Number Calculations ---")
first_num = float(input("Please enter a number: "))
second_num = float(input("Please enter another number: "))
sum_result = first_num + second_num

print(f"The result of {first_num} + {second_num} is {sum_result}")
print(f"The type of the value is {type(sum_result)}")

# Step 3: String operations
print("\n--- Step 3: String Operations ---")
first_string = input("Please enter a string: ")
second_string = input("Please enter another string: ")
combined_string = first_string + " " + second_string

print("The new value is", combined_string)
print(f"The type of the value is {type(combined_string)}")

# Step 4: Type conversion (number to string)
print("\n--- Step 4: Type Conversion ---")
version_number = 1.0
app_title = "Lab Data Logger Version " + str(version_number)
print(f"The title of this app is {app_title}")

# Step 5: None value
print("\n--- Step 5: Using None ---")
user_preference = None
print("user_preference:", user_preference)
print("user_preference is None:", user_preference is None)
print("The type of user_preference:", type(user_preference))

# Summary
print("\n" + "=" * 50)
print("Summary: User:", user_name, "| App:", app_title)
print("=" * 50)
