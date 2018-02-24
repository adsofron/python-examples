# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 17:55:36 2017

@author: Alina
"""
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y :
    print("x equals y")
    if y!= 0:
        print("x/y is ", x/y)
elif x < y :
        print("x is smaller")
else:
        print("y is smaller")
print("thanks")