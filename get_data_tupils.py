# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 21:56:33 2018

@author: Alina
"""

def get_data(a_tuple):
    nums = ()
    words = ()
    for t in a_tuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums,max_nums,unique_words)


(small,large,words) = get_data(( (1, 'mine'),(3,'yours'),(5,'ours'),(7,'mine')))
