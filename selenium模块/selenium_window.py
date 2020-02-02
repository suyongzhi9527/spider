from selenium import webdriver


driver = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe')
driver.get("http://www.baidu.com")

driver.execute_script('window.open("https://www.douban.com/")')
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)
