# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:50:19 2017

@author: Alina
"""


s = "abdefhabckfor"
n = 0
x = 0
word =""
for i in range(1,len(s)-1):
    if s[i] > s[i-1] :
        word= word + s[i]
        print(word)
    else:
        break
print("Longest substring in alphabetical order is: " ,word)

