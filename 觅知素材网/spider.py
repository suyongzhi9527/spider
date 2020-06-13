import requests
from lxml import etree
from urllib.request import urlretrieve


class ImageSpider(object):
    def __init__(self):
        self.url = 'https://www.51miz.com/so-sucai/140321/p_{}/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
        }

    def get_page(self, url):
        response = requests.get(url, headers=self.headers)
        html = response.content.decode('utf-8')
        return html

    def parse_page(self, html):
        parse_html = etree.HTML(html)  # 解析html对象
        img_src_list = parse_html.xpath('//a[@class="image-box"]/@href')
        for src in img_src_list:
            # print(src)
            # if 'ppt' in src or 'muban' in src or 'dianshang' in src or 'biaoge' in src or 'wendang' in src:
            #     continue
            html1 = self.get_page(src)
            parse_html1 = etree.HTML(html1)
            try:
                bimg_url = parse_html1.xpath(
                    '//div[@class="preview-content"]//img/@src')[0]
                name = parse_html1.xpath(
                    '//div[@class="showTitle"]//h1/span//text()')[0].strip()
                file_path = '爬虫\\觅知素材网\\img\\' + name + '.jpg'
                bimg_url = 'http:' + bimg_url
                # print(name,bimg_url)
                urlretrieve(bimg_url, file_path)
                print('%s下载成功!' % name)
                # print(file_path)
            except Exception as e:
                # print(e)
                pass

    def main(self):
        startPage = int(input('起始页:'))
        endPage = int(input('终止页:'))
        for page in range(startPage, endPage + 1):
            print('第' + str(page) + '页')
            url = self.url.format(page)
            html = self.get_page(url)
            self.parse_page(html)


if __name__ == "__main__":
    img = ImageSpider()
    img.main()
