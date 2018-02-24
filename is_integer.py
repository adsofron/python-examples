# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:45:09 2018

@author: Alina
"""
def is_int(x):
    y = int(x) - float(x)
    print(int(x))
    print(float(x))
    if y == 0:
        return True
    else:
        return False

print(is_int(70.1))

