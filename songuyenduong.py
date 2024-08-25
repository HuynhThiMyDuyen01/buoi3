# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:33:02 2024

@author: MY DUYEN
"""

N=int(input("Nhap 2 so nguyen duong "))
if 9<N<100:
    chuc= N%10
    donvi= N//10
    print(f"{chuc+donvi}")
else:
    print("khong hop le ")
    
