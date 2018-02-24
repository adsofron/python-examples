# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 23:06:27 2018

@author: Alina
"""

def median(idk):
    new_list=[]
    for i in idk:
        new_list.append(i)
        new_list.sort()
    for i in range(len(new_list)):
        return new_list[len(i)/2.0]

print(median[5,6,2,5,7,8])