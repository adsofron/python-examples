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
def isIn(char,aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    #  string is empty
    print(len(aStr))
    
    if aStr == '':
        return False
   
    # string is of length 1    
    if len(aStr) == 1:  
         return aStr == char
    
    # the test character equals the middle character     
    midStr = len(aStr)//2
    aStr_new = aStr[midStr]
    
    if char == aStr_new:
        return True
    elif char > aStr_new:
        return isIn(char, aStr[:midStr])
    else :
        return isIn(char, aStr[midStr+1:])


    
print(isIn('g','dfghjknnnooppsvxy'))
