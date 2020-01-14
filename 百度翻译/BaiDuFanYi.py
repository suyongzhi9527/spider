import requests
import json


class BaiduFanyi:
    def __init__(self, trans_data):
        self.trans_data = trans_data
        self.lang_detect_url = "httP://fanyi.baidu.com/langdetect"
        self.trans_url = "http://fanyi.baidu.com/basetrans"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36"
        }

    def parse_url(self,url,data):
        res = requests.get(url, data=data, headers=self.headers)
        return json.loads(res.content.decode())

    def get_ret(self,dict_res):
        ret = dict_res["trans"][0]["dst"]
        print("翻译结果为:",ret)

    def run(self):
        # 1.获取语言类型
        # 1.1 准备post的url地址,post_data
        lang_detect_data = {"query": self.trans_data}
        # 1.2 发送post请求，获取响应
        lang = self.parse_url(self.lang_detect_url,lang_detect_data)["msg"]
        print(lang)
        # 1.3 提取语言类型
        # 2.准备post的数据
        trans_data = {"query":self.trans_data,"form":"zh","to":"en"} if lang == "zh" else {"query":self.trans_data,"form":"en","to":"zh"}
        # 3.发送请求，获取响应
        dict_res = self.parse_url(self.trans_url,trans_data)
        # 4.提取翻译的结果
        self.get_ret(dict_res)


if __name__ == '__main__':
    trans_str = input("请输入翻译的内容:")
    fanyi = BaiduFanyi(trans_str)
    fanyi.run()
