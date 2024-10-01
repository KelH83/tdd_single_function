## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, 
assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def calculate_reading_time(text):
    """calculates the reading time for the text inputted as a parameter

    Parameters: (list all parameters and their types)
        text: assume a long string, likely at least a few paragraphs containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        an amount of time, based on the user being able to read 200 words per minute, so will be in minute format

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
Given less than 200 words total
It returns less than a minute as the reading time
"""
calculate_reading_time("Hello there") => ["less than 1 minute"]

def test_calculate_time_for_less_than_200_words():
    result = calculate_reading_time('Hello world')
    assert result == "less than 1 minute"

"""
Given 200 words total
It returns a single minute as the reading time
"""
calculate_reading_time("Pretend this is 200 words") => ["1 minute"]

def test_calculate_time_for_200_words():
    result = calculate_reading_time('I will add 200 actual words in the real code')
    assert result == "1 minute"

"""
Given 600 words total
It returns 3 minutes as the reading time
"""
calculate_reading_time("Pretend this is 600 words") => ["3 minutes"]

def test_calculate_time_for_600_words():
    result = calculate_reading_time('I will add 600 actual words in the real code')
    assert result == "3 minutes"


calculate_reading_time(123) throws an error
def test_capture_errors():
    with pytest.raises(Exception) as e:
        calculate_reading_time(123)
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
