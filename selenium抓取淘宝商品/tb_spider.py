from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from pyquery import PyQuery as pq

import pymysql

browser = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe')  # 构造一个webdriver对象
wait = WebDriverWait(browser, 10)  # 指定等待条件
# KEYWORD = 'ipad'  # 指定关键词

db = pymysql.connect('localhost', 'root', '123456', 'tb_product')
cursor = db.cursor()


def index_page(page, KEYWORD):
    """
    抓取索引页
    :page 页码
    """
    print('正在抓取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        cookie = browser.get_cookies()[0]
        browser.add_cookie(cookie_dict=cookie)
        if page > 1:
            # 翻页操作
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input'))
            )
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit'))
            )
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page))
        )
        # 等待商品信息加载出来
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item'))
        )
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    解析商品数据
    """
    html = browser.page_source  # 获取源代码
    doc = pq(html)  # 构造PyQuery解析对象
    items = doc('#mainsrp-itemlist .items .item').items()  # 提取商品列表
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),  # 商品图片
            'price': item.find('.price').text(),  # 价格
            'deal': item.find('.deal-cnt').text(),  # 成交量
            'title': item.find('.title').text(),  # 名称
            'shop': item.find('.shop').text(),  # 店铺
            'location': item.find('.location').text()  # 店铺所在地
        }
        print(product)
        save_mysql(product)


def save_mysql(result):
    cursor = db.cursor()
    sql = 'insert into `product` (`image`,`price`,`deal`,`title`,`shop`,`location`) values ("{}","{}","{}","{}","{}","{}")'
    sql = sql.format(result['image'], result['price'], result['deal'], result['title'], result['shop'],
                     result['location'])
    cursor.execute(sql)
    db.commit()


MAX_PAGE = 100


def main():
    """
    遍历每一页
    """
    KEYWORD = input("请输入关键词: ")
    for i in range(1, MAX_PAGE + 1):
        index_page(i, KEYWORD)


if __name__ == '__main__':
    main()
