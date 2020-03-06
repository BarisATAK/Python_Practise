# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 01:47:24 2020

@author: atakb
"""

class Student():
    def __init__(self):
        print("Öğrenci sınıfının yapıcı fonk.")
        
    def Study(self):
        print("Öğrenci şuan da ders çalışıyor.")

class Employee():
    def __init__(self):
        print("Personel sınıfının yapıcı fonk.")
        
    def Work(self):
        print("Personel şuan da çalışıyor.")
        
class Programmer(Employee,Student): #İlk parametrede belirtilen sınıfın yapıcı fonk. çağırır.
    pass
        
programmer = Programmer()
#programmer.Study()
#programmer.Work()