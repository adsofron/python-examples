# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:22:28 2018

@author: Alina
"""

def factorial(x):
    multiply = 1
    while x > 0:
       multiply *= x
       x=x-1
    return multiply

print(factorial(4))