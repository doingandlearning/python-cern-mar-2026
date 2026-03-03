empty_tuple = tuple() # or ()
print(empty_tuple)
print(type(empty_tuple))
#         -4        -3         -2         -1
#          0         1         2          3
names = ("Dani", "Hjalmar", "Viren", "Korbinian")
names = (*names, "Zoe")

print(len(names))
print(names[1])  # access by index or position
print(names[1:3])  
print(names[1:])
print(names[:2])  # slicing the tuple - sub-slice
print(names[-1])

print("Hello my name is Kevin"[0:15:3])

print("Dani" in names)
print("Kevin" in names)

user = "Bob"

if user in names:
  print("Authorized")
else:
  print("Unauthorized")

for person in names:
  print(person)


print(names.count("Korbinian"))
print(names.count("Kevin"))

print(names.index("Hjalmar"))

if "Bob" in names:
  print(names.index("Bob"))  # check for membership before using .index()


print(names[::-1])

# unpacking - destructuring

particle_location = (12, 45, 10)
x = particle_location[0]
y = particle_location[1]
z = particle_location[2]

print(x, y, z)

x, y, z  = particle_location  # do *you* find it more readable or less?

