import requests
from bs4 import BeautifulSoup


class QuNaEr(object):
    def __init__(self, keyword, page):
        self.keyword = keyword
        self.page = page

    def run(self):
        url = 'https://piao.qunar.com/ticket/list.htm?keyword=%s&page=%s' % (self.keyword, self.page)
        response = requests.get(url)
        response.encoding = 'utf-8'
        text = response.text
        soup = BeautifulSoup(text, 'html.parser')

        arr = soup.find('div', class_='result_list').contents
        for i in arr:
            item = {}
            info = i.attrs
            # 景区名称
            name = info.get('data-sight-name')
            # 地址
            address = info.get('data-address')
            # 近期售票数
            count = info.get('data-sale-count')
            # 经纬度
            point = info.get('data-point')

            # 起始价格
            price = i.find('span', {'class': 'sight_item_price'})
            if type(price) == 'NoneType' or price == None:
                continue
            price = price.find_all('em')

            item['name'] = name
            item['adderss'] = address
            item['count'] = count
            item['point'] = point
            item['price'] = price[0].text

            if item['price'] == '':
                item['price'] = '免费'
            print(item)


if __name__ == '__main__':
    citys = ['北京', '上海', '成都', '三亚', '广州', '重庆', '深圳',
             '西安', '杭州', '厦门', '武汉', '大连', '苏州']
    for i in citys:
        for page in range(1, 5):
            qne = QuNaEr(i, page)
            qne.run()
