#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_d = abs(number) % 10
print(f"Last digit of {number} is {l_d}", end=" ")
if l_d > 5:
    print("and is greater than 5")
elif l_d == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
