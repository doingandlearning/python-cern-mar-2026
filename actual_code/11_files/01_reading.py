file = open("test.txt")

contents = file.read() # loads the whole file as a str
print(contents)
print(type(contents))
print(contents.find("Cup"))

file.seek(0)
contents = file.readlines() # loads the whole file, returns a list split by lines
print([line.strip() for line in contents])
print(type(contents))

for line in contents:
  if line.find("Cup") >= 0:
    print(line)

file.seek(0)
line = file.readline()

while line:
  if line.find("Cup") >= 0:
    print(line.strip())
  line = file.readline()



file.close()