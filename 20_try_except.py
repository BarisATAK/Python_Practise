# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:51:23 2020

@author: atakb
"""
# try except ile oluşacak hatalara karşı önlem al.

number1 = input("sayı1 :")
number2 = input("sayı2 :")

try:
    print(int(number1)/int(number2))
except ZeroDivisionError:
    print("Bir sayı sıfıra bölünemez!")
except ValueError:
    print("Sayı yerine karakter girdiniz!")
#except (ZeroDivisionError,ValueError):
#    print("Bir hata oluştu!")

    
    
"""
if(int(number2) == 0):
    print("Bir sayı sıfıra bölünemez!")
else:
    print("Sayı yerine karakter girdiniz!")
"""
