import requests
import time
from bs4 import BeautifulSoup
from pymongo import MongoClient
client=MongoClient()
client=MongoClient('localhost', 27017)
db=client.starttracker

url = "https://iitr.ac.in/Departments/Electrical%20Engineering%20Department/People/Faculty/index.html"
    #    https://iitr.ac.in/Departments/Mechanical%20and%20Industrial%20Engineering%20Department/People/Faculty/index.html
r=requests.get(url)
# time.sleep(10)
# htmlContent=r.content
# time.sleep(10)
# print(htmlContent)
soup=BeautifulSoup(r.text, "lxml")
# time.sleep(10)
# print(soup)
# title=soup.title
# print(type(title))
ui_faculty_card=soup.find_all("div", class_="ui faculty-card")
# time.sleep(10)

# time.sleep(5)
# print(len(ui_faculty_card))
for i in range(len(ui_faculty_card)):
    x=ui_faculty_card[i]
    data={
        "name": x.find("div", class_="ui intro-text").text.replace('\t', ''). replace('\n', ''),
        "designation": x.find("div", class_="designation").text.replace('\t', ''). replace('\n', ''),
        "mail id": x.find_all("div", class_="info-content")[0].find("div", class_="ui intro-text").text.replace('\t', ''). replace('\n', ''),
        "img": x.find("img").get('src'),
        "research interest": x.find("div", class_="ui description").text.replace('\t', ''). replace('\n', ''),
        "phone number":x.find_all("div", class_="info-content")[2].find("div", class_="ui intro-text").text.replace('\t', ''). replace('\n', '')
    }
    print(data)
# print(soup.find_all("div", class_="ui faculty-card")[10])
# ui_faculty_card=soup.find(class_="ui faculty-card")
# print(ui_faculty_card)


