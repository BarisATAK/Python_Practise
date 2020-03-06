# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:32:25 2020

@author: atakb
"""

def CalculateAvarage(f_exam, l_exam):
    f_exam *= 0.3
    l_exam *= 0.7
    avarage = f_exam + l_exam
    return avarage

def isPassed(avarage):
    if avarage >= 50:
        return "Geçtiniz"
    else:
        return "Kaldınız"
    
def TriangleArea(high, base_width):
    area = high * base_width / 2
    return area

def FactorOf15(number):
    for i in range(3*5, number):
        if(i % 15 == 0):
            print(str(i) + " ")

def StepCount(number):
    step = 0
    while True:
        step += 1
        if(int(number / 10) == 0):
            return step
        number /= 10

def WriteTheSteps(number):
    while(int(number) != 0):
       print(str(int(number) % 10)) 
       number = int(number) / 10


    
"""1
f_exam = float(input("Vize notunuzu giriniz:"))
l_exam = float(input("Final notunuzu giriniz:"))
avarage = CalculateAvarage(f_exam, l_exam)
print("Ortalamanız =", avarage)
print("Durumunuz =", isPassed(avarage))
"""
"""2
high = float(input("Üçgenin yüksekliğini giriniz:"))
base_width = float(input("Üçgenin taban uzunluğunu giriniz:"))
print("Üçgenin alanı =", TriangleArea(high, base_width))
"""
"""3
number = int(input("3 ve 5'e bölünenlerin bulmak için değer giriniz:"))
FactorOf15(number)
"""
"""4
number = int(input("Basamak sayısı hesaplanacak sayıyı giriniz:"))
print(str(number) + " sayısı " + str(StepCount(number)) + " basamaklıdır.")
"""
number = int(input("Basamakları yazdırılacak sayıyı giriniz:"))
WriteTheSteps(number)




