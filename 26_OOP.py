# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:28:22 2020

@author: atakb
"""
class Enemy:
    left_life = 10
    def Fight(self): #self sınıfımız içerisindeki nesneleri gösterir.
        print("Hücummmm")
        self.left_life -= 1
    def isLife(self):
        if(self.left_life == 0):
            print("Öldü")
        else:
            print(str(self.left_life) + " canım kaldı.")
            
enemy1 = Enemy() #Enemy classından enemy1 object'i oluşturuldu.            
enemy2 = Enemy()

enemy1.Fight()
enemy1.Fight()
enemy1.isLife()

enemy2.Fight() 
enemy2.Fight()
enemy2.isLife()

