# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:13:58 2020

@author: atakb
"""
from random import randrange as ran
import time

class Enemy:
    def __init__(self,name="Barış",left_life=100,fight_power=10,bullet_count=5):
        self.name = name
        self.left_life = left_life
        self.fight_power = fight_power
        self.bullet_count = bullet_count
        
    def Attack(self):
        print(self.name+" saldırıyor.")
        spent_bullets = ran(0,10)
        print(str(spent_bullets) + " mermi harcandı")
        self.bullet_count -= spent_bullets
        
        return spent_bullets,self.fight_power
    
    def CounterAttack(self,spent_bullets,fight_power):
        print("Vuruldum!!!")
        self.left_life -= (spent_bullets * fight_power)
        if(self.left_life < 0):
            self.left_life = 0
    
    def IsBulletOver(self):
        if(self.bullet_count <= 0):
            print(self.name+" konuşuyor: Mermim bitti oyundan çıkıyorum.")
            return True # Bullet is over
        return False
        
    def IsLife(self):
        if(self.left_life <= 0):
            print("Oyuncu öldü!!!")
            
    def Summary(self):
        print("*********<--Oyuncu Bilgisi-->**********")
        print("İsim = "+self.name+"\nKalan Can = "+str(self.left_life)+"\nSaldırı Gücü = "+str(self.fight_power)
        +"\nMermi Sayısı = "+str(self.bullet_count))
        print("***************************************")
    


enemies = []

for i in range(0,10):
    rand_life = ran(100,200)
    rand_power = ran(10,20)
    rand_bullet = ran(1,5)
    new_enemy = Enemy("Düşman_"+str(i+1),rand_life,rand_power,rand_bullet)
    enemies.append(new_enemy) #Append to enemies list.
    enemies[i].Summary()

print("<------------Oyun Başlıyor----------->")
i = 0
while(i < 10):
    print("\n")
    ranEnemy1 = ran(0,10)
    ranEnemy2 = ran(0,10)
    
    retValue = enemies[ranEnemy1].Attack() 
    enemies[ranEnemy2].CounterAttack(retValue[0],retValue[1])
    retValue2 = enemies[ranEnemy2].IsBulletOver()
    if(retValue2):
        enemies[ranEnemy2].Summary()
    else:
        enemies[ranEnemy2].IsLife()
        enemies[ranEnemy2].Summary()

    
    print(str(i+1) + ".Raund bitti...")
    time.sleep(2) #sleep 1 SECOND
    i+=1











