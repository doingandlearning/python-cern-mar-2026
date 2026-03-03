empty_list = []  # list()
print(empty_list)
print(type(empty_list))

beatles = ["John", "Paul", "Ringo", "George"]
print(len(beatles))

print("John" in beatles)
print("Kevin" in beatles)

for band_member in beatles:
  print(band_member)

print(beatles[1][-1])

# Create  Update Delete
beatles.append("Zoe")  # to add one new element
print(beatles)

beatles.extend(["Alexey", "Korbinian"])  # to add multiple items
print(beatles)

beatles.insert(1, "Dani")
print(beatles)

# Read
print(beatles[2])

print(beatles)
last_element = beatles.pop()
print(beatles)
print(last_element)

first_element = beatles.pop(0)  # First in, first out
print(beatles)

# Update

beatles[4] = "Zoé"
print(beatles)

# Delete
del beatles[1:3]
print(beatles)


new_beatles = beatles.copy()
new_beatles.append("Viren")
print(new_beatles)
print(beatles)

print(beatles.count("Viren"))

if "Viren" in beatles:
  print(beatles.index("Viren"))

beatles.reverse()
print(beatles)

beatles.sort()  # data types need to be comparable
print(beatles)