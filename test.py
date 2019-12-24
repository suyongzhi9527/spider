import requests

# r = requests.get("https://api.github.com/events")

# r = requests.post('https://httpbin.org/post', data = {'key':'value'})
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('https://httpbin.org/get', params=payload)
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)

"""
爬虫:从网站抓取数据的自动化程序
网站：静态网站，动态网站
静态：从源代码找到所需要的数据
动态：网站需要登录，数据js加密等，微博：ajax异步加载，今日头条
解析数据：re  bs4  xpath  selenium  pyquery  lxml
"""