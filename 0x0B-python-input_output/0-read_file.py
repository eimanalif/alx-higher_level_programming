#!/usr/bin/python3
"""defining read function"""


def read_file(filename=""):
    ''' reads file '''
    with open(filename, encoding= 'utf-8') as f:
        print(f.read(), end="")
