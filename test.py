import requests

# r = requests.get("https://api.github.com/events")

# r = requests.post('https://httpbin.org/post', data = {'key':'value'})
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('https://httpbin.org/get', params=payload)
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)