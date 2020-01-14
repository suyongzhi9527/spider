import requests
import re
from lxml import etree


def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    html_str = resp.text
    html = etree.HTML(resp.text)
    titles = re.findall(
        r'<h3 class="red">.*?<a .*?>(.*?)</a></h3>', html_str, re.S)  # 段子标题
    content_tag = re.findall(
        r'<div id="endtext">(.*?)</div>', html_str, re.S)  # 段子内容
    dates = html.xpath('//*[@id="footzoon"]/text()')[1:] # 段子时间和点击数
    date_list = []
    for date in dates:
        date = re.sub(r'\s', '', date)
        date_list.append(date)

    contents = []
    for content in content_tag:
        content = re.sub(r'\s|<.*?>', '', content)
        contents.append(content.strip())

    content_list = []
    for value in zip(titles, contents, date_list):
        titles, contents, date_list = value
        contents = {
            'title': titles,
            'content': contents,
            'date': date_list
        }
        content_list.append(contents)

    for content in content_list:
        print(content)
        print("*"*50)


def main():
    url = 'http://www.lovehhy.net/Joke/Detail/QSBK/1'
    for i in range(1, 3):
        url = url.format(i)
        parse_page(url)


if __name__ == "__main__":
    main()
