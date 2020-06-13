# 引入模块
import requests
import math
import re
from bs4 import BeautifulSoup



from headers import create_headers
from proxy_ip import create_proxy


class NewHouse(object):
    def __init__(self, xiaoqu, price, total):
        self.xiaoqu = xiaoqu
        self.price = price
        self.total = total

    def text(self):
        return self.xiaoqu + ", " + \
            self.price + ", " + \
            self.total


with open("newhouse.csv", "a", encoding="utf-8") as f:
    total_page = 1
    loupan_list = list()
    page = "http://bj.fang.ke.com/loupan/"
    headers = create_headers()
    response = requests.get(page, headers=headers,
                            proxies=create_proxy(), timeout=10)
    html = response.content
    # 解析返回html
    soup = BeautifulSoup(html, "lxml")

    # 获取总页数
    try:
        page_box = soup.find_all("div", class_="page-box")[0]
        matches = re.search(r'.*data-total-count="(\d+)".*', str(page_box))
        total_page = int(math.ceil(int(matches.group(1)) / 10))
    except Exception as e:
        print(e)

    print("总页数:" + str(total_page))

    for i in range(1, total_page + 1):
        page = "https://bj.fang.ke.com/loupan/pg{}".format(i)
        print(page)
        response = requests.get(page, headers=headers,
                                proxies=create_proxy(), timeout=10)
        html = response.content
        soup = BeautifulSoup(html, "lxml")

        # 获取小区信息
        house_elements = soup.find_all("li", class_="resblock-list")
        # 循环遍历获取想要的元素
        for house_elem in house_elements:
            price = house_elem.find("span", class_="number")  # 价格
            desc = house_elem.find("span", class_="desc")
            total = house_elem.find("div", class_="second")
            loupan = house_elem.find("a", class_="name")

            # 清洗数据
            try:
                price = price.text.strip() + desc.text.strip()
            except Exception as e:
                price = "0"

            loupan = loupan.text.replace("\n", "")

            try:
                total = total.text.strip().replace(u"总价", "")
                total = total.replace(u"/套起", "")
            except Exception as e:
                total = "0"

            # 作为对象保存到变量
            loupan = NewHouse(loupan, price, total)
            print(loupan.text())

            # 将新房信息加入列表
            loupan_list.append(loupan)

    for loupan in loupan_list:
        f.write(loupan.text() + "\n")
