# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:45:14 2020

@author: nitish
"""



a={1,2,3}

a=list(a)
b=[]

p=[{}]  

for i in range(len(a)):
    for j in range(i,len(a)):
        b=list(b)
        b.append(a[j])
        b=set(b)
        p.append(b)
    b=[]
        