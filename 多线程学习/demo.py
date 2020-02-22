import time
import threading


class Threading(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "我是线程" + self.name + "@" + str(i)
            print(msg)

        self.login()
        self.register()

    def login(self):
        print("这是登录代码")

    def register(self):
        print("这是注册代码")


if __name__ == '__main__':
    t = Threading()
    t.start()
