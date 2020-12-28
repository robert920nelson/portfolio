# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:55:15 2020

@author: rob
"""

my_list = ['action', 'table', 'tennis', 'apple', 'tarp']
dictF = {}

### place your code below this line ###

for x in sorted(my_list):
    letter = x[0]
    dictF.setdefault(letter, []).append(x)

### place your code above this line ###

print('dictF:', dictF)