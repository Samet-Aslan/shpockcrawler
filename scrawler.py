# Shpock Crawler Tutorial 1.0
# Samet Aslan 2020
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
keyword = "nintendo"
url = "https://www.shpock.com/de-de/results?q=" + keyword + "&location.distance=1000&location.isDomestic=true&sort=d%3Adate_start"
driver.get(url)
 
#Test: get the first img of results
#imagewrapper = driver.find_element_by_xpath("//*[@id='__next']/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div[1]/a/div/div/div[1]")
#image = imagewrapper.find_element_by_tag_name("img").get_attribute("src")
#print(image)

#class="CardGrid-sc-1l8yw3u-0 fuVpoX"

#get the results wrapper
xresult = "//*[@id='__next']/div[2]/div[3]/div[2]/div[1]/div/div/div[3]"
results = driver.find_element_by_xpath(xresult)

