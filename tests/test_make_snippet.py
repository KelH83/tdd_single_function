from lib.make_snippet import *
import pytest

def test_returns_original_string_when_input_less_than_5():
    result = make_snippet('hello')
    assert result == "hello"

def test_5_word_snippet_with_5_word_input():
    result = make_snippet("Hello, here are five words")
    assert result == "Hello, here are five words"

def test_5_word_plus_snippet_with_over_5_word_input():
    result = make_snippet("Hello, here are thirteen words, but you will only see the first five")
    assert result == "Hello, here are thirteen words,..."

def test_catches_errors():
    with pytest.raises(Exception) as e:
        make_snippet(123)
    error_message = str(e.value)
    assert error_message == "Only strings are allowed!"
