from urllib import request, parse
import requests
import json

url = 'https://www.lagou.com/jobs/positionAjax.json?xl=%E5%A4%A7%E4%B8%93&px=default&needAddtionalResult=false'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=',
    'Origin': 'https://www.lagou.com'
}

data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python爬虫'
}

urls = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

s = requests.Session()
# 获取搜索页的cookies
s.get(urls, headers=headers, timeout=3)

cookie = s.cookies

req = s.post(url, data=data, headers=headers, cookies=cookie, timeout=5).text
dict_list = json.loads(req)
print(dict_list['content']['positionResult']['result'])
