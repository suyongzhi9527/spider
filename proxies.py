import requests


req_header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

proxies = {
    "https": "182.35.80.229:9999"
}

res = requests.get("http://httpbin.org/ip", proxies=proxies)

print(res.status_code)
print(res.text)
