# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 02:51:02 2020

@author: atakb
"""
a=10
def Function():
    global a # it changes the global variable.
    a = 5
    print(a) # local => 5
print(a) # local => 10
Function()
print(a) # we changed the a variable but our global variable is 10
