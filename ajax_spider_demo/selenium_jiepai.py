import time
import os
from urllib import request
from selenium import webdriver
from lxml import etree


class JinRiSpider(object):
    driver_path = r'F:\chromedriver_win32\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=JinRiSpider.driver_path)
        self.url = 'https://www.toutiao.com/'
        self.postions = []

    def run(self):
        self.driver.get(self.url)
        tt_input = self.driver.find_element_by_class_name('tt-input__inner')
        tt_input.send_keys('街拍')
        tt_button = self.driver.find_element_by_class_name('tt-button')
        tt_button.click()
        self.driver.switch_to.window(self.driver.window_handles[1])  # 切换到新的页面
        source = self.driver.page_source
        self.parse_list_page(source)

    def parse_list_page(self, source):
        html = etree.HTML(source)
        detail_url = html.xpath('//div[contains(@class, "rbox")]//div[@class="title-box"]/a/@href')
        # print(detail_url)
        for url in detail_url:
            # print(url)
            self.request_detail_page(url)  # 请求详情页
            time.sleep(1)

    def request_detail_page(self, url):
        self.driver.execute_script("window.open('%s')" % url)  # 打开新的页面
        self.driver.switch_to.window(self.driver.window_handles[2])  # 切换到新的页面
        source = self.driver.page_source  # 获取详情页的源代码
        self.parse_detail_page(source)  # 解析详情页
        self.driver.close()  # 关闭当前页面详情页
        self.driver.switch_to.window(self.driver.window_handles[1])  # 切换回第一页

    def parse_detail_page(self, source):
        image_path = os.path.join(os.getcwd(), 'image')
        if not os.path.exists(image_path):
            os.mkdir(image_path)
        html = etree.HTML(source)
        img_url = html.xpath('//div[@class="pgc-img"]/img/@src')
        for img in img_url:
            print(img)
            img_name = img[-5:]
            request.urlretrieve(img, 'image/%s.jpg' % img_name)


if __name__ == '__main__':
    spider = JinRiSpider()
    spider.run()
