from selenium import webdriver

driver_path = r"F:\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get("http://www.baidu.com")

print(driver.page_source)
