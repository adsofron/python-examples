# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:34:09 2018

@author: Alina
"""

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = []
  for numbers in lists:
    for i in numbers: 
   		results.append(i)
  return results


print(flatten(n))