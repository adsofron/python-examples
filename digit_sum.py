# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:55:45 2018

@author: Alina
"""

def digit_sum(n):
    sum = 0
   
    for i in str(n):
       sum += int(i)
       print("i=",i)
    return sum

print(digit_sum(434))