# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 23:32:39 2018

@author: Alina
"""

def count(sequence,item):
  sum = 0
  for i in range(len(sequence)):
      if sequence[i] == item:
          sum += 1
  return sum

print(count([1, 2, 1, 1], 1) )