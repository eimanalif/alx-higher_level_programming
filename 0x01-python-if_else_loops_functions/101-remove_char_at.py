#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    for s, c in enumerate(str):
        if s != n:
            str2 += c
    return str2
