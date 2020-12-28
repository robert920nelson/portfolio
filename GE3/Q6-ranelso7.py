# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:04:30 2020

@author: rob
"""

btcdec1 = [11234, 12475]

# first task
btcdec1.append(14560)

# second task
btcdec2 = []
btcdec2.append(15630)
btcdec2.append(12475)
btcdec2.append(14972)

# third task
btcdec1.extend(btcdec2)

# fourth task
btcdec1 = sorted(btcdec1)

print(btcdec1)