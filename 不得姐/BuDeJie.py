import urllib.request
import re

"""
1. 分析页面URL和视频文件URL特征
2. 获取网页源代码HTML,解决反爬机制
3. 批量下载视频储存
"""


def getVideo(page):
    req = urllib.request.Request("http://www.budejie.com/video/%s" % page)
    # 通过页面增加头文件
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36")
    html = urllib.request.urlopen(req).read()
    html = html.decode("utf-8")
    reg = r'data-mp4="(.*?)"'
    for i in re.findall(reg, html):
        filename = i.split("/")[-1]  # 以/为分割符，保留最后一段，即MP4的文件名
        print("正在下载%s视频" % filename)
        urllib.request.urlretrieve(i, "mp4/%s" % filename)


if __name__ == '__main__':
    for i in range(1, 20):
        getVideo(i)
