import requests


req_header = {
    'Cookie': 'BIDUPSID=A90697F0CBD4A97B4C31BB829EF8D884; PSTM=1581493404; BDRCVFR[VXHUG3ZuJnT]=mk3SLVN4HKm; BAIDUID=A90697F0CBD4A97B57867598E0E897EE:FG=1; delPer=0; BD_CK_SAM=1; PSINO=3; H_PS_PSSID=; BD_UPN=12314753; H_PS_645EC=de10N4MzyHRPcFo6sFPg2vI7m%2BLsSM8HiwDmB5F3ZbrRiC2ou4x4LkqWAoVZ8nGfN5F2dOa3fxAf; BDSVRTM=0; COOKIE_SESSION=63580_0_6_0_14_7_1_3_5_3_0_4_63583_0_2_0_1581493407_0_1581493405%7C9%230_0_1581493405%7C1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

proxies = {
    "https": "123.129.143.62:9999"
}

url = "http://www.baidu.com/s?wd=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6&rsv_spt=1&rsv_iqid=0xd6df1caa002f7e4e&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=ib&rsv_sug3=13&rsv_sug1=10&rsv_sug7=101"

res = requests.get(url, headers=req_header)
res.encoding = 'utf-8'
print(res.status_code)
print(res.text)
