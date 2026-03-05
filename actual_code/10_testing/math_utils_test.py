from math_utils import add
import pytest

# [x] Two numbers add together properly
# [x] Different types (large, negative, decimal, mix)
# [ ] It fails when I try to add non-numbers

def test_two_numbers_add_together_properly():
  # Arrange - getting the world ready
  num1 = 3
  num2 = 4
  expected = 7

  # Act - using the thing (function or method) under test
  result = add(num1, num2)

  # Assert - declare that certain things are true
  assert expected == result

def test_two_negative_numbers_add_correctly():
  assert add(-1, -1) == -2

# Parameterizing the test
@pytest.mark.parametrize("num1, num2, expected", [
  (-100, -100, -200),
  (1_000_000, 1_000_000, 2_000_000),
  (100, -10, 90),
  (1_000_000, 10, 1_000_010)
])
def test_a_variety_of_numbers_add_to_the_correct_value(num1, num2, expected):
  assert add(num1, num2) == expected


# Be aware - floating point numbers can act strangely!
def test_floating_point_numbers_add_correctly():
  assert add(0.1, 0.2) == pytest.approx(0.3)


@pytest.mark.parametrize("val1, val2", [
  ("", ""),
  ("", 3),
  ([], []),
  ({}, []),
  (True, True)
  ])
def test_add_raises_typeerror_when_trying_to_add_non_numbers(val1, val2):
  with pytest.raises(TypeError):
    add(val1, val2)

# red -> green -> refactor