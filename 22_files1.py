# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:56:22 2020

@author: atakb
"""
"""
read()
readLine()
readLines()
seek()
"""

try:
    file = open("C:/Users/atakb/OneDrive/Desktop/Personal Information.txt","r")
except FileNotFoundError:
    print("1. Dosya Bulunamadı!!!")
    
try:
    file = open("Personal Information.txt","r")
    #print(file.read()) #read all of file
    #print(file.readline()) #read line
    #print(file.readlines()) #read as list
    select = file.readlines()
    print(select[2]) # writes the 3. line
except FileNotFoundError:
    print("2. Dosya bulunamadı!!!")
finally:
    file.close()
    
with open("Personal Information.txt","r") as file1: #automatically closes the file 
    print(file1.read())
    
with open("exampleFile.txt","r") as file:
    file.seek(11) #It searches up to the 11th character and performs it after finding it.
    print(file.read(95)) #it reads 95 character
    file.seek(2) #Start from the beginning of the file.
    print(file.read())
