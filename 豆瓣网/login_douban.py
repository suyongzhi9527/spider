from selenium import webdriver
import time

# 实例化driver
driver = webdriver.Chrome(r'F:\chromedriver.exe')
driver.get("https://www.douban.com/")
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to_frame(iframe)
driver.find_element_by_class_name("account-tab-account").click()

driver.find_element_by_id("username").send_keys("784542623@qq.com")
driver.find_element_by_id("password").send_keys("zhoudawei123")

time.sleep(2)
driver.find_element_by_class_name("btn-active").click()

# 获取cookie
cookies = {i["name"]: i["value"] for i in driver.get_cookies()}
print(cookies)

time.sleep(3)
driver.quit()
