#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup1 = tuple_a[0] if len(tuple_a) > 0 else 0
    tup2 = tuple_a[1] if len(tuple_a) > 1 else 0
    tupl1 = tuple_b[0] if len(tuple_b) > 0 else 0
    tupl2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (tup1 + tupl1, tup2 + tupl2)

