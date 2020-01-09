import time
import threading
from queue import Queue

class CustomThread(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.__queue = queue

    def run(self):
        while True:
            q_method = self.__queue.get()
            q_method()
            self.__queue.task_done()


def moyu():
    print(" 开始摸鱼 %s" % (time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))

def queue_pool():
    queue = Queue(5)
    for i in range(queue.maxsize):
        t = CustomThread(queue)
        t.setDaemon(True)
        t.start()

    for i in range(20):
        queue.put(moyu)
    queue.join()


if __name__ == "__main__":
    queue_pool()