def grammatically_correct(text):
    if type(text) != str:
        raise Exception("Only strings are allowed!")
    punctuation = '.!?'
    if text[0] == text[0].upper() and text[-1]in punctuation:
        return True
    else:
        return False