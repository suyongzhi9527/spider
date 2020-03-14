from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://101.4.136.34:80")

driver = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe', chrome_options=options)
# driver.get('http://httpbin.org/ip')
driver.get('https://www.taobao.com')
in_input = driver.find_elements_by_css_selector('.service-bd li')
print(in_input)
driver.close()