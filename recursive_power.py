# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 23:03:06 2018

@author: Alina
"""

def recur_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recurPower(base,exp-1)

print(recur_power(2,4))
