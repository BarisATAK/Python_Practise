# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 20:16:15 2020

@author: atakb
"""
# if-else example.
# Control program for user name and user password.

user_name = input("Kullanıcı adınızı giriniz:")
password  = input("Şifrenizi giriniz:")
try_again = "Tekrar Deneyiniz..."

database  = ["name", "pass"] # user_name, password

if user_name == database[0] and password == database[1]:
    print("Kullanıcı adı ve şifre doğru. Hoşgeldiniz...")
elif user_name == database[0] and password != database[1]:
    print("Şifreniz yanlış!!!")
elif user_name != database[0] and password == database[1]:
    print("Kullanıcı adınız yanlış!!!")
else:
    print(try_again)