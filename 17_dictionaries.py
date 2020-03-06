# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 02:13:41 2020

@author: atakb
"""

dictionary = {"Python" : "Bir programlama dili.", "Php" : "Script dili.", "Java" : "Compile edilen dil."}
#print(type(dictionary))
print(dictionary["Python"] + "\n")

for i in dictionary.items():
    print(i) #Tuple
print("\n")
for i in dictionary:
    print(dictionary[i])
print("\n")
for i in dictionary.items():
    print(i[0] + " = " + i[1])
print("\n")
for i,j in dictionary.items():
    print(i + " = " + j)
    
classes = {"Ahmet" : "Veritabanı", "Oğuz" : "Java",
           "Barış" : ["Görüntü İşleme","Yapay Sinir Ağları","Veri Madenciliği"],
           "Okan" : ["Mekanik","Makel"], "Poyraz" : "İşletme", "Enes" : "Dinamik" }

name = input("İsim giriniz:")
print("{}'in aldığı dersler.".format(name))

for i in classes[name]:
    print(i)
print("\n")
"""
for i in classes:
    if(i == name):
        print(classes[i])
"""