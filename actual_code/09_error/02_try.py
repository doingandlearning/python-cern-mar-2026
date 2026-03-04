# users, files, network, database ... potentially error causing
import traceback, sys

def ten_divided_by_user_number(no_of_tries = 1):
  if no_of_tries > 3:
    print("This failed!")
    return False
  try:
    user_number = input("Give me a number (please only use digits): ")  # raised an erro
    while not user_number.isnumeric():
      print("That wasn't a number")
      user_number = input("Give me a number (please only use digits): ")  
    user_number = int(user_number)
    print(user_number)

    print(f"10 divided by your number is {10 / user_number}")
    return 10 / user_number
  except ValueError as err:
    # tell the user this
    print("Sorry. That wasn't a number. Please only use digits.")
    # log to the developers this
    print(traceback.format_exc())
    return ten_divided_by_user_number(no_of_tries + 1)
  except ZeroDivisionError:
    print("Whoops! You can't divide by zero.")
    print(traceback.print_exc(10))
    return ten_divided_by_user_number(no_of_tries + 1)
  except Exception as err:  # bare/naked except!
    print("Something went wrong.")
    print(f"{type(err)}: {err}")
    sys.exit(1)

result = ten_divided_by_user_number()
print(f"Result is: {result}")