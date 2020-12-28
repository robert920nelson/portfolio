# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 11:53:01 2020

@author: rob
"""

j=0
sum11=0

### Place your cose below this line ###

for j in range(10):
    sum11 = j * 11 + sum11
    j += 1
    print(j, "  sum11:", sum11)


### Place your code above this line ###


print('')
print("Total Sum11 is:", sum11)