result = ["Detector A", "2026-03-03", 123, 123, 414]
#          detector_name  date_of_result  energy, location, ... 

# key -> value
# detector_name -> "Detector A"

# () [] {}

empty_dictionary = {}
print(empty_dictionary)
print(type(empty_dictionary))

result_dict = {
  "detector_name": "Detector A", 
  "date_of_result": "2026-03-03",
  "results": [123, 123, 414]
}

print(result_dict["detector_name"])
print(result_dict.get("detector_name", "Unknown key")) # safe way to read data from my dictionary

result_dict["location"] = "Merin"
result_dict["detector_name"] = "The Best Detector"

print(result_dict)

print("location" in result_dict)
print("Merin" in result_dict)  # checking the keys!

print(result_dict.keys())
print("Merin" in result_dict.values())
print(result_dict.items())

for key, value in result_dict.items():
  print(f"The key {key} has value of {value}")


result_dict.get("results", []).append(432)
print(result_dict)