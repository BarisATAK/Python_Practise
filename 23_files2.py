# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 22:07:48 2020

@author: atakb
"""
"""
insert()
writelines()
"""

#The multiplication table
with open("ExampleFile2.txt","w") as file:
    for i in range(10,21):
        for j in range(10,21):
            file.write(str(j) + " * " + str(i) + " = " + str(i*j))
            file.write("     ")
        file.write("\n")
        
with open("ExampleFile2.txt","a") as file2: #append mode
    file2.write("\n")
    for i in range(21,31):
        for j in range(21,31):
              file2.write(str(j) + " * " + str(i) + " = " + str(i*j))
              file2.write("     ")
        file2.write("\n")
        
#Append a data top of the file.
with open("ExampleFile2.txt","r+") as file3: #r+ --> to write and read
    data = file3.read()
    file3.seek(0)
    data = "<---The multiplication table--->\n\n" + data
    file3.write(data)
    
list1 = [1,2,3,4,5]
list1.insert(2,65) #Insert 65 to second index.
print(list1)

#Append a data middle of the file.
with open("ExampleFile2.txt","r+") as file4:
    data = file4.readlines() #Return the all lines as a list.
    line_count = len(data)
    line_count = int(line_count/2+1)
    data.insert(line_count, "10's digit is over")
    file4.seek(0)
    file4.writelines(data)
