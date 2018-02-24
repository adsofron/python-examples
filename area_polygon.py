# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:05:39 2018

@author: Alina
"""
from math import * 
def polysum(n,s): 
    ''' 
    n,s : positive integers
    returns:a positive integer, the sum between the area and square of the perimeter of the regular polygon 
    '''
    def perimeter(n,s): 
        ''' 
        n,s : positive integers
        returns:a positive integer, the perimeter of a polygon 
        '''
        p = n * s 
        return p*p 
    def area(n,s): 
        ''' 
        n,s : positive integers
        returns:a positive integer, the area of a polygon 
        '''
        a = s * s 
        b = 0.25 * n * a 
        c = tan(pi/n) 
        return b/c 
    return round(perimeter(n,s) + area(n,s),4)