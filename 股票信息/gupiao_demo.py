import requests
import json
import re
import pymysql
from pyquery import PyQuery as pq


# 数据库连接
def connect():
    conn = pymysql.connect('localhost', 'root', '123456', 'stocks')
    # 获取操作游标
    cursor = conn.cursor()
    return {'conn': conn, 'cursor': cursor}


connection = connect()
conn, cursor = connection['conn'], connection['cursor']
sql_insert = "insert into stock(code, name, jinkai, chengjiaoliang, zhenfu, zuigao, chengjiaoe, huanshou, zuidi, zuoshou, liutongshizhi, create_date) values (%(code)s, %(name)s, %(jinkai)s, %(chengjiaoliang)s, %(zhenfu)s, %(zuigao)s, %(chengjiaoe)s, %(huanshou)s, %(zuidi)s, %(zuoshou)s, %(liutongshizhi)s, now())"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}


def get_stock_list(urls):
    r = requests.get(urls, headers=headers)
    r.encoding = 'UTF-8'
    doc = pq(r.text)
    lists = []
    # 获取所有section 中的 a 节点，并进行迭代
    for i in doc('.stockTable a').items():
        try:
            href = i.attr.href
            # print(href)
            lists.append(re.findall(r'\d{6}', href)[0])
        except:
            continue
    lists = [item.lower() for item in lists]  # 将爬取信息转换小写
    return lists


# url = 'https://hq.gucheng.com/gpdmylb.html'
# get_stock_list(url)

def getStockInfo(lists, urls):
    count = 0
    for stock in lists:
        try:
            url = urls + stock
            r = requests.get(url, headers=headers)
            # 将获取到的数据封装进字典
            dict1 = json.loads(r.text[14:int(len(r.text)) - 1])
            # print(dict1)

            # 获取字典中的数据构建写入数据模板
            insert_data = {
                "code": stock,
                "name": dict1['info'][stock]['name'],
                "jinkai": dict1['data'][stock]['7'],
                "chengjiaoliang": dict1['data'][stock]['13'],
                "zhenfu": dict1['data'][stock]['526792'],
                "zuigao": dict1['data'][stock]['8'],
                "chengjiaoe": dict1['data'][stock]['19'],
                "huanshou": dict1['data'][stock]['1968584'],
                "zuidi": dict1['data'][stock]['9'],
                "zuoshou": dict1['data'][stock]['6'],
                "liutongshizhi": dict1['data'][stock]['3475914']
            }
            cursor.execute(sql_insert, insert_data)
            conn.commit()
            print(stock, ":写入完成")
        except Exception as e:
            print("写入异常-->%s" % e)
            # 遇到错误继续循环
            continue


def main():
    stock_url = 'https://hq.gucheng.com/gpdmylb.html'
    stock_info = 'http://qd.10jqka.com.cn/quote.php?cate=real&type=stock&return=json&callback=showStockData&code='
    lists = get_stock_list(stock_url)
    getStockInfo(lists, stock_info)


if __name__ == '__main__':
    main()
