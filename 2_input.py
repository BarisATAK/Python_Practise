# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:08:53 2020

@author: atakb
"""

# input(), format()

print("Oyuncu Kaydetme Programı")

name = input("Oyuncunun Adı: ")
lastName = input("Oyuncunun Soyadı: ")
team = input("Oyuncunun Takimi: ")

informationList = [name, lastName, team]
print("Veritabanına kaydediliyor....")

print("Oyuncunun adı:{}\n Oyuncunun Soyadı:{}\n Oyuncunun takımı:{}\n".format(informationList[0],informationList[1],informationList[2]))

print("Bilgiler Veritabanına Kaydedildi...")

