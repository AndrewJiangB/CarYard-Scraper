from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import dbconn

def launchBrowser():
    driver = webdriver.Chrome("C:/Users/andre/Documents/Projects/Chimken-Stonk/chromedriver.exe")
    driver.get("https://www.autotrader.ca/")
    content = driver.page_source
    return content

def getRequest(URL):
    page = requests.get(URL)
    return page

def htmlParser(page):
    soup = BeautifulSoup(page.content, features="html.parser")
    results = soup.findAll("div", {"class": "listing-details"})
    print(results)