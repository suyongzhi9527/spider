import requests


req_header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

proxies = {"http":"http://113.195.169.215:9999"}

res = requests.get("http://www.baidu.com",proxies=proxies,headers = req_header)

print(res.status_code)