import requests
import re
import time
import pymysql
import threading
from queue import Queue
from lxml import etree
from selenium import webdriver


def test():
    url = "http://www.dianping.com/shop/121937518"
    driver = webdriver.Chrome("E:\chromedriver_win32\chromedriver.exe")
    driver.get(url)
    time.sleep(10)
    driver.close()


if __name__ == '__main__':
    test()
