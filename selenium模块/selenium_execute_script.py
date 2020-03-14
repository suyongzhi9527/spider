from selenium import webdriver

driver = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe')
driver.get("https://www.zhihu.com/explore")
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
driver.execute_script('alert("到底了~~~")')
