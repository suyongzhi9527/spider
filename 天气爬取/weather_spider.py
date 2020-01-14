import requests
from bs4 import BeautifulSoup
from pyecharts import options as opts
from pyecharts.charts import Bar

# 需求：爬取全国所有城市和对应的天气数据

ALL_DATA = []

def parse_page(url):  # 定义一个解析网页函数
    resp = requests.get(url)
    text = resp.content.decode()  # 网页源代码

    # 1.先取到"conMidtab"
    soup = BeautifulSoup(text, 'html5lib')
    conMidtab = soup.find("div", class_="conMidtab")
    # 2.找到所有的table标签
    tables = conMidtab.find_all("table")
    for table in tables:
        # 3.找到所有的tr标签，并过滤前2个
        trs = table.find_all("tr")[2:]
        for index, tr in enumerate(trs):  # 返回两个值，第一个是下标，第二个是下标值
            # 4.获取城市和温度
            tds = tr.find_all("td")
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]  # 获取标签下面的子孙节点的文本内容
            # 获取温度
            temp_id = tds[-2]
            min_temp = list(temp_id.stripped_strings)[0]
            ALL_DATA.append({"city":city,"min_temp":int(min_temp)})
            # print({"city":city,"min_temp":int(min_temp)})


def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',  # 华北
        'http://www.weather.com.cn/textFC/db.shtml',  # 东北
        'http://www.weather.com.cn/textFC/hd.shtml',  # 华东
        'http://www.weather.com.cn/textFC/hz.shtml',  # 华中
        'http://www.weather.com.cn/textFC/hn.shtml',  # 华南
        'http://www.weather.com.cn/textFC/xb.shtml',  # 西北
        'http://www.weather.com.cn/textFC/xn.shtml',  # 西南
        'http://www.weather.com.cn/textFC/gat.shtml'  # 港澳台
    ]
    for url in urls:
        parse_page(url)

    # 分析数据
    # 根据最低气温进行排序
    ALL_DATA.sort(key=lambda data:data['min_temp']) # 匿名函数
    data = ALL_DATA[0:10] # 取前十个城市气温
    city = list(map(lambda x:x['city'],data))
    temps = list(map(lambda x:x['min_temp'],data))
    bar = Bar()
    bar.add_xaxis(city)
    bar.add_yaxis("城市",temps)
    bar.set_global_opts(title_opts=opts.TitleOpts(title="中国天气最低气温排行榜",subtitle="前十个最低气温城市"))
    bar.render("weather.html")
    

if __name__ == "__main__":
    main()

    
