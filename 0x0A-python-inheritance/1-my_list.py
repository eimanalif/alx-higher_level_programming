#!/usr/bin/python3
"""
a module to inherits from a list
"""


class MyList(list):
    '''
    custom my list class
    '''
    def print_sorted(self):
        '''
        printing sorted list
        '''
        print(sorted(self))
