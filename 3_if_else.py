# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:40:38 2020

@author: atakb
"""

#if, elif, else
letters = ["AA","BB","CC","DD","FF"]
letterFactors = ["4.0","3,5","3.0","2.5","0.0"]

note = float(input("Notunuzu Giriniz: "))
text1 = "Harfiniz : "
text2 = "Harf Katsayınız : "
if note <= 100 and note >= 90:
    print(text1 + letters[0])
    print(result)
elif note < 90 and note >= 80:
    print(text1 + letters[1])
    result = letters[1]
elif note < 80 and note >= 70:
    print(text1 + letters[2])
    result = letters[2]
elif note < 70 and note >= 60:
    print(text1 + letters[3])
    result = letters[3]
else:
    print(text1 + letters[4], ". Maalesef bu dersten kaldınız !!!\n\n")
    result = letters[4]
    
    
if result == letters[0]:
    print(text2 + letterFactors[0])    
elif result == letters[1]:
    print(text2 + letterFactors[1])
elif result == letters[2]:
    print(text2 + letterFactors[2])
elif result == letters[3]:
    print(text2 + letterFactors[3])
else:
    print(text2+ letterFactors[4])