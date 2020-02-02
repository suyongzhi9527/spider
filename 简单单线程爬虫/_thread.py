import threading
import time


class myThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("开始:" + self.name)
        print_time(self.name, self.delay)
        print("退出:", self.name)


def print_time(threadName, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        print(threadName, time.ctime())
        count += 1


threads = []

# 创建新线程
thread1 = myThread("Thread-1", 1)
thread2 = myThread("Thread-2", 2)

# 开始新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有的线程完成
for i in threads:
    i.join()

print("退出主线程!")
