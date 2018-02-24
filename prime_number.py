# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:40:29 2018

@author: Alina
"""

def is_prime(x):
    if x > 1:
       # check for factors
       for n in range(2,x):
           if (x % n) == 0:
               print(x,"is not a prime number")
               print(n,"times",x//n,"is",x)
               break
       else:
           print(x,"is a prime number")
           
    # if input number is less than
    # or equal to 1, it is not prime
    else:
       print(x,"is not a prime number")
      
print(is_prime(0))