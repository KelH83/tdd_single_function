def calculate_reading_time(text):
    if type(text) != str:
        raise Exception("Only strings are allowed!")
    text_list = text.split()
    total_words = len(text_list)
    minutes_needed = round(total_words/200)
    if minutes_needed < 1:
        return "less than 1 minute"
    elif minutes_needed == 1:
        return "1 minute"
    else:
        return f"{minutes_needed} minutes"