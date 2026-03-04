result_dict = {
  "detector_name": "Detector A", 
  "date_of_result": "2026-03-03",
  "results": [123, 123, 414]
}

def get_average_of_results(target_dict):
  results = target_dict.get("results")
  return sum(results) / len(results)

result_dict_2 = {
  "dectector_name": "Detector B",
  "date_of_results": "2026-03-02",
  "result": [12,12,12]
}
# __add__ -> double underscores -> dunder add

# protocols: print -> __str__, new -> __init__

# 1. Consistent data shapes
# 2. Encapsulation

class ResultValue:
  def __init__(self, name, date):
    self.detector_name = name
    self.date_of_results = date
    self.results = []

  def __str__(self):
    return f"<ResultValue for detector '{self.detector_name}' on {self.date_of_results}>"

  def __repr__(self):
    return f"ResultValue('{self.detector_name}', '{self.date_of_results}')"

  def __len__(self):
    return len(self.results)

  def add_result(self, result):
    self.results.append(result)

  def get_average_of_results(self):
    if len(self.results) == 0:
      return 0
    return sum(self.results) / len(self.results)

  def get_maximum_of_results(self):
    return max(self.results)

result = ResultValue(name="Detector A", date="2026-03-03")  # initialising -> instantiating -> creating an object
result_two = ResultValue("Detector B", "2026-03-04")

print(result)
print(result_two)

result.add_result(123)  # abstraction
result.add_result(125)
result.add_result(98)
result.add_result(100)

print(result.results)

print(sum(result.results) / len(result.results))
print(result.get_average_of_results())

print(result_two.get_average_of_results())

print(result.get_maximum_of_results())

# result.get_range_of_results()

print(len(result))
print(len(result.results))


class ExperimentResults(ResultValue):
  def say_name(self):
    print(self.detector_name)

new_result = ExperimentResults("New Detector", "2026-01-01")

new_result.say_name()
print(new_result.results)




print([result, result_two]) # printing a list -> print -> __repr__