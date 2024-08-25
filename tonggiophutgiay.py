# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:48:55 2024

@author: MY DUYEN
"""

gio=int(input("nhap gio :"))
phut=int(input("nhap phut :"))
giay=int(input("nhap gio :"))
if 0<=gio<=24:
    if 0<=phut<=60:
        if 0<=giay<=60:
            hi= gio*3600+phut*60+giay
            print(f"{hi}") 
else:
                print("khong hop le ")
            
                    
                
    