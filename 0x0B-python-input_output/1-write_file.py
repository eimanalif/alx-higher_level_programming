#!/usr/bin/python3
'''defining write_file fuction'''


def write_file(filename="", text=""):
    '''read filename'''
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
