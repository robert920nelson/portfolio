# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:55:44 2020

@author: rob
"""

historical = 0, 6, 2, 8, 6, 2, 0, 8, 9, 9
predictiona = 8, 6, 2, 8, 0, 3, 4, 8, 2, 5
predictionb = 3, 4, 2, 1, 1, 7, 0, 6, 7, 9,

print('')
print('historical:', historical)
print('predictiona:', predictiona)
print('predictionb:', predictionb)
print('')

### place your code below this line ###

for x, y, z in zip(historical, predictiona,predictionb):
    print('historical:', x, 'predictiona:', y, 'predictionb:', z)

### place your code above this line ###