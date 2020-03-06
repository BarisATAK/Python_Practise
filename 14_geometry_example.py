# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:13:22 2020

@author: atakb
"""

# Fonksiyon 3 elemanlı ise bu elemanların bir üçgen belirtip belirtmediği
# 4 elemanlı ise dörtgeni oluşturduğunu söyleyecek.

def Geometry(shape):
    if(len(shape) == 3):
        a = shape[0]
        b = shape[1]
        c = shape[2]
        
        if((a+b)>c and (b+c)>a and (a+c)>b): #Üçgen belirtir.
            if(a==b and a==c and b==c):
                print("Eşkenar üçgen.")
            elif((a==b and a==c) or (a==b and b==c) or (a==c and b==c)):
                print("İkizkenar üçgen.")
            else:
                print("Çeşitkenar üçgen.")
        else:
            print("Üçgen belirtmiyor!!!")
    elif(len(shape) == 4):
        a = shape[0]
        b = shape[1]
        c = shape[2]
        d = shape[3]
        if(a==b and b==c and c==d):
            print("Kare.")
        elif(a==c and b==d):
            print("Dikdörtgen.")
        else:
            print("Normal dörtgen.")
            
            
while True:
    value_count = int(input("Eleman sayısını giriniz:"))
    
    if(value_count == 3):
        a = int(input("a ="))
        b = int(input("b ="))
        c = int(input("c ="))
        Geometry([a,b,c])
    elif(value_count == 4):
        a = int(input("a ="))
        b = int(input("b ="))
        c = int(input("c ="))
        d = int(input("d ="))
        Geometry([a,b,c,d])    
    else:
        print("Tekrar deneyiniz...")
            
            
            
            
            
            
            