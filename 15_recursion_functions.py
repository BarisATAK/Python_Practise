# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 00:16:49 2020

@author: atakb
"""

# Recursion Function
""""
return_1 => 1 + (array[2,3,4,5]) => 15 #1.indis 3 oldu
return_2 => 2 + (array[3,4,5]) => 14
return_3 => 3 + (array[4,5]) => 12
return_4 => 4 + (array[5]) => 9
return_5 => 5 + (array[] = 0) => 5
"""

def RecursiveSum(array):
    if(len(array) == 0):
        return 0
    else:
        return array[0] + RecursiveSum(array[1:])
    
# Fibonacci with recursion
# array = 1 1 2 3 5 8 13 21 34 55 89 ...
        
def RecursiveFibonacci(index):
    if(index <= 1):
        return index
    return RecursiveFibonacci(index - 1) + RecursiveFibonacci(index - 2)

# Factorial with recursion

def RecursiveFactorial(number):
    if(number == 1):
        return 1
    else:
        return number * RecursiveFactorial(number - 1)
    
    
print("Verilen dizinin toplamı =" + str(RecursiveSum([1,2,3,4,5])) + "\n")

index = int(input("Fibonacci dizisinde istenilen index değerini girin:"))
print("Fibonacci dizisinin " + str(index) + ". index değeri =" + str(RecursiveFibonacci(index)))

number = input("Faktoriyeli alınacak sayıyı giriniz:")
print(number + " sayısının faktoriyeli =" + str(RecursiveFactorial(int(number))))



