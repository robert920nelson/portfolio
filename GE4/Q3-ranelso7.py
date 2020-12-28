# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:48:38 2020

@author: rob
"""

lorem = 'lorem ipsum dolor sit ad dolore consectetur adipiscing elit sed aliqua'
lorem2 = lorem.split(sep=' ')

### place your code below this line ###

dictD = {}

for x in sorted(lorem2):
    dictD[x] = len(x)

### place your code above this line ###

print(dictD)