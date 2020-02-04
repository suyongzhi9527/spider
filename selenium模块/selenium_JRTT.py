from selenium import webdriver
import time

driver = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe')
driver.get("https://www.toutiao.com/ch/news_hot/")
time.sleep(2)

wcommonFeed = driver.find_element_by_xpath('//div[@class="wcommonFeed"]').find_elements_by_class_name('title')

for i in wcommonFeed:
    print(i.text)