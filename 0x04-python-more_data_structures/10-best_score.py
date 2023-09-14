#!/usr/bin/python3
def best_score(a_dictionary):
    key = ""
    big_key = None
    big_value = 0
    if not a_dictionary:
        return None
    else:
        for key in a_dictionary:
            if a_dictionary[key] > big_value:
                big_value = a_dictionary[key]
                big_key = key
    return big_key
