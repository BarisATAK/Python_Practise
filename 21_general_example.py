# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 15:16:33 2020

@author: atakb
"""

#finally kısmı --> Hata verse de vermese de son işlem burda yapılır...
"""
try:
    file = open("dosya.txt","r")
except IOError:
    print("Dosya bulunamadı!")
finally: #Dosya açılsa da açılmasa da dosyayı kapatmamız lazım.
    file.close()
"""
# modes ==> "w" -> write, "r" -> read, "a" -> append
"""
file = open("file1.txt","w") #open and write to file.
file.write("asdasda")
file.close()

file = open("file1.txt","a") #open and write to file.
file.write("hello")
file.close()

file = open("file1.txt","r")
print(file.read())
"""

def WriteToFile(personal_dictionary):
    write_file = open("Personal Information.txt","w")
    for i,j in personal_dictionary.items():
        write_file.write(i + " = " +  j + "\n")
    write_file.close()

def ReadFromFile():
    read_file = open("Personal Information.txt","r")
    print(read_file.read())

print("Veritabanına kaydolmak için kişisel bilgilerinizi giriniz.")
name = input("Adınızı giriniz:")
l_name = input("Soyadınızı giriniz:")
sex = input("Cinsiyetinizi giriniz:")
age = input("Yaşınızı giriniz:")
country = input("Yaşadığınız ülkeyi giriniz:")

personal_dictionary = {"İsim " : name,
                       "Soyad " : l_name,
                       "Cinsiyet " : sex,
                       "Yaş " : age,
                       "Ülke " : country}

WriteToFile(personal_dictionary)

print("Bilgileriniz veritabanına kaydedildi...\n")

ReadFromFile()

update_text = "Güncellemek istediğiniz bilgi var mı?(E/H) : "
bye = "Hoşçakalın..." 
while True:
    update = input(update_text)
    if(update == "H" or update == "h"):
        break
    elif(update == "E" or update == "e"): #or update != "H" or update != "h"):
        counter = 1
        for i in personal_dictionary:
            print(str(counter) + " --> " + i + "\n")
            counter +=1
        try:
            update_value = int(input("Güncellemek istediğiniz verinin numarasını girin:"))            
            counter = 1
            for i in personal_dictionary:
                if(counter == update_value):
                   new_value = input("{} : ".format(i)) 
                   personal_dictionary[i] = new_value                 
                   write_file = open("Personal Information.txt","w")
                   WriteToFile(personal_dictionary)
                   print("Bilgileriniz güncellenmiştir...")
                   break
                counter += 1
            if(update_value < 1 or update_value > 5):
                print("1 ve 5 arası değer giriniz!")
            else:
                break
        except ValueError:
            print("RAKAM Giriniz!")
    else:
        print("Yanlış değer girdiniz E veya H giriniz...")

print("\n")
for i,j in personal_dictionary.items():
    print(i + " = " + j + "\n")

print(bye)

