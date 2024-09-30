def count_words(string):
    if type(string) != str:
        raise Exception("Only strings are allowed!")
    
    else:
        string_list = string.split()
        return len(string_list)