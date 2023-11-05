#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    list2 = []
    for i in my_list:
        if (i % 2) == 0:
            list2.append(True)
        else:
            list2.append(False)
    return list2
            
