# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:55:10 2017

@author: Alina
"""
s = "azcbobobegghakl"
n = 0
for vowel in s:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
        n = n +1
print("Number of vowels:" ,n)
