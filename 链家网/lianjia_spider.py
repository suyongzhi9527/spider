import requests
from bs4 import BeautifulSoup

url = 'https://gz.lianjia.com/ershoufang/pg/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

resp = requests.get(url, headers=headers)

# print(resp.text) 网页内容，文本格式
# print(resp.content.decode())  # 网页内容，二进制格式
html_str = resp.content.decode()
soup = BeautifulSoup(html_str, 'lxml') # html.parse
# print(soup)
ul_list = soup.find('ul',{'class':'sellListContent'}).find_all('li')
# print(ul_list)

for li in ul_list:
    name = li.find('div',{'class':'title'}).find('a').get_text()
    print(name)
    price = li.find('div',{'class':'totalPrice'}).find('span').get_text()
    print(price+'万')
    position = li.find('div',{'class':'positionInfo'}).find_all('a')
    for i in position:
        # print(i.string)
        position = i.string
        print(position)
    # print(position)
    address = li.find('div',{'class':'houseInfo'}).get_text()
    print(address)
    print('*'*10)
    with open('lianjia.csv','a',encoding='GBK',newline="") as f:
        f.write('{},{}万,{},{}\n'.format(name,price,position,address))