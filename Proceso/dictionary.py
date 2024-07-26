def get_mapping(dictionary):
    ''' This function returns the mapping dictionaries for the education and gender'''
    if dictionary == "education":
        dict_map = {
            "Bachelors" : "Bachelor",
            "mastre" : "Master",
            "phd" : "PhD",
            "no education" : "NE"
        }
    elif dictionary == 'gender':
        dict_map = {
            "m" : "M",
            "f" : "F"
        }

    return dict_map