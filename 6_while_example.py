# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 20:46:09 2020

@author: atakb
"""

# while example and break

def_user_name = "barış"
def_user_pass = "123"

u_name_err = "Kullanıcı adını yanlış girdiniz."
u_pass_err = "Şifrenizi yanlış girdiniz."
try_again = "Tekrar Deneyiniz!!!"
while(True):
    u_name = input("Kullanıcı adınızı giriniz: ")
    u_pass = input("Kullanıcı şifrenizi giriniz: ")
    if(u_name == def_user_name and u_pass == def_user_pass):
        print("Hoşgeldiniz...")
        break
    elif(u_name != def_user_name and u_pass == def_user_pass):
        print(u_name_err, try_again)
    elif(u_name == def_user_name and u_pass != def_user_pass):
        print(u_pass_err)
        isChange = input("Şifrenizi değiştirmek ister misiniz?(E/H) : ")
        if(isChange == "E" or isChange == "e"):
            def_user_pass = input("Yeni şifrenizi giriniz:")
        else:
            print(try_again)
        
        