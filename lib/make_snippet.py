def make_snippet(string):
    if type(string) != str:
        raise Exception("Only strings are allowed!")
    else:
        string_list = string.split()
        if len(string_list) < 5:
            return string
        if len(string_list) == 5:
            first_five = []
            for num in range(5):
                first_five.append(string_list[num])
            words = " ".join(first_five)
            return words
        elif len(string_list) >5:
            first_five = []
            for num in range(5):
                first_five.append(string_list[num])
            words = " ".join(first_five)
            words += "..."
            return words