# test_reading.py
# Lab 10 solution - tests for the DataReading class

import pytest
from reading_module import DataReading


def test_reading_stores_text_and_source():
    r = DataReading("Temperature nominal in Sector 7", "Detector A")
    assert r.text == "Temperature nominal in Sector 7"
    assert r.source == "Detector A"


def test_get_word_count_counts_words():
    r = DataReading("One two three", "Detector A")
    assert r.get_word_count() == 3


def test_get_word_count_empty_string_is_zero():
    r = DataReading("", "Detector A")
    assert r.get_word_count() == 0


@pytest.mark.parametrize(
    "text, expected",
    [
        ("One", 1),
        ("One two", 2),
        ("One two three", 3),
        ("", 0),
    ],
)
def test_get_word_count_cases(text, expected):
    r = DataReading(text, "Detector A")
    assert r.get_word_count() == expected
