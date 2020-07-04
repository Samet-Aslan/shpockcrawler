# Shpock Crawler Tutorial 1.0
# Samet Aslan 2020
from selenium import webdriver

#Variables
PATH = "C:\Program Files (x86)\chromedriver.exe"
mainurl = "https://www.shpock.com/"
language = "de-de" #available de-at, en-gb
keyword = "nintendo"
distance = "1000"
url = mainurl + language + "/results?q=" + keyword + "&location.distance=1000&location.isDomestic=true&sort=d%3Adate_start"

#Setting up the driver
driver = webdriver.Chrome(PATH)
driver.get(url)
 
driver.implicitly_wait(5)

#printing links of recent listings
items = driver.find_elements_by_class_name("ffXkEX")
titles = driver.find_elements_by_class_name("kjCAzp")
prices = driver.find_elements_by_class_name("gSgzGm")
descriptions = driver.find_elements_by_class_name("bqTBXL")

for item in items:
	links = item.find_elements_by_tag_name("a")
	for link in links:
		print(link.get_attribute("href"))