class InvalidDetectorError(Exception):
  pass

def get_detector_from_user():
  valid_detectors = ["alice", "atlas", "lhc"]
  user_input = input("Which detector do you want? ").lower().strip()

  if not user_input in valid_detectors:
    raise InvalidDetectorError(f"{user_input} is not a valid detector.")
  
  return user_input

try: 
  valid_detector = get_detector_from_user()
  print(valid_detector)
except InvalidDetectorError as err:
  print(err, type(err))