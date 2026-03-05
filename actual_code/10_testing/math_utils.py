def add(a, b):
  # raise TypeError if a or b is not an int or float
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    raise TypeError("Both arguments must be numbers.")

  if isinstance(a, bool) or isinstance(b, bool):
    raise TypeError("Both arguments must be numbers.") 
  
  return a + b


# test_  .py
#    _test.py