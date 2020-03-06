# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 02:53:02 2020

@author: atakb
"""

import Modules
#from Modules import * #Other using.
#from Modules import Dictionary
from math import factorial
from matplotlib import pyplot as plt

word = input("Aradığınız kelimeyi giriniz:")

a = Modules.Dictionary(word)
print("{} = {}".format(word, Modules.Dictionary(word)))

number1 = int(input("Karesi alınacak sayıyı giriniz:"))
print("{}^2 = {}".format(number1, Modules.CalculateSquare(number1)))

number2 = int(input("Karakökü alınacak sayıyı giriniz:"))
print("{}^0.5 = {}".format(number2, Modules.RootOfSquare(number2)))

fact = int(input("Faktoriyeli hesaplanacak sayıyı giriniz:"))
print("{}! = {}".format(fact, factorial(fact)))

x1,x2,x3 = input("X değerlerini giriniz:").split()
y1,y2,y3 = input("Y değerlerini giriniz:").split()

print("X ve Y değerlerine göre oluşan grafik:")
plt.plot([x1,x2,x3],[y1,y2,y3])
