from selenium import webdriver

# 实例化driver
driver = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe')
driver.get("http://www.baidu.com")

# 定位元素
# inputTag = driver.find_element_by_id("kw")
# inputTag = driver.find_element_by_name("wd")
# inputTag = driver.find_element_by_class_name("s_ipt")
inputTag = driver.find_element_by_css_selector(".s_ipt")
inputTag.send_keys("武汉肺炎")

# 1.如果只是想要解析网页中的数据，那么推荐将网页源代码给lxml来解析，因为lxml底层使用的是C语言，所以解析效率会更高。
# 2.如果是想要对元素进行一些操作，比如给一个文本框输入值，或者是点击某个按钮，那么久必须使用selenium给我们的提供的查找元素的方法。
