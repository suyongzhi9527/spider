from selenium import webdriver
import time

"""
selenium使用的注意点
1.获取文本和属性
    1.1先定位到元素，然后调用'.text'或者'.get_attribute("href")'方法来获取
2.selenium获取的页面数据是浏览器中elements的内容
3.find_element和find_elemens的区别
    3.1find_element返回的是一个element,如果没有会报错
    3.2find_elemens返回的是一个列表，没有就是空列表
    3.3正在判断是否有下一页的时候，使用find_elements来根据结果的列表长度判断
4.如果页面中含有iframe、frame需要先用'.switch_to.frame方法切换到frame中才能定位元素'
5.selenium请求第一页的时候会等待页面加载完成后再获取数据，但是在点击翻页之后，会直接获取数据，
可能会报错，因为数据还没加载出来，需要'time.sleep(3)'
"""

caps = webdriver.DesiredCapabilities.FIREFOX
caps['marionette'] = False
# 实例化driver
driver = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe')
driver.get('https://www.airbnb.cn/s/Shenzhen--China/all?page=1')

data_list = driver.find_elements_by_css_selector('div._p62vg1')
for data in data_list:
    print(data.text)

# driver.get("https://dianping.com/search/category/7/10/p1")
# titles = driver.find_elements_by_css_selector('div.view-content')
# for title in titles:
#     print(title.text)

# ret1 = driver.find_elements_by_xpath("//article[@class='post']//h1")
# # print(ret1)
# for h1 in ret1:
#     print(h1.find_element_by_xpath("./a").get_attribute("href"))

time.sleep(2)

# driver.quit()  # 退出整个浏览器
# driver.close()  # 关闭当前页面