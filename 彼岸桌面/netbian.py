import os
import time
import random
import requests
from bs4 import BeautifulSoup

index = 'http://www.netbian.com'  # 网站根地址
interval = 1  # 爬取图片的间隔时间
firstDir = r'E:\Python程序设计实验项目\爬虫\彼岸桌面'  # 总路径,因为不会自动创建文件夹,所以这里自己修改一下即可
classificationDict = {}  # 存放网站分类子页面的信息


# 获取页面筛选后的内容列表
def screen(url, select):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
    html = requests.get(url=url, headers=headers)
    html.encoding = 'gbk'  # 网站的编码
    html = html.text
    soup = BeautifulSoup(html, 'lxml')
    return soup.select(select)


# 获取页码
def screenPage(url, select):
    # 随机获取一个headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
    html = requests.get(url=url, headers=headers)
    html.encoding = 'gbk'
    html = html.text
    soup = BeautifulSoup(html, 'lxml')
    return soup.select(select)[0].next_sibling.text


# 定位到 1920*1080 分辨率图片
def handleImgs(links, path):
    for link in links:
        href = link.get('href')  # /desk/22629.htm
        if (href == 'http://pic.netbian.com/'):  # 过滤图片广告
            continue

        # 第一次跳转
        if ('http://' in href):  # 有极个别图片不提供正确的相对地址
            url = href
        else:
            url = index + href  # http://www.netbian.com/desk/22629.htm
        select = 'div#main div.endpage div.pic div.pic-down a'
        # [<a href="/desk/22629-1920x1080.htm" target="_blank">下载壁纸<span>（1920x1080）</span></a>]
        link = screen(url, select)
        if (link == []):
            print(url + ' 无此图片，爬取失败')
            continue
        href = link[0].get('href')  # /desk/22629-1920x1080.htm

        # 第二次跳转
        url = index + href  # http://www.netbian.com/desk/22629-1920x1080.htm

        # 获取到图片了
        select = 'div#main table a img'
        # [<img alt="晚上 灯 女子 天使2k动漫壁纸" src="http://img.netbian.com/file/2020/0424/ee0e117577a998b7cbc1e7d74578d53a.jpg" title="晚上 灯 女子 天使2k动漫壁纸"/>]
        link = screen(url, select)
        if (link == []):
            print(url + " 该图片需要登录才能爬取，爬取失败")
            continue
        name = link[0].get('alt')
        print(name)  # 输出下载图片的文件名
        src = link[0].get('src')
        print(src)  # 打印高清图片地址

        if (requests.get(src).status_code == 404):
            print(url + ' 该图片下载链接404，爬取失败')
            print()
            continue

        print()
        # D:\Python程序设计实验项目\爬虫/动漫/1/晚上 灯 女子 天使2k动漫壁纸.jpg
        jpg_path = path + '/' + name + '.jpg'

        # 下载保存图片
        with open(jpg_path, 'wb') as f:
            resp = requests.get(src).content
            f.write(resp)
        time.sleep(interval)


# 选择下载分类子页面
def select_classification(choice):
    secondUrl = classificationDict[choice]['url']
    secondDir = classificationDict[choice]['path']

    if (not os.path.exists(secondDir)):
        os.mkdir(secondDir)  # 创建分类目录

    select = '#main > div.page > span.slh'
    pageIndex = screenPage(secondUrl, select)
    lastPagenum = int(pageIndex)  # 获取最后一页的页码
    for i in range(0, lastPagenum):
        if i == 0:
            url = secondUrl
        else:
            url = secondUrl + 'index_%d.htm' % (i + 1)

        print('--------------' + choice + ': ' + str(i + 1) + '-------------')
        path = secondDir + '/' + str(i + 1)
        if (not os.path.exists(path)):
            os.mkdir(path)  # 创建分类目录下页码目录

        select = 'div#main div.list ul li a'
        links = screen(url, select)
        handleImgs(links, path)


# ui界面，用户选择下载分类
def ui():
    print('--------------netbian-------------')
    print('全部', end=' ')
    for c in classificationDict.keys():
        print(c, end=' ')
    print()
    choice = input('请输入分类名：')
    if (choice == '全部'):
        for c in classificationDict.keys():
            select_classification(c)
    elif (choice not in classificationDict.keys()):
        print("输入错误，请重新输入！")
        print('----')
        ui()
    else:
        select_classification(choice)


# 将分类子页面信息存放在字典中
def init_classification():
    url = index
    select = '#header > div.head > ul > li:nth-child(1) > div > a'
    classifications = screen(url, select)
    for c in classifications:
        href = c.get('href')  # 获取的是相对地址
        text = c.string  # 获取分类名
        if (text == '4k壁纸'):  # 4k壁纸，因权限问题无法爬取，直接跳过
            continue
        secondDir = firstDir + '/' + text  # 分类目录
        url = index + href  # 分类子页面url  http://www.netbian.com/rili/
        global classificationDict
        classificationDict[text] = {
            'path': secondDir,
            'url': url
        }


def main():
    if (not os.path.exists(firstDir)):
        os.mkdir(firstDir)  # 创建总目录
    init_classification()
    ui()


if __name__ == '__main__':
    main()
