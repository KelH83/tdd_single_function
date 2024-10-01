from lib.grammatically_correct import *
import pytest

def test_correct_grammar_used():
    result = grammatically_correct('This is a sentence.')
    assert result == True

def test_no_punctuation():
    result = grammatically_correct('This is a sentence')
    assert result == False

def test_no_capital():
    result = grammatically_correct('this is a sentence!')
    assert result == False

def test_incorrect_datatype():
    with pytest.raises(Exception) as e:
        grammatically_correct(123)
    error_message = str(e.value)
    assert error_message == "Only strings are allowed!"