# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:53:26 2018

@author: Alina
"""


def gcd_recur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a == b:
        return a
    elif a > b:
        return gcd_recur (a - b,b)
    else:
        return gcd_recur(a, b - a)


print (gcd_recur(9, 12))
