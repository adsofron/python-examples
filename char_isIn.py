# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 18:14:58 2018

@author: Alina
"""
"""First, test the middle character of a string against the character you're looking for (the "test character").
 If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the middle character.
If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string.
(Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr.
char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value
"""
def is_in(char,a_str):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    #  string is empty
    print(len(a_str))

    if a_str == '':
        return False

    # string is of length 1
    if len(a_str) == 1:
         return a_str == char

    # the test character equals the middle character
    mid_str = len(a_str)//2
    a_str_new = a_str[midStr]
    
    if char == a_str_new:
        return True
    elif char > a_str_new:
        return is_in(char, a_str[:mid_str])
    else :
        return is_in(char, a_str[mid_str+1:])



print(is_in('g','dfghjknnnooppsvxy'))
