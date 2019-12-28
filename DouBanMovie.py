# 1.导入第三方库
import requests
from lxml import etree
import lxml.html
import csv
# 2.获取目标网页
# url规律:页数-1*25 用5的倍数替换任意一页内容
url = 'https://movie.douban.com/top250?start={}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

# 3.解析目标网页
# 定义一个函数，获取网页中需要的数据
def get_html(url):
    # 获取网页内容
    resp = requests.get(url,headers=headers)
    resp.encoding = 'UTF-8'
    return resp.content

# 定义一个函数，获取每一个电影的相关信息
def get_content(html_str):
    html = etree.HTML(html_str)
    # html = lxml.html.document_fromstring(html_str)
    movie_list = html.xpath("//div[@class='info']")
    # 定义空列表，存放信息
    moviList = []
    # 勇for循环把电影信息展开
    for each in movie_list:
        # 创建一个空字典，保存电影信息，标题、地址、评分、引言
        items = {}
        title = each.xpath(".//div[@class='hd']/a/span[@class='title']/text()") # 标题
        # print(title)
        otherTitle = each.xpath(".//div[@class='hd']/a/span[@class='other']/text()") # 副标题
        # print(otherTitle)
        link = each.xpath(".//div[@class='hd']/a/@href")[0] # url链接
        # print(link)
        star = each.xpath(".//div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()") # 评分
        # print(star)
        quote = each.xpath(".//div[@class='bd']/p[@class='quote']/span/text()") # 引言
        # print(quote)

        # 保存进字典中
        items['标题'] = ''.join(title+otherTitle)
        items['链接'] = link
        items['评分'] = star
        items['名言'] = quote
        print(items)
        moviList.append(items)
    return moviList


# 4.下载目标网页数据
# 定义一个函数，保存数据进csv
def save_content(moviList):
    with open('DouBanMovie.csv','a',encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f,fieldnames=['标题','评分','名言','链接'])
        writer.writeheader() # 写入表头

        # 传入的参数是一个列表，每个元素代表每行数据
        for each in moviList:
            writer.writerow(each)


if __name__ == "__main__":
    movieList = []
    for i in range(10):
        url_list = url.format(i * 25)
        print(url_list)
        html_str = get_html(url_list)
        # print(html_str)
    # url = url.format(1)
    # print(url)
    # html_str = get_html(url)
    # print(html_str)
        movieList += get_content(html_str)
    
    print(movieList[:10])
    save_content(movieList)
