# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 00:25:10 2020

@author: atakb
"""

# Factorial calculation with for cycle
while True:
    number = int(input("Faktoriyeli hesaplanacak sayıyı giriniz: "))
    fact = number
    if(number <= 0):
        print("lütfen negatif olmayan bir sayı giriniz...")
    else:
        for i in range(1,number):
            fact *= i
        print(str(number) + "! = ", fact)
        break


