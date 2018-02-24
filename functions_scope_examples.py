# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 22:43:58 2018

@author: Alina
"""

x = 12
def g(x):
      x = x + 1
      def h(y):
          return x + y
      return h(6)
g(x)