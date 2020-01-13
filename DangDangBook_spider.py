import requests
import re
import json


def request_dangdang(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_html(html_str):
    pattern = re.compile(r'<li>.*?list_num.*?(\d+).</div>.*?<img.*?src="(.*?)".*?title="(.*?)".*?<span.*?class="tuijian">(.*?)</span>.*?class="publisher_info".*?title="(.*?)".*?<span>(.*?)</span>.*?class="price_n">&yen;(.*?)</span>.*?', re.S)
    items = re.findall(pattern, html_str)
    for item in items:
        yield {
            'rank': item[0],
            'image': item[1],
            'title': item[2],
            'tuijian': item[3],
            'publisher': item[4],
            'time': item[5],
            'price': '¥'+item[6]
        }

def write_item_to_file(item):
    print("开始写入数据===>" + str(item))
    with open("book.txt","a",encoding="utf-8") as f:
        f.write(json.dumps(item,ensure_ascii=False,indent=2) + '\n')


def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + \
        str(page)
    html_str = request_dangdang(url)
    for item in parse_html(html_str):
        write_item_to_file(item)


if __name__ == "__main__":
    for i in range(1, 11):
        main(i)
        break
