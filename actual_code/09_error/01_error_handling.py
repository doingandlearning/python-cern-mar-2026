# Error and Exception used interchangably 

# 1. What went wrong
  # error type: error message
  # ValueError: invalid literal for int() with base 10: 'this is not a number'

# 2. Where it went wrong
  # Traceback - traceback.format_exc()

# 3. If it was expected, what should we do?
  # - Ask the user to give me a different value
  # - Report that this value is invalid and keep going 
  # - Stop!
  # - Give the user a readable message, save/store/log the actual error

# 4. If it wasn't expected, what should we do?  # except Exception:
  # - Stop!
  # - Report the issue and then keep going

# We want to declare an error which isn't a Python predefined error


user_age = int(input("What is your age? "))

