# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 00:48:08 2020

@author: atakb
"""
# Break and Continue
"""
# break
def_u_name = "barış"
def_u_pass = "asd312"

while True:
    u_name = input("Kullanıcı Adınızı Giriniz:")
    u_pass = input("Şifrenizi Giriniz:")
    if(def_u_name != u_name or def_u_pass != u_pass):
        print("Kullanıcı adınızı veya şifrenizi yanlış girdiniz!!!")
    else:
        print("Hoşgeldiniz...")
        break
"""

# continue
for i in range(1,10):
    if(i==2):
        continue
    print(i)
    
print("\n")

liste = [1,3,4]
for i in range(1,10):
    if(i in liste): # Is there i in the list?
        continue
    print(i)

"""
# Continue always return the beginning of the cycle.
# So, this code enters the infinite cyle. 
i=0
while(i<10):
    print(i)
    if i==2:
        continue
    i+=1
"""