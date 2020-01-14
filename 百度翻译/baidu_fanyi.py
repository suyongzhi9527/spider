import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36"
}

content = input("请输入翻译的内容:")

data = {
    'i': content,
    'from': 'AUTO',
    'to': 'AUTO',
    'doctype': 'json'
}

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

res = requests.post(url, data=data, headers=headers)

# print(res.status_code)
print(type(res.text))
# dict_ret = json.loads(res.text)
# result = dict_ret["translateResult"][0][0]["tgt"]
# print("翻译结果:{}".format(result))
