user_input = input("Enter your password: ")
password = "password123"
attempts_tried = 1

while user_input != password and attempts_tried < 3:   # uncounted loop
  # print("Python is great!")  # infinite loop!
  print("Invalid password.")
  user_input = input("Enter your password: ")
  # attempts_tried = attempts_tried + 1
  attempts_tried += 1

if attempts_tried < 3:
  print("Here are you secret documents.")