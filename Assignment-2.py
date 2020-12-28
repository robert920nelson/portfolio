# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 19:24:48 2020

@author: rob
"""
import secrets

class get_numbers:
    def __init__(self, length):
        self.length = length
    def random_gen(length):
        randomlist=[]
        for i in range(length):
            randomlist.append(secrets.randbelow(1000001))
        return randomlist
    def fib_gen(length):
        fiblist=[1,1]
        n = 1
        while n <= (length-2):
            fiblist.append(fiblist[n]+fiblist[n-1])
            n += 1
        return fiblist
    
### TESTING ###

a=get_numbers
print(a.random_gen(5))
print(a.fib_gen(5))