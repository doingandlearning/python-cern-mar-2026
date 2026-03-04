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

result = ResultValue("Detector A", "2026-03-03")

result.add_result(100)
result.get_average_of_results()
result.get_maximum_of_results()
result.get_range_of_results()