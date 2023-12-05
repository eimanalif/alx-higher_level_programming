#!/usr/bin/python3
'''defining write_file fuction'''


def write_file(filename="", text=""):
    '''read filename with utf-8'''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
