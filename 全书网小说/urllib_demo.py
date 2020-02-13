import urllib.request
import re


# 获取页面源代码
# 获取章节连接
# 获取章节页面源代码
# 获取章节内容
# 下载

def download_novert():
    # 获取页面源代码
    headers = {
        'Host': 'www.quanshuwang.com',
        'Cookie': 'fikker-DUjq-IGhG=xujQNN49VCFILcL9lSpG0M6JMLnc49IN; fikker-DUjq-IGhG=xujQNN49VCFILcL9lSpG0M6JMLnc49IN; bdshare_firstime=1581432590294; jieqiHistoryBooks=%5B%7B%22articleid%22%3A%22269%22%2C%22articlename%22%3A%22%u51E1%u4EBA%u4FEE%u4ED9%u4F20%22%2C%22chapterid%22%3A%2278850%22%2C%22chaptername%22%3A%22%u7B2C%u4E00%u5377%20%u4E03%u7384%u95E8%u98CE%u4E91%20%u7B2C%u4E00%u7AE0%20%u5C71%u8FB9%u5C0F%u6751%22%7D%5D; _ga=GA1.2.1913132680.1581432627; _gid=GA1.2.272560784.1581432627',
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3945.117Safari / 537.36',
    }
    url = 'http://www.quanshuwang.com/book/0/269'
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read()
    # 指定编码
    html = html.decode("gbk")
    # 获取章节连接
    reg = '<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    urls = re.findall(reg, html)
    for url in urls:
        # nover_url = url[0]  # 小说章节
        # nover_title = url[1]  # 小说标题
        nover_url, nover_title = url
        req = urllib.request.Request(nover_url, headers=headers)
        chapt = urllib.request.urlopen(req).read()  # 获取章节页面源代码
        chapt_html = chapt.decode("gbk")
        # 获取章节内容
        reg = '</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'
        chapt_content = re.findall(reg, chapt_html, re.S)
        # 数据清洗
        chapt_content = chapt_content[0].replace('&nbsp;', '')
        chapt_content = chapt_content.replace('<br />', '')
        # 下载到本地
        # f = open('{}.txt'.format(nover_title), 'w')
        # f.write(chapt_content)
        # print("正在下载%s" % nover_title)
        # f.close()
        with open('TXT/{}.txt'.format(nover_title), 'w', encoding="utf-8") as f:
            print("正在下载%s" % nover_title)
            f.write(chapt_content)


def main():
    download_novert()


if __name__ == '__main__':
    main()
