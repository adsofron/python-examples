# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 23:31:37 2017

@author: Alina
"""

count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))