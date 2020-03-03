# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:47:10 2020

@author: nitish
"""

"""Given an array of integers, return a new array such that each
 element at index i of the new array is the product of all the numbers in the original array except the one at i."""
 
z=[]
a=[1,2,3,4,5]
for i in range(len(a)):
    m=1
    for j in range(len(a)+1):
        if(i!=j and j<=len(a)-1):
           m=m*a[j]
        elif(j==len(a)):
            z.append(m)
print(z)



