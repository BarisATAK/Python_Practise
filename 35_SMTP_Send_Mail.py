# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 01:27:00 2020

@author: atakb
"""
import smtplib

content = "SMTP MAIL GÖNDERME!"
mail = smtplib.SMTP("smtp.gmail.com",587) #GMAİL PORT --> 587
mail.ehlo()
mail.starttls() #Encypts the user name and password.
mail.login("XXXXXXX@gmail.com","asddf2343432")#User name, password
mail.sendmail("XXXXXXX@gmail.com","YYYYYY@gmail.com",content)#Sender, Receiver, message.