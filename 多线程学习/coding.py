import threading
import time
from queue import Queue


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程ID%s: %s" % (self.threadID, self.name))
        start_coding(self.name, self.counter, 10)
        print("退出线程ID%s: %s" % (self.threadID, self.name))


def start_coding(Pythoner, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s 开始敲代码 %s" % (Pythoner, time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime())))
        counter -= 1


t1 = MyThread(1, "小苏", 1)
t2 = MyThread(2, "小妞", 2)
t1.start()
t2.start()

t1.join()
t2.join()
print("敲代码结束!")
