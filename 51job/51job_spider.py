"""
1.确定要抓取的网站
2.解析网站的结构
3.请求网络获取网络返回的信息 html 数据
4.解析返回的html数据 - 提取需要的内容
5.数据的保存 { text,文件夹 }
"""
import requests
import re
import csv
from lxml import etree
from urllib import parse

key = '实施工程师'
key = parse.quote(key)

# 伪装爬虫头部，防止被网站禁止
headers = {'Host': 'search.51job.com',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)\
         Chrome/63.0.3239.132 Safari/537.36'}

data = open('Job_data.csv', 'w', newline='')
writer = csv.writer(data)
writer.writerow(
    ('link', 'job', 'salary', 'company', 'area', 'experience', 'education', 'companytype', 'direction', 'describe'))


def get_links(page):
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,' + key + ',2,' + str(page) + '.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    response = requests.get(url, headers=headers, timeout=10)
    s = requests.session()
    s.keep_alive = False
    response.encoding = 'gbk'
    html = etree.HTML(response.text)
    # reg = re.compile(r'class="t1 ">.*? <a target="_blank" title=".*?" href="(.*?)".*? <span class="t2">', re.S)
    # url_list = re.findall(reg, response.text)
    url_list = html.xpath('//div[@id="resultList"]//div[@class="el"]/p/span/a/@href')
    return url_list


def content_data(url):
    detail_url = requests.get(url, headers=headers, timeout=10)
    s = requests.session()
    s.keep_alive = False
    detail_url.encoding = 'gbk'
    detail_html = etree.HTML(detail_url.text)
    job = detail_html.xpath('//div[@class="cn"]/h1/@title')[0].strip()
    salary = detail_html.xpath('//div[@class="cn"]//strong/text()')[0].strip()
    company = detail_html.xpath('//p[@class="cname"]/a/text()')[0].strip()
    area = detail_html.xpath('//p[@class="msg ltype"]/text()')[0].strip()
    experience = detail_html.xpath('//p[@class="msg ltype"]/text()')[1].strip()
    education = detail_html.xpath('//p[@class="msg ltype"]/text()')[2].strip()
    companytype = detail_html.xpath('//p[@class="at"]/text()')[0].strip()
    companyscale = detail_html.xpath('//p[@class="at"]/text()')[1].strip()
    direction = detail_html.xpath('//p[@class="at"]/a/text()')[0].strip()
    describe = detail_html.xpath('//div[@class="bmsg job_msg inbox"]//text()')
    writer.writerow(
        (url, job, salary, company, area, experience, education, companytype, companyscale, direction, describe)
    )


# 主调用函数
# 抓取前三页信息
for i in range(1, 3):
    print('正在抓取第{}页信息'.format(i))
    links = get_links(i)
    for link in links:
        try:
            content_data(link)
        except:
            print("数据有缺失!")
            continue

# 关闭写入文件
data.close()
