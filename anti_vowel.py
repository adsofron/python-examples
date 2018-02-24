# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:09:02 2018

@author: Alina
"""

def anti_vowel(text):
  new_text = ""
  for c in text:
    if c not in "aeiouAEIOU":
      new_text += c
  return new_text


print(anti_vowel("ana are mere!"))