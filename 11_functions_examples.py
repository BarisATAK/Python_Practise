# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 01:24:34 2020

@author: atakb
"""

# Factorial Function.
def Factorial(number):
    for i in range(1,number):
        number *= i
    return number
  
# Fibonacci Function.
def Fibonacci(number):
    f1 = 0
    f2 = 1
    print(f1+f2)
    for i in range(0,number):
        fib = f1 + f2
        if(fib < number):
            print(fib)
            f1 = f2
            f2 = fib

#a*(x^2)+b*(x)+c
def FindRoots(a,b,c):
    discriminant = b*b-4*a*c
    if(discriminant<0):
        print("Reel kök bulunamadı")
        return
    else:
        x1 = (-b+discriminant**0.5)/(2*a)
        x2 = (-b-discriminant**0.5)/(2*a)
        return (x1,x2)
    
    
#fact
fact_number = int(input("Faktoriyeli hesaplanacak sayı :"))
print(str(fact_number) + "! =", Factorial(fact_number))

#fibon
fibon_number = int(input("Kaça kadar fibonacci sayıları yazılacağını belirt :"))
Fibonacci(fibon_number)

#root
a,b,c = input("Denklemin a,b ve c değerlerini giriniz:").split()
a,b,c = int(a),int(b),int(c)
print("Denklemin kökü =", FindRoots(a,b,c))
