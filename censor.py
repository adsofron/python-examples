# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 23:26:12 2018

@author: Alina
"""

def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
            print(words)
        count += 1
    result =' '.join(words)

    return result

print(censor("this hack is wack hack", "hack"))