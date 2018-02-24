# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:17:36 2018

@author: Alina
"""

n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in range(len(numbers)):
      	result = result + result[i]
  return result

print(total(n))