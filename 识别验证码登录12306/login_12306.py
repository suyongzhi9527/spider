import base64
import re
import time

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(object):
    def __init__(self, username, password):
        # 图片验证码坐标
        self.coordinate = [[-105, -20], [-35, -20], [40, -20], [110, -20], [-105, 50], [-35, 50], [40, 50], [110, 50]]
        self.username = username
        self.password = password

    def login(self):
        # 初始化浏览器对象
        driver = webdriver.Chrome("E:\chromedriver_win32\chromedriver.exe")
        # 12306登陆页面
        login_url = "https://kyfw.12306.cn/otn/resources/login.html"
        # 设置浏览器长宽
        driver.set_window_size(1200, 900)
        # 打开登陆页面
        driver.get(login_url)
        # 找到账号登陆按钮
        account = driver.find_element_by_class_name("login-hd-account")
        # 点击按钮
        account.click()
        # 找到用户名输入框
        userName = driver.find_element_by_id("J-userName")
        # 输入用户名
        userName.send_keys(self.username)
        # 找到密码输入框
        passWord = driver.find_element_by_id("J-password")
        # 输入密码
        passWord.send_keys(self.password)
        self.driver = driver

    def getVerifyImage(self):
        try:
            # 找到图片验证码标签
            img_element = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((By.ID, "J-loginImg"))
            )

        except Exception as e:
            print(u"验证码图片未加载！")
        # 获取图片验证码的src属性，就是图片base64加密后的数据
        base64_str = img_element.get_attribute("src").split(",")[-1]
        # base64解码得到图片的数据
        imgdata = base64.b64decode(base64_str)
        # 存入img.jpg
        with open('img.jpg', 'wb') as file:
            file.write(imgdata)
        self.img_element = img_element

    def getVerifyResult(self):
        # 12306验证码识别网址
        url = "http://littlebigluo.qicp.net:47720/"
        # 发送post请求把图片数据带上
        response = requests.request("POST", url, data={"type": "1"}, files={'pic_xxfile': open('img.jpg', 'rb')})
        result = []
        print(response.text)
        # 返回识别结果
        for i in re.findall("<B>(.*)</B>", response.text)[0].split(" "):
            result.append(int(i) - 1)
        self.result = result
        print(result)

    def moveAndClick(self):
        try:
            # 创建鼠标对象
            Action = ActionChains(self.driver)
            for i in self.result:
                # 根据获取的结果取坐标选择图片并点击
                Action.move_to_element(self.img_element).move_by_offset(self.coordinate[i][0],
                                                                        self.coordinate[i][1]).click()
            Action.perform()
        except Exception as e:
            print(e)

    def submit(self):
        # 点击登陆按钮
        self.driver.find_element_by_id("J-login").click()

    def __call__(self):
        self.login()
        time.sleep(3)
        self.getVerifyImage()
        time.sleep(1)
        self.getVerifyResult()
        time.sleep(1)
        self.moveAndClick()
        time.sleep(1)
        self.submit()
        time.sleep(1000)


if __name__ == '__main__':
    # 用户名和密码
    username = '******'
    password = '******'
    Login(username, password)()
