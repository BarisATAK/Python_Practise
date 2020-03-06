# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:28:28 2020

@author: atakb
"""
#varsayılan değer alan parametreler

info = "Bilgi yok" 
def AddRecord(name = info, l_name = info, age = info, job = info ):
    print("Ad = {} \nSoyad = {} \nYaş = {} \nMeslek = {}".format(name, l_name, age, job))
    print("Kayıt başarıyla eklendi....")

AddRecord("Barış","Atak",job = "Bilgisayar Mühendisliği")