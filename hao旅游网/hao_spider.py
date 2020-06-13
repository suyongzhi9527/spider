import requests
from lxml import etree


class HaoSpider(object):
    def __init__(self):
        self.url = 'https://go.hao123.com/ticket?city={0}&pn={1}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
        }

    def get_page(self, url):
        response = requests.get(url, headers=self.headers)
        html = response.content.decode('utf-8')
        self.parse_page(html)

    def parse_page(self, html):
        parse_html = etree.HTML(html)
        link = parse_html.xpath(
            '//div[@class="info-item"]//div[@class="info g-ib"]/a/@href')
        for url in link:
            html = requests.get(
                url, headers=self.headers).content.decode('utf-8')
            parse_html1 = etree.HTML(html)
            dict_list = dict()
            try:
                # 景区名
                s_name = parse_html1.xpath(
                    '//div[@class="info_r"]//h3[@class="s_name"]/text() | //div[@class="brief-box clearfix"]//div[@class="brief-right"]/h2/text()')
                open_time = parse_html1.xpath(
                    '////div[@class="info_r"]//p[@class="s_com open_time canhover"]//span/text() | //div[@class="brief-box clearfix"]//div[@class="brief-right"]//li[@class="time"]//span[@data-reactid="51"]/text()')
                comment = parse_html1.xpath(
                    '//div[@class="s_comment"]/div[@class="s_comment_i"]/text()')
                s_price = parse_html1.xpath(
                    '//div[@class="s_price"]/div[@class="s_p_t"]//b/text() | //td[@class="td5"]//strong[@class="ttd-fs-24"]/text()')
                if len(s_name) != 0:
                    dict_list['景点名称'] = s_name[0].strip()
                else:
                    dict_list['景点名称'] = 'null'
                if len(open_time) != 0:
                    dict_list['开放时间'] = open_time[0].strip()
                else:
                    dict_list['开放时间'] = 'null'
                if len(comment) != 0:
                    dict_list['精彩点评'] = comment[0].strip()
                else:
                    dict_list['精彩点评'] = 'null'
                if len(s_price) != 0:
                    dict_list['价格'] = s_price[0].strip()
                else:
                    dict_list['价格'] = 'null'
            except Exception as e:
                print(e)
            print(dict_list)

    def main(self):
        startPage = int(input('起始页:'))
        endPage = int(input('结束页:'))
        city = input('城市:')
        for page in range(startPage, endPage+1):
            print('第'+ str(page) + '页')
            url = self.url.format(city, page)
            self.get_page(url)


if __name__ == "__main__":
    hao = HaoSpider()
    hao.main()
