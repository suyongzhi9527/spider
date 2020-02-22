import requests
import re
import time


def get_html(url):
    headers = {
        'cookie': 'cna=NXfGFtwxwyECAXQV6wqFrOqO; t=3e7bdfa84d92e235acd29e5c0d339e10; thw=cn; uc3=id2=UoH%2B4xVWYJ%2F04Q%3D%3D&vt3=F8dBxdzwGBpWeVSIH%2Fg%3D&nk2=rM7MtiLsOcZFNQ%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D; lgc=%5Cu590F%5Cu5B63%5Cu7EC3%5Cu604B%5Cu6B4C; uc4=id4=0%40UOnhBz4ba3wwqpmOFZ7YscpjH9wB&nk4=0%40ruDqiqvtjVNDBkpsOlhdCiuJV27p; tracknick=%5Cu590F%5Cu5B63%5Cu7EC3%5Cu604B%5Cu6B4C; _cc_=W5iHLLyFfA%3D%3D; tg=0; hng=CN%7Czh-CN%7CCNY%7C156; _tb_token_=iIJoiWWENAs0mivtbG4X; _samesite_flag_=true; cookie2=1a65abdf4934e9140c5b1d9f89bd0425; mt=ci=-1_0; v=0; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; tfstk=cYFFB39A86CFGs6anjGrVvwjX9AdZ3FuG93-K-D2MYKCNmMhibx-S6BLvuoAsvf..; enc=tsMIBjXr%2BR0uVg5vTv5CDBUM%2B1tBpmpKOSrW6MhTRE%2FsskgByOy%2Boydn30C3eDYhXIoOZWYNigeiUluMxduOrg%3D%3D; JSESSIONID=EF3081C48DB0A40CAEF5121A4A7E5794; uc1=cookie14=UoTUOLC2HCslbg%3D%3D; l=dBIlyPBPQYlCrVmCBOCMCDHAabbOIIRxoulpk5gyi_5Q86L16y_Oo-gkzFp6DjWftV8B43ral1J9-etkiKy06Pt-g3fP6xDc.; isg=BB0dKXT3H-2tZfvSPTvguO8_LPkXOlGMwOLrCd_iSHSjlj3Ip470XEEExYqQaGlE',
        'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/79.0.3945.117Safari/537.36'
    }
    try:
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def parse_page(ilt, html):
    try:
        # "raw_title":"()"
        plt = re.findall(r'\"raw_title\"\:\".*?\"', html, re.S)
        tlt = re.findall(r'\"view_price\"\:\"[\d\.]*"', html, re.S)
        nik = re.findall(r'\"nick\"\:\".*?\"', html, re.S)
        # print(plt)
        for i in range(len(plt)):
            title = eval(plt[i].split(':')[1])
            price = eval(tlt[i].split(':')[1])
            nick = eval(nik[i].split(':')[1])
            # print(title, price)
            ilt.append([price, title, nick])
    except:
        print('')


def print_data(ilt):
    tplt = '{:4}\t{:4}\t{:4}\t{:4}'
    # print(tplt.format("序号", "价格", "商品名称", "店铺名"))
    # print(ilt)
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1], g[2]))
        time.sleep(1)


def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = get_html(url)
            # print(html)
            parse_page(infoList, html)
        except:
            continue
        break
    print_data(infoList)


if __name__ == '__main__':
    main()
