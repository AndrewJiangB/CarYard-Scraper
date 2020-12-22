from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("C:/Users/andre/Documents/Projects/Chimken-Stonk/chromedriver.exe")
driver.get("https://www.autotrader.ca/")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
