# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 22:00:27 2018

@author: Alina
"""



def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3, 0)
print(foo(3, 0) )


