import requests
import parsel
import time


def check_ip(proxies_list):
    """
    检测代理IP是否可用
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    }
    can_use = list()
    for proxy in proxies_list:
        # print(proxy)
        try:
            proxies = {
                "http": proxy,
            }
            # response = requests.get('https://www.baidu.com', headers=headers, proxies=proxy, timeout=0.1)
            req = requests.get("http://ip.xpcha.com/myip.php", proxies=proxies, timeout=5)
            if response.status_code == 200:
                html = req.text
                html_ip = parsel.Selector(html)
                medium = html_ip.xpath('//p[@class="medium"]/span/text()').extract_first()
                print("你的IP地址是：",medium)
                can_use.append(proxy)
        except Exception as e:
            print(e)
    return can_use


proxies_list = list()
for i in range(1, 3):
    print('===============正在抓取第{}页数据==============='.format(i))
    base_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    }

    response = requests.get(base_url, headers=headers)
    data = response.text

    html_data = parsel.Selector(data)

    parse_list = html_data.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')

    for tr in parse_list:
        proxies_dict = {}
        http_type = tr.xpath('./td[4]/text()').extract_first()  # 协议类型
        ip = tr.xpath('./td[1]/text()').extract_first()  # IP
        port = tr.xpath('./td[2]/text()').extract_first()  # 端口

        proxies_dict = 'http://' + ip + ':' + port
        proxies_list.append(proxies_dict)
        print(proxies_dict)
        time.sleep(0.5)

print(proxies_list)
print('获取代理IP数量:', len(proxies_list))

can_use = check_ip(proxies_list)
print('可用的代理IP:', can_use)
print('可用代理IP数量:', len(can_use))
