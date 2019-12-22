from selenium import webdriver

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

# 实例化driver
driver = webdriver.Chrome(r'F:\chromedriver.exe')

driver.get("http://duanziwang.com/category/%E7%BB%8F%E5%85%B8%E6%AE%B5%E5%AD%90/")

# ret1 = driver.find_elements_by_xpath("//article[@class='post']//h1")
# # print(ret1)
# for h1 in ret1:
#     print(h1.find_element_by_xpath("./a").get_attribute("href"))

print(driver.find_element_by_link_text(">").get_attribute("href"))

driver.quit()