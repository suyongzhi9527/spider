from urllib import request

# 没有使用代理
# url = 'http://httpbin.org/ip'
# req = request.urlopen(url)
# print(req.read())

# 使用代理
url2 = 'http://httpbin.org/get'
# 1.使用Proxyhandler,传入代理构建一个handler
handler = request.ProxyHandler({"https":"157.230.250.116:8080"})
# 2.使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
# 3.使用opener发送请求
res = opener.open(url2)
print(res.read())

"""
ProxyHandler处理器(代理):
1.代理的原理：在请求目的网站的之前，先请求代理服务器，然后让代理服务器去请求目的网站，
代理服务器拿到目的网站的数据后，再转发给我们的代码
2.
"""