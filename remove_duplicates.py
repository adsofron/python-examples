# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:59:01 2018

@author: Alina
"""

def remove_duplicates(idk):
  str=[] #Empty list
  for x in idk: #iterating in original list
    if x not in str: #checking for duplicates in the new list
      str.append(x)
  return str


print(remove_duplicates([4, 5, 5, 4]))