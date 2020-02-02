import requests
import time
import re
from lxml import etree

headers = {
    'Host': 'www.lagou.com',
    'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/79.0.3945.117Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}


def request_list_page():
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    base_url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
    data = {
        'first': 'true',
        'pn': 1,
        'kd': 'Python爬虫'
    }
    for i in range(1, 2):
        data['pn'] = i
        s = requests.Session()
        s.get(base_url, headers=headers, timeout=3)
        cookies = s.cookies
        response = requests.post(url, headers=headers, data=data, cookies=cookies)
        result = response.json()
        positions = result['content']['positionResult']['result']
        for position in positions:
            positionid = position['positionId']
            position_url = 'https://www.lagou.com/jobs/%s.html' % positionid
            parse_postion_detail(position_url)
            break
        break


def parse_postion_detail(url):
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    postion_name = html.xpath("//div/@title")[0]
    job_requets_spans = html.xpath('//dd[@class="job_request"]//span/text()')
    salary = job_requets_spans[0].strip()  # 薪资
    city = job_requets_spans[1]  # 城市
    city = re.sub(r'[\s/]', '', city)
    work_years = job_requets_spans[2].strip()  # 工作年限
    work_years = re.sub(r'[\s/]', '', work_years)
    education = job_requets_spans[3].strip()  # 学历要求
    education = re.sub(r'[\s/]', '', education)
    desc = "".join(html.xpath('//dd[@class="job_bt"]//text()')).strip()  # 职位详情
    print(desc)


def main():
    request_list_page()


if __name__ == '__main__':
    main()
