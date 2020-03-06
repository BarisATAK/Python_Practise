# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:47:56 2020

@author: atakb
"""
import requests
from bs4 import BeautifulSoup

imdbUrl = requests.get("https://www.imdb.com/chart/top/")
#print(r.content)

soup = BeautifulSoup(imdbUrl.content,"html.parser")
#print(soup)

data = soup.find_all("table",{"class":"chart full-width"})
#print(data)
#print("**********")
#print(len(data))
#print("\n\n\n"+"****************")
#print(data[0].contents)
#print(len(data[0].contents))

# tbody has the films name --> index number 5
filmTable = (data[0].contents)[len(data[0].contents)-2] ## 7 - 2
filmTable = filmTable.find_all("tr") #All film rows
print(len(filmTable))

for films in filmTable:
    filmTitles = films.find_all("td",{"class":"titleColumn"})
    print(filmTitles[0].text.replace("\n","")) # replace the \n with space character.
    print("***********************************************")







