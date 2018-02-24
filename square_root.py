# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:51:50 2018

@author: Alina
"""

ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag= True
while ans**2 < x:
    ans = ans + 1
if ans**2 == x:
    print("Square root of",x,"is" ,ans)
else:
    print(x,"is not a perfect square")
    if neg_flag:
        print("Jsut checking... did you mean", -x,"?")
    