from headline_module import Headline

def test_the_word_count():
  h = Headline("One two three", "BBC")

  assert h.get_word_count() == 3