#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            divi = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            divi = 0
            print('divion by 0')
            continue
        except IndexError:
            divi = 0
            print('out of range')
            continue
        except TypeError:
            divi = 0
            print('wrong type')
            continue
        finally:
            new_list.append(divi)

    return new_list
