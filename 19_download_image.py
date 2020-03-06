# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 04:38:00 2020

@author: atakb
"""
from urllib import request as download

url1 = "https://upload.wikimedia.org/wikipedia/commons/c/c9/Moon.jpg"
url2 = "http://www.ottophoto.com/kirlian/kirlian_1/kirlian01.jpg"
url3 = "http://www.ottophoto.com/kirlian/kirlian_1/kirlian16.jpg"
url4 = "https://upload.wikimedia.org/wikipedia/commons/2/2a/Junonia_lemonias_DSF_upper_by_Kadavoor.JPG"
url5 = "https://bellard.org/bpg/lena5.jpg"

imageList = [url1,url2,url3,url4,url5]
imageCounter = 1
print("Resimler indiriliyor...")

for i in imageList:
    download.urlretrieve(i,"Images/Image" + str(imageCounter) + ".jpg")
    imageCounter += 1
