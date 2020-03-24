import requests
import os
import re
from lxml import etree
from multiprocessing.dummy import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

# 梨视频财富板块地址
main_url = 'https://www.pearvideo.com/category_3'
# 解析视屏详情页src
main_page_text = requests.get(main_url, headers=headers).text
tree = etree.HTML(main_page_text)
li_list = tree.xpath('//*[@id="listvideoListUl"]/li')

# 线程池
video_urls = list()
for li in li_list:
    # 详情页具体地址和标题
    detail_url = "https://www.pearvideo.com/" + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0]
    # 对详情页发起请求
    page_text = requests.get(detail_url, headers=headers).text
    # 详情页的video是js动态生成，使用re正则解析
    ex = 'srcUrl="(.*?)",vdoUrl='
    video_url = re.findall(ex, page_text, re.S)[0]  # 返回列表类型
    dic = {
        'url': video_url,
        'name': name
    }
    video_urls.append(dic)


# 回调函数
def get_video(url):
    # 创建存储视频的文件夹
    dir_name = 'video'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    # 对视频地址发请求，将二进制文件持久化存储
    video_data = requests.get(url['url'], headers=headers).content
    file_name = "video/" + url['name'] + ".mp4"
    with open(file_name, 'wb') as f:
        f.write(video_data)
        print(url['name'], "下载完毕！")


# get_video(video_urls)

# 实例化线程池
pool = Pool(4)
pool.map(get_video, video_urls)
