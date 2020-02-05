import requests
import time
from lxml import etree

tieba_name = input('请输入贴吧名:')
startPage = int(input('开始页:'))
endPage = int(input('结束页:'))

for page in range(startPage, endPage):
    yema = (page - 1) * 50
    # print(yema)
    url = "https://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%s" % (tieba_name, yema)
    response = requests.get(url)
    html = response.text
    # print(html)

    element = etree.HTML(html)
    link_list = element.xpath('//a[@class="j_th_tit "]/@href')
    # print(link_list)
    for link in link_list:
        link = "https://tieba.baidu.com" + link
        detail_html = requests.get(link).text
        img_lists = etree.HTML(detail_html)
        img_list = img_lists.xpath('//img[@class="BDE_Image"]/@src')
        for img in img_list:
            img_name = img[-10:]
            img_res = requests.get(img).content
            with open('img/' + img_name, 'wb') as f:
                f.write(img_res)
                print(img_name)
                time.sleep(1)
