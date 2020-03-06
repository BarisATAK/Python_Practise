# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 23:38:50 2020

@author: atakb
"""


import requests
import operator
from bs4 import BeautifulSoup

url = "https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w"
url = requests.get(url)
soup = BeautifulSoup(url.content,"html.parser")

def CreateDictionary(wordsWithoutSymbols):
    wordCount = {} # Dictionary
    for word in wordsWithoutSymbols:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    return wordCount
    
    
def PullTheAllWords():
    allWords = []
    for paragraph in soup.find_all("p"):
        allText = paragraph.text
        lowerCase = allText.lower().split() #split returns a list.
        #print(lowerCase)
        
        for word in lowerCase:
            allWords.append(word)
            #print(word)
    return allWords

def CleanTheSymbols(allWords):
    wordsWithoutSymbols = []
    allSymbols = "!@$%^*()|_+{}[]?<>,./\":\'`;-=+&^£" + chr(775)
    for word in allWords:
        for symbol in allSymbols:
            if symbol in word:
                word = word.replace(symbol,"")
            
        if(len(word)>0):
            wordsWithoutSymbols.append(word)    
            #print(word)
    return wordsWithoutSymbols

allWords = PullTheAllWords()
wordsWithoutSymbols = CleanTheSymbols(allWords)
wordDictionary = CreateDictionary(wordsWithoutSymbols)

for value, count in sorted(wordDictionary.items(),key = operator.itemgetter(0)): # 0->value, 1->count
    print(value + " --> ",count)
    
""""
for word in wordDictionary:
    print(word + " --> ",wordDictionary[word])
"""        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
  
