# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:21:28 2018

@author: Alina
"""

def gcd_iter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    x = 0
    if a < b:

      bigger = b
    else:

      bigger = a
    for i in range(1,bigger):
         if a % i == 0 and b % i == 0:
             x= i

    return x

print (gcd_iter(9, 12))
