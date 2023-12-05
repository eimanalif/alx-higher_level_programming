#!/usr/bin/python3
'''defining append_ write fuction'''


def write_file(filename="", text=""):
    '''append filename with utf-8'''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
