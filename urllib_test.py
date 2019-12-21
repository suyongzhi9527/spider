from urllib import request,parse

resp = request.urlopen('http://www.baidu.com')
# print(resp.read())
# print(resp.readline())
# print(resp.readlines()) 
# print(resp.getcode()) # 获取状态码

# urlretrieve函数使用
# request.urlretrieve('http://www.baidu.com','baidu.html') # 保存页面到本地

# urlencode函数使用
# data = {'name':'爬虫基础','greet':'Hello spider','age':20}
# qs = parse.urlencode(data) # 进行编码
# print(qs)

# url = 'https://www.baidu.com/s?'
# parses = {
#     'kw':'爬虫'
# }
# qs = parse.urlencode(parses)
# url = url + qs
# resp = request.urlopen(url)
# print(resp.read())

# parse_qs函数使用
data = {'name':'爬虫基础','greet':'Hello spider','age':20}
qs = parse.urlencode(data) # 进行编码
result = parse.parse_qs(qs)
print(result)