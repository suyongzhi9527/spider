import requests
import csv
from lxml import etree


def parser(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        'Cookie': 'uuid=f032c884-c040-4f48-9d84-c33ae1840279; sessionid=2501670a-df82-46a8-f709-ef8b64f37f07; __utmganji_v20110909=fb715dd2-52c6-4a90-a8b2-9e2cbc986e9e; guazitrackersessioncadata=%7B%22ca_kw%22%3A%22-%22%7D; clueSourceCode=%2A%2300; ganji_uuid=5489692696196677069115; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22f032c884-c040-4f48-9d84-c33ae1840279%22%2C%22sessionid%22%3A%222501670a-df82-46a8-f709-ef8b64f37f07%22%2C%22ca_city%22%3A%22gz%22%7D; lg=1; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1582989488; user_city_id=204; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A84011640170%7D; cityDomain=cs; antipas=6451q58m7050e7124j197646k78; preTime=%7B%22last%22%3A1582992094%2C%22this%22%3A1582989472%2C%22pre%22%3A1582989472%7D; Hm_lpvt_936a6d5df3f3d309bda39e92da3dd52f=1582992096'
    }
    response = requests.get(url, headers=headers)
    html = response.content.decode('utf-8')
    data = etree.HTML(html)
    return data


def get_car_detail_url(url):
    data = parser(url)
    detail_urls = data.xpath('//a[@class="car-a"]/@href')
    # print(detail_urls)
    for url in detail_urls:
        url = 'https://www.guazi.com' + url
        data = parser(url)
        parse_detail(data)


def save_data(info):
    with open('guazi.csv', 'a', encoding='utf-8-sig') as f:
        f.write('{},{},{},{},{},{}\n'.format(info['title'], info['cardtime'], info['displacemment'], info['km'],
                                             info['speedbox'], info['price']))
        print("写入{}".format(info['title'][:5]))


def parse_detail(data):
    title = data.xpath('//div[@class="product-textbox"]/h2/text()')[0].strip()
    info = data.xpath('//div[@class="product-textbox"]/ul/li/span/text()')
    price = data.xpath('//div[@class="product-textbox"]//span[@class="pricestype"]/text()')[0] + '万'

    infos = {}
    cardtime = info[0]
    km = info[1]
    displacemment = info[2]
    speedbox = info[3]

    infos['title'] = title
    infos['cardtime'] = cardtime
    infos['km'] = km
    infos['displacemment'] = displacemment
    infos['speedbox'] = speedbox
    infos['price'] = price

    save_data(infos)


if __name__ == '__main__':
    base_url = 'https://www.guazi.com/cs/buy/o{}/#bread'
    for i in range(1, 6):
        print("开始第{}页抓取".format(i))
        url = base_url.format(i)
        # print(url)
        get_car_detail_url(url)
