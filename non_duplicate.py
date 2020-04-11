# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 22:02:50 2020

@author: nitish
"""

a=[1,2,3,3,1,1,3]


def non_duplicate(a):
 for i  in range(len(a)):
    x=0
    for j in range(len(a)):
        if(a[i]==a[j]):
            x=x+1
    if(x==1):
        print(a[i])
        

non_duplicate(a)