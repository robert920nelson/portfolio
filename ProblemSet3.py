# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 02:36:46 2020

@author: rob
"""

#problem set 3

#distance measures

#manhattan, euclidean, and minowski distance

import math

a, b, c, d = 1, 2, 10, 20

manh = abs(a-c) + abs(b-d)
print("Manhattan distance:", manh)

eucl = math.sqrt(abs(a-c)**2 + abs(b-d)**2)
print("Euclidean distance:", eucl)

mink = (abs(a-c)**3 + abs(b-d)**3)**(1/3)
print("Minkowski distance:", mink)

# INSTRUCTOR'S METHOD

P = [1, 2, 3]
Q = [10, 20, 30]

manhattan = (math.fabs(P[0] - Q[0]) + math.fabs(P[1] - Q[1]) + math.fabs(P[2] - Q[2]))

euclidean = (pow(pow(math.fabs(P[0] - Q[0]), 2) + 
                 pow(math.fabs(P[1] - Q[1]), 2) +
                 pow(math.fabs(P[2] - Q[2]), 2), 1/2))

minkowski = (pow(pow(math.fabs(P[0] - Q[0]), 3) + 
                 pow(math.fabs(P[1] - Q[1]), 3) +
                 pow(math.fabs(P[2] - Q[2]), 3), 1/3))

print("P[0] =", P[0], "P[1] =", P[1], "P[2] =", P[2])
print("Q[0] =", Q[0], "Q[1] =", Q[1], "Q[2] =", Q[2])
print("Manhattan Distance =", round(manhattan,2))
print("Euclidean Distance =", round(euclidean,2))
print("Minkowski Distance =", round(minkowski,2))

print()
print()
#PEARSON CORRELATION

P = [1, 2, 3]
Q = [10, 20, 30]
n = 3

# calculate the partial sums

sumpq = P[0]*Q[0] + P[1]*Q[1] + P[2]*Q[2]
sump = P[0] + P[1] + P[2]
sumq = Q[0] + Q[1] + Q[2]

sump2 = P[0]**2 + P[1]**2 + P[2]**2
sumq2 = Q[0]**2 + Q[1]**2 + Q[2]**2

# calculate the numerator and denominator

numerator = sumpq - (sump*sumq)/n

denominator = (pow(sump2 - (sump**2)/n, 0.5) * pow(sumq2 - (sumq**2)/n, 0.5))

# calculate and print the pearson correlation

r = numerator / denominator

print("P =", P)
print("Q =", Q)
print("Pearson Correlation =", round(r,2))

