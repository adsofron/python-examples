# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 22:29:23 2018

@author: Alina
"""

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    if x%2 == 1:
        return True
    else:
        return False
    
odd(32)
print(odd(32))