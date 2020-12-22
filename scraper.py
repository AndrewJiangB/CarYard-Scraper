from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import dbconn

#driver = webdriver.Chrome("C:/Users/andre/Documents/Projects/Chimken-Stonk/chromedriver.exe")
#driver.get("https://www.autotrader.ca/")
#content = driver.page_source

URL = 'https://www.autotrader.ca/cars/?rcp=0&rcs=0&prx=100&hprc=True&wcp=True&sts=New-Used&inMarket=basicSearch&loc=l5l1c6'
page = requests.get(URL)

soup = BeautifulSoup(page.content, features="html.parser")
results = soup.findAll("div", {"class": "listing-details"})
#print(results)

dbCars = dbconn.getCars()
print(dbCars)