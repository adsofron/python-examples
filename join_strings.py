# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:21:47 2018

@author: Alina
"""

n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ""
  for i in range(len(words)):
      result = result + words[i]
  return result

print(join_strings(n))