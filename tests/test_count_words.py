from lib.count_words import *
import pytest

def test_count_words_does_not_return_none():
    result = count_words('')
    assert result != None

def test_count_words_returns_number_of_words():
    result = count_words('Hello, world')
    assert result == 2

def test_catches_errors():
    with pytest.raises(Exception) as e:
        count_words(123)
    error_message = str(e.value)
    assert error_message == "Only strings are allowed!"