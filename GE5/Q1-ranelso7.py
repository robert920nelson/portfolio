# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 18:57:47 2020

@author: rob
"""

# Fahrenheit to Celsuis Conversion = (Fahrenheit - 32) * (5/9)
# Celsuis to Fahrenheit Conversion = (Celsius * (9/5)) + 32

Fahrenheit = 100
ftoc = round((Fahrenheit - 32) * (5/9), 1)

print(ftoc)

Celsius = 31
ctof = round((Celsius * (9/5)) + 32, 1)

print(ctof)