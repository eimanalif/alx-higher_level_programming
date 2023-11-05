#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for list1 in matrix:
        if len(list1) == 0:
            print()
        for i in range(len(list1)):
            print("{}".format(list1[i]),
                    end="\n" if i is len(list1) -1 else " ")
