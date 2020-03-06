import requests
from bs4 import BeautifulSoup
import time

##Pulling and Process the data from internet with Requests and BeatifulSoup.
# requests -- > HTTP module

r = requests.get("https://www.tripadvisor.com.tr/Attractions-g298656-Activities-Ankara.html")
print(r.status_code,"\n\n")
#print(r.content)
time.sleep(2)
soup = BeautifulSoup(r.content)
print(soup.prettify()) #edit to page

#print(soup.find_all("a"))#a href --> link tag

links = soup.find_all("a")
#for i in links:
#    print(i)
    
print("\n\n Link Sayısı = ",len(links))

for i in links: #Real links
    print(i.get("href"))

for i in links:
    print(i.text) #Texts of the links.
    
for i in links:
    print(i.text + " --> " + str(i.get("href")))