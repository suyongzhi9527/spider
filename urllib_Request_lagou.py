from urllib import request,parse

url = 'https://www.lagou.com/jobs/positionAjax.json?xl=%E5%A4%A7%E4%B8%93&px=default&needAddtionalResult=false'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=',
    'Origin':'https://www.lagou.com'
}

data = {
    'first':'true',
    'pn':'1',
    'kd':'python爬虫'
}

req = request.Request(url,headers=headers,method='POST',data=parse.urlencode(data).encode('utf-8'))
resp = request.urlopen(req)
print(resp.read().decode("utf-8")) 