import urllib.request
import time
import os
from bs4 import BeautifulSoup


class SpiderDown(object):
    _headers = ''
    _url = ''
    _citylist = []

    def set_headers(self, headers):
        self._headers = headers

    def set_url(self, url, citylist):
        self._url = url
        self._citylist = citylist

    def down_load_page(self, url):
        try:
            # 此处可优化，后面修改成自动获取浏览器version信息
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
            req = urllib.request.Request(url=url, headers=headers)
        except:
            print('打开链接失败url:(%s)' % url)
        else:
            return urllib.request.urlopen(req, timeout=30)

    def parse_html(self, html):
        response1 = html.read().decode('utf-8').replace('price-txt', 'price')
        soup = BeautifulSoup(response1, 'html.parser')
        listinfo = soup.find_all(class_='infos')
        listprice = soup.find_all(class_='favor-pos')
        # print(len(listprice),len(listinfo))
        infolist = []
        for number in range(0, len(listinfo)):
            houseinfo = ''
            if len(listinfo[number].select('.items-name')) != 0:
                houseinfo = houseinfo + (listinfo[number].select('.items-name')[0].get_text())
            else:
                houseinfo = houseinfo + ("default")
            houseinfo = houseinfo + ";"
            if len(listinfo[number].select('.list-map')) != 0:
                houseinfo = houseinfo + (listinfo[number].select('.list-map')[0].get_text())
            else:
                houseinfo = houseinfo + ("default")

            houseinfo = houseinfo + ";"
            for status in listinfo[number].select('.status-icon'):
                houseinfo = houseinfo + (status.get_text())
                houseinfo = houseinfo + ","
            houseinfo = houseinfo + ";"

            if len(listinfo[number].select('.group-mark')) != 0:
                houseinfo = houseinfo + (listinfo[number].select('.group-mark')[0].get_text())
            else:
                houseinfo = houseinfo + ("default")
            houseinfo = houseinfo + ";"

            if len(listprice[number].select('span')) != 0:
                houseinfo = houseinfo + (listprice[number].select('span')[0].get_text())
            else:
                houseinfo = houseinfo + ('-1')
            print('获取城市住房销售信息成功:%s ' % houseinfo)
            infolist.append(houseinfo + '\n')
        return infolist

    # 保存文件按天进行保存
    def save_file(self, infolist):
        filename = 'house_indo_' + time.strftime('%Y%m%d', time.localtime())
        fp = ''
        try:
            if os.path.exists('.\\data'):
                fp = open('.\\data\\' + filename, 'a', encoding='utf-8')
                fp.writelines(infolist)
                fp.close()
            else:
                os.mkdir('.\\data')
                fp = open('.\\data\\' + filename, 'a', encoding='utf-8')
                fp.writelines(infolist)
                fp.close()
        except Exception as e:
            print('保存文件失败，请检查错误信息 %s' % str(e))
            if fp != '':
                fp.close()

    def run_sprider(self):
        # 1、获取链接(安居客)
        url_set = set()
        for city in self._citylist:
            url = self._url + city + '/'
            print('完成一个网页链接:%s' % url)
            url_set.add(url)
        # 2、遍历链接，获取网页
        for url in url_set:
            print('开始爬取[%s]...' % url)
            html = self.down_load_page(url)
            if html.getcode() == 200:
                info_list = self.parse_html(html)
                self.save_file(info_list)
                print('一个批次爬取完成，休眠5秒.......')
                time.sleep(5)
            else:
                print('网页没有正确打开，请检查，网页返回码：(%d)' % html.getcode())


if __name__ == '__main__':
    try:
        jiwuApp = SpiderDown()
        base_url = 'https://xm.fang.anjuke.com/loupan/'
        city_list = ['tongan', 'xiangan', 'jimei', 'haicang', 'zhangzhougang', 'siming', 'huli', 'jiaomei', 'quanzhou',
                     'xiamenzhoushi']
        jiwuApp.set_url(base_url, city_list)
        jiwuApp.run_sprider()
    except Exception as e:
        print('爬取失败,错误信息:%s' % str(e))
