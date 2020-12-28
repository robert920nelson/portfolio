# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 23:14:44 2020

@author: rob
"""

##PROBLEM SET 2##

import math

euros = 200

exchange = 1.09

dollars = round(euros * exchange, 2)
print(dollars)

print(f"{euros} Euros is equal to {dollars} dollars.")

# example 2
print()

bill = 39.98
tip = 0.15
total = round(bill * (1 + tip),2)

print("bill:", bill)
print("tip percentage:", tip)
print("total due:", total)

# example 3

print()

var1 = 5

remainder = var1%2
isEven = (remainder==0)

print("Number =", var1)
print("Number%2 =", remainder)
print("Is number even?", isEven)

# example 4
print()

money = 259

twenties = money//20
money = money - twenties*20
print("twenties", twenties)


tens = money//10
money = money - tens*10
print("tens", tens)

fives = money//5
money = money - fives*5
print("fives", fives)

ones = money//1
money = money - ones*1
print("ones", ones)

print(money)
