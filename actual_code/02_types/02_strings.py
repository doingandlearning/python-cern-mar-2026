first_name = "Kevin"
last_name = "Cunningham"

# concatenate -> join together!
full_name = first_name + " " + last_name  # remembering spaces!
print(full_name)

print("1 + 1 =" + str(2))  # converting types

# f-string -> formatted string
print(f"{first_name} {last_name}")
print(f'1 + 1 = {1 + 1}')
print(f"""First line
last line""")
print(f'''''')

print(full_name.lower())
print(full_name.upper())
print(full_name.center(50))
print(full_name.ljust(50))
print(full_name.rjust(50))

print(full_name.find("not in there"))

#0123456789
"Kevin Cunningham"