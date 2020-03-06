# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 22:59:09 2020

@author: atakb
"""

import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w")

allWords = []

soup = BeautifulSoup(url.content,"html.parser")
#print(url.content)
#print(soup.prettify())
#print("***********************************************")

for paragraph in soup.find_all("p"):
    allText = paragraph.text
    lowerCase = allText.lower().split() #split returns a list.
    #print(lowerCase)
    
    for word in lowerCase:
        allWords.append(word)
        print(word)
    
print("**************")
print(len(allWords))

















    