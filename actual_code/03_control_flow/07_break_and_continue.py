user_input = int(input("What number do you want to look for? "))

for count in range(100):
  if user_input == count:
    print("Found it!")
    # break  # break early! exit the loop altogether.
    continue  #exits this cycle but picks up again at the next value.
  else:
    print(f"It wasn't {count}, still looking")