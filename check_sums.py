# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:32:45 2020

@author: nitish
"""

"""Given a list of numbers, return whether any two sums to k.
 For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17"""
 
 
def check_sums(a,k):
    for i in range(len(a)):
        for j in range(len(a)):
            x=a[i]+a[j]
            if(x==k):
              m=1 
    if(m==1):
       print("true")
    else:
       print("false")

