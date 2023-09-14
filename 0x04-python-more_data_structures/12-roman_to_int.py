#!/usr/bin/python3
def roman_to_int(roman_string):

    if type(roman_string) is not str or roman_string is None:
        return (0)
    all_t = 0
    r_di = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(roman_string)):
        a = r_di.get(roman_string[i])
        if (i < len(roman_string) - 1):
            aa = r_di.get(roman_string[i + 1])
            if aa > a:
                all_t -= a
            else:
                all_t += a
        else:
            all_t += a
    return (all_t)
