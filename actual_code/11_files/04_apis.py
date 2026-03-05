# Request    ->  Server   ->  Response

# + url                       + status code (404, 401)
# + method (GET, POST)        ? status text
# ? headers                   ? headers
# ? query parameters          ? body
# ? body

import requests
import json
import csv

response = requests.get("https://swapi.dev/api/planets")
data = response.json()

with open("planets.json", mode="w") as file:
  file.write(json.dumps(data, indent=2))

with open("planets.csv", mode="w") as file:
  writer = csv.DictWriter(file, fieldnames=["name", "rotation_period", "diameter", "population" ], extrasaction="ignore")
  writer.writeheader()

  for planet in data["results"]:
    writer.writerow(planet)