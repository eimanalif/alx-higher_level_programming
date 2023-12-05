#!/usr/bin/python3
"""defining append_ write fuction"""


def write_file(filename="", text=""):
    '''append filename with utf-8
     Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    '''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
