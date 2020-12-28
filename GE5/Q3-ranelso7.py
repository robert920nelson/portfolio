# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:14:05 2020

@author: rob
"""

# Fahrenheit to Celsuis Conversion = (Fahrenheit - 32) * (5/9)
# Celsuis to Fahrenheit Conversion = (Celsius * (9/5)) + 32

def convert_temp(degrees, cnv_type = 'ftoc'):    

    if type(degrees) is int:
        pass
    elif type(degrees) is float:
        pass
    else:
        return -2

    if cnv_type == 'ftoc':
         Celsius = round((degrees - 32) * (5/9), 1)
         return Celsius

    elif cnv_type == 'ctof':
        Fahrenheit = round((degrees * (9/5)) + 32, 1)
        return Fahrenheit
    
    else:
        return -1


    