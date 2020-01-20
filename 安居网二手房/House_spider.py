import requests
import time
import json
from bs4 import BeautifulSoup

headers = {
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3945.117Safari / 537.36'
}

for i in range(1,2):
    link = 'https://beijing.anjuke.com/sale/p' + str(i)
    r = requests.get(link, headers=headers)
    print('现在抓取第{}页数据'.format(i))

    soup = BeautifulSoup(r.text, 'lxml')
    house_list = soup.find_all('li', class_='list-item')  # 房子全部信息
    houselists = []
    for house in house_list:
        house_item = {}
        house_item['房名'] = house.find('div', class_='house-title').a.text.strip()  # 房名
        house_item['价格'] = house.find('span', class_='price-det').text.strip()  # 价格
        house_item['每平方价格'] = house.find('span', class_='unit-price').text.strip()  # 每平方价格
        house_item['几室几厅'] = house.find('div', class_='details-item').text.strip()  # 几室几厅
        house_item['面积'] = house.find('div', class_='details-item').contents[3].text  # 面积
        house_item['层数'] = house.find('div', class_='details-item').contents[5].text  # 层数
        # house_item['年份'] = house.find('div', class_='details-item').contents[7].text if house.find('div', class_='details-item').contents[7].text == None else house.find('div', class_='details-item').contents[7].text  # 年份
        house_item['中介'] = house.find('span', class_='broker-name broker-text').text  # 房屋中介
        address = house.find('span', class_='comm-address').text.strip()  # 地址
        house_item['地址'] = address.replace('\xa0\xa0\n', '')  # 去除特殊字符和换行
        tag_list = house.find_all('span', class_='item-tags')
        house_item['标签'] = [i.text for i in tag_list]

        houselists.append(house_item)

with open('house.json','w',encoding='utf-8') as f:
    f.write(json.dumps(houselists,ensure_ascii=False,indent=2) +'\n')

