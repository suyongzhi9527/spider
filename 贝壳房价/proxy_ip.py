import requests
import random
import telnetlib
from bs4 import BeautifulSoup
from headers import create_headers

# 定义变量
proxys_src = []
proxys = []


# 请求获取代理地址
def spider_proxyip(num=10):
    try:
        url = 'http://www.xicidaili.com/nt/1'
        # 获取代理 IP 列表
        req = requests.get(url, headers=create_headers())
        source_code = req.content
        # 解析返回的 html
        soup = BeautifulSoup(source_code, 'lxml')
        # 获取列表行
        ips = soup.findAll('tr')

        # 循环遍历列表
        for x in range(1, len(ips)):
            ip = ips[x]
            tds = ip.findAll("td")
            proxy_host = "{0}://".format(tds[5].contents[0]) + tds[1].contents[0] + ":" + tds[2].contents[0]
            proxy_temp = {tds[5].contents[0]: proxy_host}
            # 添加到代理池
            proxys_src.append(proxy_temp)
            if x >= num:
                break
    except Exception as e:
        print("获取代理地址异常:")
        print(e)


spider_proxyip()


def create_proxy():
    proxy = random.choice(proxys_src)
    return proxy


proxy = create_proxy()

# print('------------------------connect---------------------------')
# # 连接Telnet服务器
# try:
#     tn = telnetlib.Telnet('49.72.208.42', port='8118', timeout=10)
# except:
#     print('该代理IP  无效')
# else:
#     print('该代理IP  有效')
#
# print('-------------------------end----------------------------')
