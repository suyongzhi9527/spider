import requests


def main():
    url = 'https://www.airbnb.cn/s/Shenzhen--China/all?page=1'
    headers = {
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 79.0.3945.117Safari / 537.36'
    }
    text = requests.get(url,headers=headers).text
    print(text)


if __name__ == '__main__':
    main()