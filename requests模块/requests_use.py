# 引入第三方模块
import requests
import json

# req = requests.get("https://ptorch.com")
# print(req.text)  # 提取目标网页代码

# Requests基本请求方式
requests.get("http://httpbin.org/get")  # GET请求
requests.post("http://httpbin.org/post")  # POST请求
requests.put("http://httpbin.org/put")  # PUT请求
requests.delete("http://httpbin.org/delete")  # DELETE请求
requests.head("http://httpbin.org/heade")  # HEAD请求
requests.options("http://httpbin.org/options")  # OPTIONS请求

# GET请求带参数
payload = {'key1': 'value1', 'key2': 'value2'}
req = requests.get("http://httpbin.org/get", params=payload)
# print(req.url)

# POST请求带参数
payload = {'key1': 'value1', 'key2': 'value2'}
req = requests.post("http://httpbin.org/post", params=payload)
# print(req.text)

# POST请求发送JSON数据
url = "http://httpbin.org/post"
payload = {'some': 'data'}
req1 = requests.post(url, data=json.dumps(payload))
req2 = requests.post(url, json=payload)
print(req1.text)
print(req2.text)

# POST文件上传
url = 'http://httpbin.org/post'
files = {'file': open('test.xlsx', 'rb')}
req = requests.post(url, files=files)
req.text

# 请求会话
s = requests.Session()
s.get("http://httpbin.org/get")

# Cookie获取
req = requests.get("https://ptorch.com")
req = requests.get("https://ptorch.com")
print(req.cookies)
print(req.cookies['laravel_session'])

# 超时配置
requests.get('http://github.com', timeout=0.001)  # timeout 仅对连接过程有效，与响应体的下载无关。

# 代理
proxies = {
  "https": "http://127.0.0.1:4433"
}
req = requests.post("http://httpbin.org/post", proxies=proxies)
print(req.text)
