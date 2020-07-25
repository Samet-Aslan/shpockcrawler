from selenium import webdriver
from Listing import Listing
import time 

def startSearch():
	print("Preparing search...")
	PATH = "C:\Program Files (x86)\chromedriver.exe"
	mainurl = "https://www.shpock.com/"
	language = "de-de" #available de-at, en-gb
	keyword = "nintendo 64"
	distance = "1000"
	url = mainurl + language + "/results?q=" + keyword + "&location.distance=1000&location.isDomestic=true&sort=d%3Adate_start"
	print("Preparing search finished")
	setUpConnection(PATH,url)

def setUpConnection(path,url):
	print("Setting up connection...")
	driver = webdriver.Chrome(path)
	driver.get(url)
	print("Setting up connection succesfull")
	createObjects(driver)

def createObjects(driver):
	print("Starting to fetch...")
	time.sleep(2)
	driver.execute_script("window.scrollTo(0, 1000);")
	time.sleep(2)
	my_listings = []
	itemcards = driver.find_elements_by_class_name("ffXkEX")

	for itemcard in itemcards:
		hrefs = itemcard.find_elements_by_class_name("kvbvf")

		for href in hrefs:
			containers = href.find_elements_by_class_name("joQnVa")
		
			for container in containers:
				cards = container.find_elements_by_class_name("hpjVjR")
		
				for card in cards:
					boxes = card.find_elements_by_class_name("dADjlv")
					prices = card.find_elements_by_class_name("kbnIAg")
			
					for price in prices:
						theprice = price.find_element_by_class_name("gSgzGm").get_attribute("innerHTML")
					for box in boxes:
						listings = box.find_elements_by_tag_name("img")
						for listing in listings:
							listingobject = Listing(listing.get_attribute("title"), theprice , listing.get_attribute("src"), listing.get_attribute("alt"))
							my_listings.append(listingobject)
	print("Fetch finished")
	print("Printing Objects...")
	printObjects(my_listings)

def printObjects(listitems):
	print("Printing items...")
	for item in listitems:
		print(item.getTitle())
		print(item.getPrice())
		print(item.getImgsrc())
		print(item.getDescription())
	print("Printing items done")


