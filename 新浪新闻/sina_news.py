import codecs
import requests
import json
import re
from bs4 import BeautifulSoup as bs
from pybloom_live import ScalableBloomFilter


def getdetailpagebybs(url):
    detail = dict()  # 创建一个字典，存放URL、title、newstime等信息
    detail['url'] = url  # 将URL时间存入detail字典中的相应键值中

    page = requests.get(url).content  # 使用requests.get方法获取网页代码，由于bs4可以自动解码URL的编码，所以此处不需要decode
    html = bs(page, "lxml")  # 使用lxml解析器
    title = html.find(class_="main-title")  # 获取新闻网页中的title信息，此处网页中只有一个“class=main-title”，所以使用find即可
    print(title.text.strip())  # 新闻标题
    detail["title"] = title.text  # 将新闻标题以文本形式存入detail字典中的相应键值中
    artibody = html.find(class_="article")  # 使用find方法，获取新闻网页中的article信息
    print(artibody.text.strip())
    detail["artibody"] = artibody.text
    date_source = html.find(class_="date_source")  # 使用find方法，获取新闻网页中的date-source信息
    # 由于不同的新闻详情页之间使用了不同的标签元素，直接抽取可能会报错，所以此处使用判断语句来进行区分爬取
    # if date_source.a:
    #     print(date_source.span.text)
    #     detail["newstime"] = date_source.span.text
    #     print(date_source.a.text)
    #     detail["newsfrom"] = date_source.a.text
    # else:
    #     print(date_source("span")[0].text)
    #     detail["newstime"] = date_source("span")[0].text  # 抽取'span'标签中包含的时间信息
    #     print(date_source("span")[1].text)
    #     detail["newsfrom"] = date_source("span")[1].text  # 抽取'span'标签中包含的新闻来源信息
    return detail


def savenews(data, new):
    f = codecs.open('F:\\爬虫\\新浪新闻\\' + new + '.txt', 'a+', 'utf-8')
    f.write(json.dumps(data, ensure_ascii=False))
    f.close()
    # with open('F:\\爬虫\\新浪新闻\\' + new + '.txt', 'a+', encoding='utf-8') as f:
    #     f.write(json.dumps(data, ensure_ascii=False))


urlbloomfilter = ScalableBloomFilter(initial_capacity=100, error_rate=0.001, mode=ScalableBloomFilter.LARGE_SET_GROWTH)
page = 1
error_url = set()  # 创建集合，用于存放出错的URL链接
while page <= 10:
    data = requests.get(
        "https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=" + str(page))  # 拼接URL，并获取索引页面信息
    if data.status_code == 200:  # 当请求页面返回200（代表正确）时，获取网页数据
        # 将获取的数据json化
        data_json = json.loads(data.content)
        news = data_json.get("result").get("data")  # 获取result节点下data节点中的数据，此数据为新闻详情页的信息
        # 从新闻详情页信息列表news中，使用for循环遍历每一个新闻详情页的信息
        for new in news:
            # 查重，从new中提取URL，并利用ScalableBloomFilter查重
            if new["url"] not in urlbloomfilter:
                urlbloomfilter.add(new["url"])  # 将爬取过的URL放入urlbloomfilter中
                try:
                    # print(new)
                    detail = getdetailpagebybs(new["url"])
                    savenews(detail, new["docid"][-7:])
                except Exception as e:
                    error_url.add(new["url"])
        page += 1
        break
