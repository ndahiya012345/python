# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 17:06:54 2020

@author: nitish
"""

"""Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place."""

def find(b):
    b.sort()
    b=set(b)
    b=list(b)
  
   
    def infinity():
      i=0
      while True:
           yield(i)
           i+=1
         
         
    for j in infinity():
       if(b[j]!=j ):
        print(j)
        break
       else:
         continue
        

a=[8,0,1,2,3,3,4,7,-1]
        

find(a)    
      
        
        
        

   
    