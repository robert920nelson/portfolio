# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:08:08 2020

@author: rob
"""

# Fahrenheit to Celsuis Conversion = (Fahrenheit - 32) * (5/9)
# Celsuis to Fahrenheit Conversion = (Celsius * (9/5)) + 32

a = {}

for x in range(0,36,2):
    a[x] = round((x * (9/5)) + 32, 1)

a[23] = 16.4
a = sorted(a)
print(a)