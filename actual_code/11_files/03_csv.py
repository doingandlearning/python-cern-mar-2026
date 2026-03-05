import csv

with open("movies.csv") as file:
  # reader = csv.reader(file)
  reader = csv.DictReader(file)
  # next(reader) # skips a row
  for row in reader:
    if int(row["Year"]) > 2020:
      print(row)

with open("movies.csv", mode="a") as file:
  writer = csv.DictWriter(file, fieldnames=["Title", "Year", "Director", "Genre", "Revenue"])
  writer.writerow({
    "Title": "Metaphysique des tubes",
    "Director": "Liane-Cho Han Jin Kuang",
    "Year": 2025,
    "Genre": "Animated",
    "Revenue": 0.001
  })