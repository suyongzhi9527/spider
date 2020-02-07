"""
1.确定要抓取的网站
2.解析网站的结构
3.请求网络获取网络返回的信息 html 数据
4.解析返回的html数据 - 提取需要的内容
5.数据的保存 { text,文件夹 }
"""
import requests
import re
from lxml import etree

url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,Python%25E7%2588%25AC%25E8%2599%25AB,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='


def content_data(url):
    item = {}
    detail_url = requests.get(url)
    detail_url.encoding = 'gbk'
    detail_html = etree.HTML(detail_url.text)
    title = detail_html.xpath('//div[@class="cn"]/h1/@title')[0]
    salary = detail_html.xpath('//div[@class="cn"]//strong/text()')[0]
    company = detail_html.xpath('//div[@class="cn"]//p[@class="cname"]/a/@title')[0]
    msg_ltype = detail_html.xpath('//div[@class="cn"]//p[@class="msg ltype"]/@title')[0]
    msg_ltype = re.sub(r'[\s\|]', '', msg_ltype)
    tbordertop_box = "".join(detail_html.xpath('//div[@class="bmsg job_msg inbox"]//p/text()')).strip()
    item = {
        'title': title,
        'salary': salary,
        'company': company,
        'msg': msg_ltype,
        'tbordertop_box': tbordertop_box
    }
    print(item)


response = requests.get(url)
response.encoding = 'gbk'
html = etree.HTML(response.text)
url_list = html.xpath('//div[@id="resultList"]//div[@class="el"]/p/span/a/@href')
for url in url_list:
    content_data(url)
