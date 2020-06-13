import requests
import random
import csv
from lxml import etree
from fake_useragent import UserAgent


class Travel(object):
    def __init__(self):
        self.url = "https://place.qyer.com/south-korea/citylist-0-0-{}/"
        self.film_list = list()
        ua = UserAgent(verify_ssl=False)
        for i in range(1, 50):
            self.film_list.append(ua.chrome)
            self.Hostreferer = {
                'User-Agent': random.choice(self.film_list)
            }

    def get_page(self, url):
        html = requests.get(url, headers=self.Hostreferer).content.decode('utf-8')
        parse_html = etree.HTML(html)
        image_src_list = parse_html.xpath('//ul[@class="plcCitylist"]/li')
        for i in image_src_list:
            title = i.xpath('.//h3//a/text()')[0].strip()
            beento = i.xpath('.//p[@class="beento"]/text()')[0].strip()
            pics = i.xpath('.//p[@class="pics"]//img//@src')[0].strip()
            # print(title, beento, pics)
            csv_file = open('scrape.csv', 'a', encoding='gbk')
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([title, beento, pics])
            csv_file.close()
        print("成功!")


    def main(self):
        startPage = int(input("起始页:"))
        endPage = int(input("终止页:"))
        for page in range(startPage, endPage + 1):
            url = self.url.format(page)
            self.get_page(url)


if __name__ == "__main__":
    spider = Travel()
    spider.main()
