# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:06:10 2020

@author: nitish
"""
def edit_distance():
    a=input("enter string")
    b=input("enter string")
    print(abc(a,b))
    
def abc(a,b):
    a=list(a)
    b=list(b)
    e=0
    if len(b)==len(a): 
     for i in range(len(a)):
        if a[i]!=b[i]:
           b[i]=a[i]
           e=e+1
        
    elif len(b)<len(a):
        for i in range(len(b)): 
             if a[i]!=b[i]:
                b[i]=a[i]
                e=e+1
        for i in range(len(b),len(a)):
               b.append(a[i]) 
               e=e+1
    elif len(b)>len(a):
         for i in range(len(a)): 
             if a[i]!=b[i]:
                b[i]=a[i]
                e=e+1
         for i in range(len(a),len(b)):
               b.pop(i) 
               e=e+1
    return(e)

edit_distance()
               
  
   

        