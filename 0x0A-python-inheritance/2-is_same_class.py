#!/usr/bin/python3
'''
a module that return true or false
'''


def is_same_class(obj, a_class):
    '''
    function that returns True if the object is exactly an instance
    '''
    return type(obj) == a_class
