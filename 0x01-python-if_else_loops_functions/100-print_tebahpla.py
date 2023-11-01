#!/usr/bin/python3
for char in range(25, -1, -1):
    c = char + ord('A')
    if char % 2 == 1:
        c += 32
    print("{:c}".format(c), end="")
