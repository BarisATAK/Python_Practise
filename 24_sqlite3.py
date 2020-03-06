# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:27:29 2020

@author: atakb
"""
#Install the https://sqlitebrowser.org/dl/ to open the database file.
import sqlite3

con = sqlite3.connect("StudentDatabase.db") #Create or connect a database.
cursor = con.cursor() #To execute sql commands.

def CreateTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS StudentInfo(Name TEXT,Last_Name TEXT, No INT, Grade INT)")
    
def InsertValue(name,l_name,s_number,grade):
    cursor.execute("INSERT INTO StudentInfo VALUES('{}','{}', {}, {})".format(name,l_name,s_number,grade))
    
CreateTable()  

print("<---Öğrenci Kayıt Sistemi--->")
while True:
    name = input("İsim = ")
    l_name = input("Soyad = ")
    s_number = int(input("Ögrenci Numarası = "))
    grade = int(input("Sınıf = "))
    InsertValue(name,l_name,s_number,grade)
    con.commit()
    print("Bilgileriniz başarıyla kaydedildi...")
    new_record = input("Yeni kayıt yapmak istiyor musunuz?(E/H):")
    if(new_record == 'H'):
        break
con.close()



