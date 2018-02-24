# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:06:31 2017

@author: Alina
"""

s = "azcbobobegghakl"
n = 0
for i in range(1,len(s)+1):
    if s[i-1:i+2] == 'bob':
        n = n+1
print("Number of times bob occurs is: " ,n)
