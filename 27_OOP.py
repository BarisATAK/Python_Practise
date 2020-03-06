# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:43:25 2020

@author: atakb
"""
# Constructor --> def __init__(self):

class Enemy:
    """
    def __init__(self): #Constructor.
        self.name = "Barış"
        self.left_life = 100
        self.power = 30
        self.bullet_count = 4
    """    
    def __init__(self,name = "Barış",left_life = 100,power = 30,bullet_count=4):
        self.name = name
        self.left_life = left_life
        self.power = power
        self.bullet_count = bullet_count
        
    def PersonalInfo():
        name = input("Name : ")
        left_life = input("Left_life : ")
        power = input("Power : ")
        bullet_count = input("Bullet_count : ")
        return name,left_life,power,bullet_count
    
    def Summary(self):
        print("********************************")
        print("Name = "+self.name+"\nLeft Life = "+str(self.left_life)+"\nPower = "+str(self.power)+"\nBullet Count = "+str(self.bullet_count))
        print("********************************")


#Non-paramater Call
enemy_1 = Enemy()
enemy_1.Summary()

#Paramater call
enemy_2 = Enemy("Hasan",32,10,5)
enemy_2.Summary()

"""
name,left_life,power,bullet_count = Enemy.PersonalInfo()
enemy_par = Enemy(name,left_life,power,bullet_count)
enemy_par.Summary()
"""
