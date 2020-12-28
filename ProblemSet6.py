# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:01:03 2020

@author: rob
"""

lstA = [1, 2, 3, 4, 5]
lstB = [10, 20, 30, 40, 50]

listC = []

for a, b in zip(lstA, lstB):
    listC.append(a + b)
    
print(listC)
print()

# question 2

def addLists(lst1, lst2):
    lst = []
    for l1, l2, in zip(lst1, lst2):
        lst.append(l1 + l2)
    return (lst)

listC = addLists(lstA, lstB)
print (listC)

print()

# question 3

class listComposites:
    
    def __init__ (self, lst1, lst2):
        print("instantiation")
        self.list1 = lst1
        self.list2 = lst2
    
    def addLists(self):
        print("addList method")
        lst = []
        for l1, l2 in zip(self.list1, self.list2):
            lst.append(l1+l2)
        return (lst)
    
    def subLists(self):
        print("subLists method")
        lst = []
        for l1, l2 in zip(self.list1, self.list2):
            lst.append(l1-l2)
        return(lst)
        
    
lc = listComposites(lstA, lstB)
lstC = lc.addLists()
print(lstC)

lstC = lc.subLists()
print(lstC)
