# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:47:30 2018

@author: Alina
"""

# -*- coding: utf-8 -*-

low = 0
high = 100
average=int((low+high)/2)


print("Please think of a number between 0 and 100!")


while average :
    guess_nr = average
    print("Is your secret number",guess_nr,"?")
    x = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if x == 'l':
        low = guess_nr
        average=int((low+high)/2)
        print("h= average =",average)       
    elif x =='h':
        high = guess_nr   
        average=int((low+high)/2)
        print("l= average =",average)
    elif x == 'c':
        print("Game over. Your secret number was:",guess_nr)
        break
    else:
        print("Sorry, I did not understand your input.")