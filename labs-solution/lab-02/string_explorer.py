# Lab 2 Steps 3 & 4: String input, concatenation, and type conversion

# Step 3: Input two strings and concatenate
first_string = input("Please enter a string: ")
second_string = input("Please enter another string: ")
combined_value = first_string + second_string

print("The new value is", combined_value)
print(f"The type of the value is {type(combined_value)}")

# Step 4: Concatenate a number and a string (must convert number to string)
# Wrong: title = 'Lab Data Logger Version ' + 1.0   # TypeError!
title = "Lab Data Logger Version " + str(1.0)
print(f"The title of this app is {title}")
