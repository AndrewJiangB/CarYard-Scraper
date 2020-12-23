import atScraper
import dbconn

url= 'https://www.autotrader.ca/cars/?rcp=0&rcs=0&prx=100&hprc=True&wcp=True&sts=New-Used&inMarket=basicSearch&loc=l5l1c6'
page = atScraper.getRequest(url)

dbCars = dbconn.getCars()
print(dbCars)