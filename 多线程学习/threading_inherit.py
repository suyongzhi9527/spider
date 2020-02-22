import threading
import time


class coding(threading.Thread):
    def run(self):
        for i in range(3):
            print("线程%s正在敲代码" % threading.current_thread())
            time.sleep(2)


class run(threading.Thread):
    def run(self):
        for i in range(3):
            print("线程%s正在运动呢" % threading.current_thread())
            time.sleep(2)


def main():
    t1 = coding()
    t1.start()
    t2 = run()
    t2.start()


if __name__ == "__main__":
    main()
