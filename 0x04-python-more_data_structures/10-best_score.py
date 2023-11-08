#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    val = 0
    key  = None
    for i, v in adictionary.items():
        if v > val:
            val = v
            key = i
   return key
