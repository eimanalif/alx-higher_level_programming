#!/usr/bin/python3
for number in range(10):
    for number2 in range(number, 10):
        if number < number2:
            print("{:d}{:d}".format(number, number2),
                 end="\n" if number == 8 and number2 == 9 else ", ")
