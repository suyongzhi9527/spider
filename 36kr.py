import re
import json
import requests

url = 'https://36kr.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

res = requests.get(url,headers=headers)

html_str = res.content.decode()

ret = re.findall("<script>window.initialState=(.*?)</script>",html_str)[0]
ret = json.loads(ret)
print(ret["homeData"]["data"]["bannerLeft"]["data"][0])