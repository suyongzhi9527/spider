import requests
from bs4 import BeautifulSoup

# 第一步：获取页面
link = "http://www.santostang.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}  # 伪装浏览器访问
r = requests.get(link, headers=headers)  # Response响应对象,从中获取想要的信息
# print(r.text)  # 获取网页内容代码

# 第二步：提取需要的数据
soup = BeautifulSoup(r.text, "lxml")  # 对爬下来的页面进行解析，把HTML代码转换为soup对象
title = soup.find("h1", class_="post-title").a.text.strip()  # 得到第一篇标题
print(title)

# 第三步：存储数据
with open('title.txt', 'a+', encoding='utf-8') as f:
    f.write(title)
