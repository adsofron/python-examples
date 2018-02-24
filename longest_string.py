# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:50:19 2017

@author: Alina
"""


s = "azcbobobegghakl"
n = 0
x = 0
word =""
for i in range(1,len(s)-1):
    if s[i-1] < s[i] :
        word= word +s[i-1] + s[i]
        print(word)
       
    elif s[i-1] > s[i] or s[i] == s[i]:
        n = n+1 
         
print("Longest substring in alphabetical order is: " ,word)
print("n = ",n)
