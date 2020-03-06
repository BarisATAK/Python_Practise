# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 01:02:02 2020

@author: atakb
"""
import sqlite3, random, time, datetime

con = sqlite3.connect("Date_Database.db")
cursor = con.cursor() #To execute the sql commands

def CreateTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS DateTable (Zaman REAL, Tarih TEXT, Anahtar_Kelime TEXT, Deger REAL)")
    
def InsertRandomValue():
    t = time.time() #Current time
    current_time = str(datetime.datetime.fromtimestamp(t).strftime('%H:%M:%S'))  
    current_date = str(datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')) #Current date
    keyword = "Eklendi"
    value = random.randrange(1,10)
    cursor.execute("INSERT INTO DateTable (Zaman, Tarih, Anahtar_Kelime, Deger) VALUES (?,?,?,?)", (current_time, current_date, keyword, value))
    con.commit()

def SelectValues(col_val, selec_value):
    cursor.execute("SELECT * FROM DateTable WHERE {} = {}".format(col_val, selec_value))
    data = cursor.fetchall() #Sign to a list
    print(data)

def Update():
    cursor.execute("UPDATE DateTable SET Deger = 3 WHERE Deger = 80")
    data = cursor.execute("SELECT * FROM DateTable")
    for i in data:
        print(i)
    print("---------------Silinince----------------")
    cursor.execute("DELETE FROM DateTable WHERE Deger = 99")
    data = cursor.execute("SELECT * FROM DateTable")
    con.commit()
    for i in data:
        print(i)
    
CreateTable()
#for i in range(10):
#    InsertRandomValue()
#    time.sleep(1) #Wait 1 second to update the time.
while True:
    ques = input("Tablodan değer çekmek istiyor musunuz?(E/H):")
    if(ques == 'E'): 
        col_value = input("Görmek istediğiniz sütun adını girin:")  
        sel_value = input("Görmek istediğiniz koşulu girin:")
        SelectValues(col_value, sel_value)
    elif(ques == 'H'):
        print("Hoşçakalın...")
        break
    else:
        print("E veya H giriniz!!!")
Update()
con.close()