# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:06:10 2024

@author: MY DUYEN
"""
import math 
a=float(input("nhap a:"))
b=float(input("nhap b:"))
A1=(math.sqrt(a) - math.sqrt(b)) / ((math.pow(a,1/4 )) - (math.pow(b,1/4 )))
A2=(math.sqrt(a) + (math.pow(a*b,1/4))) / ((math.pow(a,1/4)) + (math.pow(b,1/4)))
tong=A1-A2
print(f"ket qua la : {tong}")
