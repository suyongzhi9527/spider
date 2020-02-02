from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://101.4.136.34:80")

driver = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe', chrome_options=options)
driver.get('http://httpbin.org/ip')
