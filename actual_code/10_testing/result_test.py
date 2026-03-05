from result import ResultValue

def test_result_value_initialised_properly():
  r = ResultValue("Detector A", "2026-03-03")

  assert r.detector_name == "Detector A"
  assert r.date_of_results == "2026-03-03"
  assert r.results == []