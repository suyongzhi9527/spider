import requests
import time

while True:
    question = input(':')
    girl = '莉莉'
    send_data = {
        'question': question,
        'api_key': 'd9d1e6f998285cc37f639692bed988da',
        'api_secret': '38izjq7ybegj'
    }

    api_url = 'http://i.itpk.cn/api.php'
    chat_content = requests.post(api_url, data=send_data)
    print(girl + ':' + chat_content.text)
    time.sleep(1)
