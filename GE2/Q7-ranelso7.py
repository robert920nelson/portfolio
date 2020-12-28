# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 12:14:45 2020

@author: rob
"""
from datetime import datetime

dt = datetime(2017, 8, 26, 14, 51, 33)
print('dt variable is:', dt)

# place your code below this line ###

dt2 = dt.strftime('%m/%d/%Y')


### place your code above this line ###

print('dt2 date is:', dt2)