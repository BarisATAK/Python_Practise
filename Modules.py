# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 02:49:24 2020

@author: atakb
"""

def Dictionary(word):
    dict = {"sirayet":"(hastalık için) başkalarına geçme, bulaşma.",
            "barış":"barışmak eylemi.",
            "havale":"bir işin görülmesini, yapılmasını vb. bir başkasına yükleme, onun sorumluluğuna bırakma.",
            "galaksi":"gökada",
            "fent":"düzen, hile",
            "terim":"bir bilim, sanat, meslek dalıyla ya da bir konuyla ilgili özel ve belirli bir kavramı olan sözcük.",
            "yargı":"kişinin, bir şey konusunda olumlu ya da olumsuz düşünce söylemesi."}
    
    
    for i,j in dict.items():
        if(i == word):
            return j
        
def CalculateSquare(number):
    return number ** 2

def RootOfSquare(number):
    return number ** 0.5