# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 12:39:48 2018

@author: Alina
"""

from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)


guesses_left = 3
# Start your game!
while guesses_left > 0:
      guess = int(input("Your guess: "))
      if guess == random_number: # correct guess
        print("You win!")
        break
      guesses_left -= 1
else:
    print("You lose.")
   