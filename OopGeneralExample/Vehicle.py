# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 02:35:31 2020

@author: atakb
----araba----	----motor---
motor gücü	motor gücü
model		model
marka		marka
yakıt tüketimi  yakıt tüketimi
kilometre	kilometre
kasa tipi
renk		renk
durumu		durumu(2.el)
		silindir sayısı
vites 		vites
		tipi(scooter)
çekiş(önden)
"""
from random import choice     

car_list = [["BMW i8","AUDI Q2","TESLA S","MERCEDES G63"],["Sedan","Hatchback"]]
mot_list = [["HONDA CB1000R","BMW F-750 ","YAMAHA YZF-R6","HARLEY-DAVIDSON V-ROD"],["2 Silindir","4 Silindir"]]
km_list = [1000,0,150000,70000,8000,3500,21300,55000,12000]
color_list = ["Siyah","Mavi","Beyaz","Sarı","Kırmızı"]
status_list = ["Sıfır","İkinci El"]
traction_list = ["Manuel","Yarı Otomatik","Otomatik"]


class Vehicle():
    def __init__(self,model,kilometer,color,status,traction):
        self.model = model
        self.kilometer = kilometer
        self.color = color
        self.status = status
        self.traction = traction

class Car(Vehicle):
    def __init__(self,model,kilometer,color,status,traction,car_type):
        super().__init__(model,kilometer,color,status,traction)
        self.car_type = car_type
    def ViewCars(self):
         print("Model="+self.model+"\nKm="+str(self.kilometer)+"\nRenk="+self.color+"\nDurumu="+
              self.status+"\nVites="+self.traction+"\nTipi="+self.car_type+"\n")

class Motorcycles(Vehicle):
    def __init__(self,model,kilometer,color,status,traction,num_cylinders):
        super().__init__(model,kilometer,color,status,traction)
        self.num_cylinders = num_cylinders
    def ViewMotors(self):
        print("Model="+self.model+"\nKm="+str(self.kilometer)+"\nRenk="+self.color+"\nDurumu="+
             self.status+"\nVites="+self.traction+"\nSilindir="+self.num_cylinders+"\n")
        

cars = []
motors = []
for i in range(5):
    new_car =  Car(choice(car_list[0]),choice(km_list),choice(color_list),choice(status_list),choice(traction_list),choice(car_list[1]))
    new_motor = Motorcycles(choice(mot_list[0]),choice(km_list),choice(color_list),choice(status_list),choice(traction_list),choice(mot_list[1]))
    cars.append(new_car)
    motors.append(new_motor)
    
print("(1) --> Tüm Araçları Göster.\n(2) --> Arabaları Göster.\n(3) --> Motosikletleri Göster.\n(4) --> Çık.")
while(True):
    select = int(input("Yapmak istediğiniz işlemi seçiniz:"))
    if(select>=1 and select<=4):
        if(select == 1):
           print("      <---Araç Listesi--->     \n")
           counter = 0
           for i in range(5):
               counter += 1
               print("("+str(counter)+")")
               cars[i].ViewCars()
               counter += 1
               print("("+str(counter)+")")
               motors[i].ViewMotors()
        elif(select == 2):
           print("      <---Araba Listesi--->     \n")
           for i in range(5):
               print("("+str(i+1)+")")
               cars[i].ViewCars()
        elif(select == 3):
           print("      <---Motosiklet Listesi--->     \n")
           for i in range(5):
               print("("+str(i+1)+")")
               motors[i].ViewMotors()
        else:
            break
    else:
        print("1 ve 3 arasında bir değer giriniz!")



