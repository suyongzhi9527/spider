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
    for i in range(1, 3):
        data['pn'] = i
        session = requests.Session()
        session.get(base_url, headers=headers, timeout=3)
        cookies = session.cookies
        response = requests.post(url, headers=headers, data=data, cookies=cookies)
        result = response.json()
        positions = result['content']['positionResult']['result']
        for position in positions:
            positionid = position['positionId']  # 获取职位的ID
            position_url = 'https://www.lagou.com/jobs/%s.html' % positionid  # 构建详情页的url
            parse_postion_detail(position_url)  # 请求详情页的url
            time.sleep(1)
            break
        # break


def parse_postion_detail(url):
    response = requests.get(url, headers=headers).text
    html = etree.HTML(response)  # 构建HTML对象
    postion_name = html.xpath('//span[@class="name"]/text()')[0]  # 职位
    job_requets_spans = html.xpath('//dd[@class="job_request"]//span/text()')  # 取到所有的span标签
    salary = job_requets_spans[0].strip()  # 薪资
    city = job_requets_spans[1]  # 城市
    city = re.sub(r'[\s/]', '', city)  # 空白字符\s和/斜杆替换为空字符
    work_years = job_requets_spans[2].strip()  # 工作年限
    work_years = re.sub(r'[\s/]', '', work_years)
    education = job_requets_spans[3].strip()  # 学历要求
    education = re.sub(r'[\s/]', '', education)
    desc = "".join(html.xpath('//dd[@class="job_bt"]//text()')).strip()  # 职位详情
    company_name = html.xpath('//h3[@class="fl"]/em/text()')[0].strip()  # 公司
    print(postion_name, salary, city, education, company_name, desc)


def main():
    request_list_page()


if __name__ == '__main__':
    main()
