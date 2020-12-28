# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 12:04:25 2020

@author: rob
"""

sum5 = 0
sum2 = 0

### Place your code below this line ###

for j in range(11):
    sum5 = j * 5 + sum5
    sum2 = j * 2 + sum2

### Place your code above this line ###

print('sum2', sum2, 'divided by sum5', sum5, 'is', sum2 / sum5)