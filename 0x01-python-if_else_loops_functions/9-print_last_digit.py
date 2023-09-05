#!/usr/bin/python3
def print_last_digit(n):
    if n < 0:
        n = -n
    l_d = n % 10

    print("{:d}".format(l_d), end='')
    return (l_d)
