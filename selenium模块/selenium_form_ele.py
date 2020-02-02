from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# 实例化driver
driver = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe')
# driver.get("http://www.baidu.com")

# 常见的表单元素：input type='text/password/email/number'
# button,input[type='submit']
# checkbox:input[type='checkbox']
# select:下拉列表

# 操作输入框
# inputTag = driver.find_element_by_id('kw')
# inputTag.send_keys('你好')
#
# time.sleep(3)
# inputTag.clear()

# 操作checkbox
# driver.get("https://accounts.douban.com/passport/login?source=movie")
# checkboxTag = driver.find_element_by_name('remember')
# time.sleep(3)
# checkboxTag.click()

# 操作select
# driver.get('http://www.dobai.cn')
# # 选中这个标签，然后使用Select创建对象
# selectBtn = Select(driver.find_element_by_name('jumpMenu'))
# # 根据索引选择
# # selectBtn.select_by_index(1)
# # 根据值选择
# # selectBtn.select_by_value('xxx')
# # 根据可视的文本选择
# selectBtn.select_by_visible_text('xxx')
# # 取消选中的所有选项
# selectBtn.deselect_all()

# 操作按钮
driver.get('http://www.baidu.com')
inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('武汉肺炎')

submitTag = driver.find_element_by_id('su')
submitTag.click()
