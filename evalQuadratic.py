# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 22:26:46 2018

@author: Alina
"""

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    print( a*(x**2) + b * x + c)
    return a*(x**2) + b * x + c


evalQuadratic(2,2,2,2)