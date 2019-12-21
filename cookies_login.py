import json
import requests

url = "https://m.douban.com/rexxar/api/v2/movie/suggestion?start=0&count=10&new_struct=1&with_review=1&for_mobile=1"

res = requests.get(url)

print(res.status_code)
dict_ret = json.loads(res.content.decode())
print(dict_ret)