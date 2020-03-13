import requests
import re
import xlwt
from bs4 import BeautifulSoup


def open_url(url):
    headers = {
        'user-agent': 'Mozilla/5.0(iPhone;CPUiPhoneOS11_0likeMacOSX) AppleWebKit/604.1.38(KHTML, likeGecko) Version/11.0Mobile/15A372Safari/604.1'
    }
    html = requests.get(url, headers=headers)
    return html.text


def find_data(html):
    data = list()
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find(bosszone="content").find_all(class_="text")
    # for tar in content:
    #     print(tar.text)
    tar = iter(content)
    for t in tar:
        if t.text.isnumeric():
            data.append([
                re.search(r'\[(.+)\]', next(tar).text).group(1),
                re.search(r'\d.*', next(tar).text).group(),
                re.search(r'\d.*', next(tar).text).group(),
                re.search(r'\d.*', next(tar).text).group()
            ])
    return data


def to_excel(data):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('sheet1')
    headata = ['城市', '平均房价', '平均工资', '房价工资比']
    for i in range(len(headata)):
        ws.write(0, i, headata[i])
    for i in range(len(data)):
        for j in range(len(headata)):
            ws.write(i + 1, j, data[i][j])
    wb.save('no5.xls')
    print('数据写入excel成功!')


def main():
    url = 'https://news.house.qq.com/a/20170702/003985.htm'
    html = open_url(url)
    data = find_data(html)
    to_excel(data)


if __name__ == '__main__':
    main()
