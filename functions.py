from selenium import webdriver

def startSearch():

	PATH = "C:\Program Files (x86)\chromedriver.exe"
	mainurl = "https://www.shpock.com/"
	language = "de-de" #available de-at, en-gb
	keyword = "nintendo 64"
	distance = "1000"
	url = mainurl + language + "/results?q=" + keyword + "&location.distance=1000&location.isDomestic=true&sort=d%3Adate_start"
	setUpConnection(PATH,url)

def setUpConnection(path,url):
	driver = webdriver.Chrome(path)
	driver.get(url)
	driver.implicitly_wait(5)
	getTitles(driver)

def getTitles(driver):
	titles = []
	itemcards = driver.find_elements_by_class_name("ffXkEX")
	for itemcard in itemcards:
		hrefs = itemcard.find_elements_by_class_name("kvbvf")
		for href in hrefs:
			containers = href.find_elements_by_class_name("joQnVa")
			for container in containers:
				cards = container.find_elements_by_class_name("hpjVjR")
				for card in cards:
					datas = card.find_elements_by_class_name("kbnIAg")
					for data in datas:
						titles.append(data.find_element_by_class_name("kjCAzp").get_attribute("innerHTML"))	
	printTitle(titles)

def printTitle(titles):
	for title in titles:
		print(title)