import re
import json
import csv
import requests

url = 'https://36kr.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

res = requests.get(url, headers=headers)

html_str = res.content.decode()

ret = re.findall("<script>window.initialState=(.*?)</script>", html_str)[0]
ret = json.loads(ret)
item_list = []
for i in range(len(ret["homeData"]["data"]["latestArticle"]["data"])):
    item = {}
    item['title'] = ret["homeData"]["data"]["latestArticle"]["data"][i]["post"]["title"]
    item['cover'] = ret["homeData"]["data"]["latestArticle"]["data"][i]["post"]["cover"]
    item['summary'] = ret["homeData"]["data"]["latestArticle"]["data"][i]["post"]["summary"]
    item['published_at'] = ret["homeData"]["data"]["latestArticle"]["data"][i]["post"]["published_at"]
    item_list.append(item)

    with open("36kr.csv","w",encoding="utf-8-sig",newline="") as f:
        headers = ['title','cover','summary','published_at']
        writer = csv.DictWriter(f,headers)
        writer.writeheader()
        writer.writerows(item_list)
        # for item_li in item_list:
        #     f.write(json.dumps(item_li,ensure_ascii=False,indent=2))
