# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:29:42 2020

@author: rob
"""

import math

#define class similarity
class similarity:
    
    # class instantiation
    def __init__ (self, ratingP, ratingQ):
        self.ratings1 = ratingP
        self.ratings2 = ratingQ
        
    # Minkowski Distance between two vectors
    def minkowski(self, r):
        
    # initialize distance
        dist = 0
        
    # consider only if both users have rated item
        for i in self.ratings1:
            if i in self.ratings2:
                
    # calculate minkowski distance using computationally efficient form
                dist = dist + pow(math.fabs(self.ratings1[i] - self.ratings2[i]), r)
        
        dist = pow (dist, 1/r)
        
        return dist
                
        
    # Pearson Correlation between two vectors
    def pearson(self):
        
    # initialize component sums
        n = 0
        sumpq = 0
        sump = 0
        sumq = 0
        sump2 = 0
        sumq2 = 0
        
    # consider only if both users have rated item
        for item in self.ratings1:
            if item in self.ratings2:
                          
    # calculate pearson correlation using computationally efficient form
                n = n+1
                sumpq += self.ratings1[item] * self.ratings2[item]
                sump += self.ratings1[item]
                sumq += self.ratings2[item]
                sump2 += pow(self.ratings1[item], 2)
                sumq2 += pow(self.ratings2[item], 2)
                
        numerator = (sumpq - (sump * sumq) / n)
        denominator = (math.sqrt(sump2 - pow(sump, 2) / n) *
                       math.sqrt(sumq2 - pow(sumq, 2) / n))
                
        r = numerator/denominator
        return r
        
# user ratings
UserPRatings = {'Motorola':8, 'LG':5, 'Sony':1, 'Apple':1, 'Samsung':5, 'Nokia':7}
UserQRatings = {'Apple':7, 'Samsung':1, 'Nokia':4, 'LG':4, 'Sony':6, 'Blackberry':3}

x = similarity(UserPRatings, UserQRatings)

print ("Manhattan Distance (r=1) =", round(x.minkowski(1),4))
print ("Euclidean Distance (r=2) =", round(x.minkowski(2),4))
print ("Minkowski Distance (r=3) =", round(x.minkowski(3),4))
print ("Pearson Correlation      =", round(x.pearson(),4))