from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

driver = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe')
try:
    driver.get("https://www.baidu.com")
except TimeoutException:
    print("Time Out")

try:
    driver.find_element_by_id("hello")
except NoSuchElementException:
    print("No Element")
finally:
    driver.close()
