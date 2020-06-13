import requests
import re
import json


def start():
    for page in range(0, 1600, 32):
        try:
            url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/1?uuid=9056230DD3A5CF85F2BF3310D9213340D8C10904049D7374779ECF0C1D3CF6D0&userid=-1&limit=32&offset=' + str(
                page) + '&cateId=-1&q=%E7%81%AB%E9%94%85'
            headers = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',
                'Host': 'apimobile.meituan.com',
                'Origin': 'https://bj.meituan.com',
                'Referer': 'https://bj.meituan.com/s/%E7%81%AB%E9%94%85/'
            }
            response = requests.get(url, headers=headers)
            titles = re.findall('","title":"(.*?)","address":"', response.text)
            addresses = re.findall(',"address":"(.*?)",', response.text)
            avgprices = re.findall(',"avgprice":(.*?),', response.text)
            avgscores = re.findall(',"avgscore":(.*?),', response.text)
            comments = re.findall(',"comments":(.*?),', response.text)
            print(len(titles), len(addresses), len(avgprices), len(avgscores), len(comments))
            for i in range(len(titles)):
                title = titles[i]
                address = addresses[i]
                avgprice = avgprices[i]
                avgscore = avgscores[i]
                comment = comments[i]
                # 写入本地文件
                file_data(title, address, avgprice, avgscore, comment)
        except:
            pass


def file_data(title, address, avgprice, avgscore, comment):
    data = {
        '店铺名称': title,
        '店铺地址': address,
        '平均消费价格': avgprice,
        '店铺评分': avgscore,
        '评价人数': comment
    }
    with open('美团美食.txt', 'a', encoding='utf-8')as fb:
        fb.write(json.dumps(data, ensure_ascii=False) + '\n')
        # ensure_ascii=False必须加因为json.dumps方法不关闭转码会导致出现乱码情况


if __name__ == '__main__':
    start()
