## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def grammatically_correct(text):
    """Checks that the start has a capital letter and then end has some sort of punctuation

    Parameters: (list all parameters and their types)
        text: a string of words (e.g "This is a short sentence.")

    Returns: (state the return value and its type)
        will return True if the text meets the requirements otherwise returns False

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a sentence 
Will check for a capital letter and punctuation at the end and will return True if it finds it
"""
grammatically_correct('This is a sentence.') => True
def test_correct_grammar_used():
    result = grammatically_correct('This is a sentence.')
    assert result == True

"""
Given some text with missing punctuation at the end
It returns False
"""
grammatically_correct('This is a sentence') => False

def test_no_punctuation():
    result = grammatically_correct('This is a sentence')
    assert result == False
"""
Given some text with a missing capital
It returns False
"""
grammatically_correct('this is a sentence!') => False
def test_no_capital():
    result = grammatically_correct('this is a sentence!')
    assert result == False

"""
Given something other than a string
It throws an error
"""
grammatically_correct(123) throws an error
def test_incorrect_datatype():
    with pytest.raises(Exception) as e:
        grammatically_correct(123)
    error_message = str(e.value)
    assert error_message == "Only strings are allowed!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
