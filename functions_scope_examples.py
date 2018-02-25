# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 22:43:58 2018

@author: Alina
"""

x = 12
def num_1(x):
      x = x + 1
      def num_2(y):
          return x + y
      return num_2(6)
print(num_1(x))