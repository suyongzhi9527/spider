import requests
from bs4 import BeautifulSoup
import re
import os


class getmeizitu():
    def __init__(self):
        url = "https://www.mzitu.com/"
        # url = "http://www.baidu.com"
        headers = {
            'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, image/apng, */*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN, zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Host': 'http://www.mzitu.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
        }
        html = requests.get(url)
        cookies = str(html.cookies.get_dict())
        print(cookies)
        # self.getall(cookies)

    def getall(self, cookies):
        url = "http://www.mzitu.com/all/"
        headers = {
            'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, image/apng, */*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN, zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Cookie': cookies,
            'Host': 'www.mzitu.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 66.0.3359.117 Safari / 537.36'

        }
        html = requests.get(url, headers=headers)
        print(html.text)

        # years = input("请输入您想要爬去的年份： ")
        # month = input("请输入您想要爬去的月份:  ")
        # month1 = str(month) + "月"
        # soup = BeautifulSoup(html.text, 'lxml')
        # #print(soup.name)
        # all = soup.find('div', text=re.compile(years))
        # all1 = all.next_sibling
        # #print(all1)
        # test = all1.find('em', text=re.compile(month1))
        # ##获取包含月份的父节点
        # parent = test.parent
        # # 获取每个月的数据，也就是上一个标签的兄弟标签
        # allpic = parent.next_sibling
        # # 获取每个图片的url
        # #        print(type(allpic))
        # #         for i in (allpic):
        # allurllist = []
        # for url1 in allpic.find_all('a', href=True):
        #     if url1.get_text(strip=True):
        #         print(type(url1['href']))
        #         allurllist.append(str(url1['href']))
        # # 这里就获取了全部的url,列表形式，以逗号分隔
        # # self.getallpic(strall4)
        # self.getallpic(allurllist, cookies)

    def getallpic(self, url, cookies):
        for i in url:
            headers = {
                'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh - CN, zh;q = 0.9',
                'Cache-Control': 'max - age = 0',
                'Connection': 'keep - alive',
                'Cookie': cookies,
                'Host': 'www.mzitu.com',
                # 'If - Modified - Since': 'Tue, 26 Jun 2018 05: 26:18 GMT',
                'Upgrade-Insecure - Requests': '1',
                'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 66.0.3359.117 Safari / 537.36'
            }
            html = requests.session().get(i, headers=headers)
            soup = BeautifulSoup(html.text, 'lxml')
            all = soup.find('span', text=re.compile("下一页"))
            # 找到下一页的父标签
            parent = all.parent
            # 获取上一级标签，也就是含有最大页面的标签
            allpic = parent.previous_sibling
            maxyema = allpic.find('span').get_text()
            # 获取了最大页面之后循环获取每一页
            for p in range(1, int(maxyema) + 1):
                url = str(i) + "/" + str(p)
                self.downloadpict(p, url, headers)

    def downloadpict(self, yema, url, headers):
        # 加载每一个页面
        html = requests.session().get(url, headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')
        picture = soup.find('div', class_="main-image")
        picture = str(picture)
        # 获取每张图片的url
        pattern = re.compile(r'src="(.*?)"/.*', re.S)
        picturl = pattern.findall(picture)
        # 匹配名称为后面的命令打基础
        namepattern = re.compile(r'alt="(.*?)" src.*', re.S)
        name1 = str(namepattern.findall(picture)).replace('"', '').replace("[", "").replace("]", "")[0:5]

        # picture=requests.get(str(picturl[0]),headers=headers)
        headers = {
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh - CN, zh;q = 0.9',
            'Cache-Control': 'max - age = 0',
            'Connection': 'keep - alive',
            'Host': 'i.meizitu.net ',
            # 'Referer': 'http://www.mzitu.com/139042/7',
            'Referer': 'http://www.mzitu.com/',
            'Upgrade-Insecure - Requests': '1',
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 66.0.3359.117 Safari / 537.36'
        }
        print("正在爬取崔潜喜欢的" + name1 + str(yema) + ".jpg")
        try:
            pwd = os.getcwd()
            picture = requests.get(picturl[0], headers=headers)
            # print(picture)
            isExists = os.path.exists(name1)
            # 判断结果
            if not isExists:
                # 如果不存在则创建目录
                # 创建目录操作函数
                os.makedirs(name1)
            os.chdir(name1)
            with open("" + 'picture' + name1 + str(yema) + '.jpg', 'wb') as file:
                file.write(picture.content)
                file.close()
            os.chdir(pwd)
        except Exception as e:
            print("有异常，异常如下\n %s:" % e)
        else:
            print("爬取崔潜喜欢的" + name1 + str(yema) + ".jpg" + "成功")

            # 已经获取了最大页面接下来开始爬取数据


cuiqian = getmeizitu()
# cuiqian.getall()
# cuiqian.getallpic()
# cuiqian.downloadpict()
