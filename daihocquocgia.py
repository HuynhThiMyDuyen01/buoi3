# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:35:04 2024

@author: MY DUYEN
"""

chuoi="Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
din = chuoi.split(", ")
print(din)
print("Tach thanh cac sub-string (theo yeu cau 1):")
for u in din:
    print(u)
     
    
    
anh = chuoi.replace("P. ","").replace("Q. ","").replace("Tp. ","").split(", ")
print(anh)
print("Tach thanh cac sub-string (theo yeu cau 2 ):")
for g in anh:
    print(g)
    
    
    