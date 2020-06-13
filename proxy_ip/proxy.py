import requests
from lxml import etree


def get_ip():
    url = 'https://www.xicidaili.com/wn/'
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/81.0.4044.92Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    ip_list = html.xpath('//tr[@class="odd"]/td[2]/text()')  # IP
    port_list = html.xpath('//tr[@class="odd"]/td[3]/text()')  # 端口

    ip = []
    for i in range(len(port_list)):
        ip_list[i] += ':{}'.format(port_list[i])
        proxies = {"https": ip_list[i]}
        print(ip_list[i], end=' ')
        try:
            resp = requests.get('https://www.baidu.com', proxies=proxies, timeout=6)
            print(resp.status_code)
            if resp.status_code == 200:
                ip.append(ip_list[i])
        except:
            print('IP无效!')
    return ip_list


with open("ip.txt", "w", encoding="utf-8") as f:
    for i in get_ip():
        f.write(i + '\n')

if __name__ == '__main__':
    get_ip()
