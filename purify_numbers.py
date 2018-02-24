# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 23:39:15 2018

@author: Alina
"""

def purify(numbers):
    new_list = ""
    for i in range(len(numbers)):
        if i % 2 == 0:
          new_list.append(i)
    return new_list
 
print(purify([1,2,3,4,5,6,67]))
        
    