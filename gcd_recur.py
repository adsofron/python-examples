# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:53:26 2018

@author: Alina
"""


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a == b:
        return a
    elif a > b:
        return gcdRecur (a - b,b)
    else:
        return gcdRecur(a, b - a)
    
    
print (gcdRecur(9, 12))

