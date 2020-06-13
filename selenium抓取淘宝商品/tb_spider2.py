import time
from selenium import webdriver


def search_product(key):
    browser.find_element_by_id('q').send_keys(key)
    browser.find_element_by_class_name('btn-search').click()
    browser.maximize_window()  # 最大化浏览器窗口
    time.sleep(15)


def get_product():
    divs = browser.find_elements_by_class_name('item J_MouserOnverReq ')
    print(divs)
    for div in divs:
        info = div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text  # 商品名称
        price = div.find_element_by_xpath('.//strong').text + "元"  # 商品价格
        deal = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text  # 付款人数
        name = div.find_element_by_xpath('.//div[@class="shop"]/a').text  # 商家名称
        print(info, price, deal, name, sep='|')


def main():
    search_product(keyword)
    get_product()


if __name__ == '__main__':
    # keyword = input("请输入商品关键字: ")
    keyword = "U盘"
    browser = webdriver.Chrome(r'F:\chromedriver_win32\chromedriver.exe')  # 构造一个webdriver对象
    browser.get("http:www.taobao.com")
    main()
