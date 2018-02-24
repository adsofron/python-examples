# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 22:56:40 2018

@author: Alina
"""

n = [3, 5, 7]

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
# Don't forget to return your new list!

print(double_list(n))