# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 11:42:59 2020

@author: rob
"""

input1 = int(input('Enter an integer number: '))

### Place your code below this line ###

if input1 < 0:
    print("Input 1 integer is negative")
elif input1 == 0:
    print("Input 1 integer is zero")
elif input1 <= 30:
    print("Input 1 is positive but less or equal than 30.")
else:
    print("Input 1 is positive and greater than 30.")

### Place your code above this line ###