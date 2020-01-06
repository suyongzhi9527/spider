import threading
import random
import time

gMoney = 1000
gTotalTimes = 10
gCondition = threading.Condition()
gTimes = 0


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100, 1000)
            gCondition.acquire()
            if gTimes >= 10:
                gCondition.release()
                break
            gMoney += money
            print("%s生产了%d元钱,剩余%d元钱" %
                  (threading.current_thread(), money, gMoney))
            gTimes += 1
            gCondition.notify_all()
            gCondition.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            gCondition.acquire()
            while gMoney < money:
                if gTimes >= gTotalTimes:
                    gCondition.release()
                    return 
                print("%s消费了%d元钱,剩余%d元钱,不足!" % (threading.current_thread(),gMoney,money))
                gCondition.wait()
            gMoney -= money
            print("%s消费了%d元钱,剩余%d元钱" %
                  (threading.current_thread(), money, gMoney))
            gCondition.release()
            time.sleep(0.5)


def main():
    for i in range(3):
        t = Consumer(name="消费者线程%s" % i)
        t.start()

    for i in range(5):
        t = Producer(name="生产者线程%s" % i)
        t.start()


if __name__ == "__main__":
    main()
