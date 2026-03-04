"""
A utils module - contains ..., used in ..., things to remember, ... 
"""

def add(a, b):
  """
  A function that adds two numbers together.
  """
  return a + b

class Shape:
  """
  A class for Shapes
  """
  def __init__(self, type):
    """
    Initialises shapes and needs the type to be passed.
    """
    self.type = type

triangle = Shape("triangle")

if __name__ == "__main__":
  print("Hello from the utils module!")
  print(__name__)
  print(__file__)
  print(__doc__)