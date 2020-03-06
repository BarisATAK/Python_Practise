# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:08:53 2020

@author: atakb
"""
print("Ders Programı Veritabanı Sistemi")

days = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]

class1 = input(days[0] + ":")
class2 = input(days[1] + ":")
class3 = input(days[2] + ":")
class4 = input(days[3] + ":")
class5 = input(days[4] + ":")

classes = [class1, class2, class3, class4, class5]

print("Dersler Veritabınına Kaydediliyor...")

print(days[0] + ":", classes[0])
print(days[1] + ":", classes[1])
print(days[2] + ":", classes[2])
print(days[3] + ":", classes[3])
print(days[4] + ":", classes[4])

