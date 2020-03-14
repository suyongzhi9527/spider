import time
from selenium import webdriver

driver = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe')
driver.get("http://www.baidu.com")
driver.execute_script('window.open()')
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.taobao.com")
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
driver.get("https://python.org")
