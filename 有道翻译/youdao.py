import requests
import json
import time
import random
import hashlib
import tkinter as tk

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36",
    "Referer": "http://fanyi.youdao.com/?keyfrom=dict2.top",
    "Cookie": "OUTFOX_SEARCH_USER_ID=-237170162@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=994120418.9853693; _ntes_nnid=e61ea52dfbf7f13653e3674375c16f15,1575719676416; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcwKpPv5EsB1aLHyuvax; ___rl__test__cookies=1580905690483"
}

r = str(int(time.time() * 1000))
random_num = random.randint(0, 9)
i = r + str(random_num)


def data_new(e):
    str_sign = "fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj"
    md5 = hashlib.md5()
    md5.update(str_sign.encode())
    sign = md5.hexdigest()
    data = {
        'i': e,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': i,
        'sign': sign,
        'ts': r,
        'bv': '75a84f6fbcebd913f0a4e81b6ee54608',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }
    return data


root = tk.Tk()
var = tk.StringVar()
root.title('GUI翻译')  # 设置窗口标题
root.geometry('500x150')  # 设置窗口大小
l2 = tk.Label(root, fg="blue", text='GUI翻译:', font=('Arial', 15))
l2.grid(row=1, column=0)
t2 = tk.Entry(root, text='', width=40)
t2.grid(row=1, column=1)
l1 = tk.Label(root, fg="blue", text='翻译结果:', font=('Arial', 15))
l1.grid(row=2, column=0)
t1 = tk.Entry(root, text='', width=40, textvariable=var)
t1.grid(row=2, column=1)


def get_value():
    content = t2.get()
    data = data_new(content)
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    response = requests.post(url, data=data, headers=headers)
    dict_ret = json.loads(response.text)
    result = dict_ret['translateResult'][0][0]['tgt']
    var.set(result)


def delete_text():
    t2.delete(0, 'end')


b1 = tk.Button(root, text='翻译', width=8, fg="green", command=get_value)
b1.grid(row=1, column=7)
b2 = tk.Button(root, text='清除', width=8, fg="red", command=delete_text)
b2.grid(row=1, column=8)
root.mainloop()
