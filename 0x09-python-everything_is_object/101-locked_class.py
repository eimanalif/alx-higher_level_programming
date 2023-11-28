#!/usr/bin/python3
"""
Define a locked class
"""


class LockedClass:
    """
    Prevent user from instantiating new lockedclass attributes
    for anything but attrbute called 'first_name'
    """

    __slots__ = ["first_name"]
