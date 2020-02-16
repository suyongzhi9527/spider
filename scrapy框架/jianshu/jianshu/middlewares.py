# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import time
from scrapy import signals
from selenium import webdriver
from scrapy.http.response.html import HtmlResponse


class SeleniumDowmloadMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'F:\chromedriver_win32\chromedriver.exe')

    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(1)
        try:
            while True:
                show_more = self.driver.find_element_by_class_name('H7E3vT')
                show_more.click()
                time.sleep(0.3)
                if not show_more:
                    break
        except:
            pass
        source = self.driver.page_source
        response = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding='utf-8')
        return response
