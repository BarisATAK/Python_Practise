# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 00:43:15 2020

@author: atakb
"""

#Inheritance

class Employee():
    def __init__(self,name,salary,department):
        print("\nÇalışan sınıfının yapıcı fonksiyonu")
        self.name = name
        self.salary = salary
        self.department = department
    
    def ViewInfo(self):
        print("<--Çalışan Sınıfının Bilgileri-->")
        print("İsim = "+self.name+"\nMaaş = "+str(self.salary)+"\nDepartman = "+self.department)
        
    def IncreaseToSalary(self,amount):
        self.salary +=  amount
        print("Yeni maaş = "+str(self.salary))

    def DepartmentChanging(self,new_department):
        self.department = new_department
        print("Yeni departmant = "+self.department)
    
class Manager(Employee): #Inheritance
    #pass
    def __init__(self,name,salary,department,people_count): #Overriding
        print("\nYönetici sınıfının yapıcı fonksiyonu")
        super().__init__(name,salary,department) #Inherited from the upper class.
        self.people_count = people_count
    
    def ViewInfo(self):#Override
        print("<--Yönetici Sınıfının Bilgileri-->")
        print("İsim = "+self.name+"\nMaaş = "+str(self.salary)+"\nDepartman = "+self.department+"\nKişi Sayısı = "+str(self.people_count))

    def IncreasePeople(self,amount):
        self.people_count += amount
        print("Yeni kişi sayısı = "+str(self.people_count))
        

"""    
employee = Employee("Okan",3500,"İnsan Kaynakları")
employee.ViewInfo()
"""
manager = Manager("Barış",5000,"Bilgisayar Müh.",10)
manager.ViewInfo()
manager.IncreasePeople(20)
manager.ViewInfo()
