# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 22:47:09 2018

@author: Alina
"""

def iter_power(base,exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    for i in range (1,exp+1):
        result = result * base

    return result

print(iter_power(2,4))
