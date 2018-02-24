# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 21:18:42 2017

@author: Alina
"""
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 