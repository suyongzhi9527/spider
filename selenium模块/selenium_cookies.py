from selenium import webdriver

driver = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe')
driver.get("http://www.baidu.com")

for cooke in driver.get_cookies():  # 遍历打印cookies
    print(cooke)

print('*' * 30)
print(driver.get_cookie('PSTM'))  # 获取某个cookies信息

driver.delete_cookie('PSTM')  # 删除某个cooke
print('*' * 30)
# print(driver.get_cookie('PSTM'))  # 获取某个cookies信息
driver.delete_all_cookies()  # 删除所有cookes信息
