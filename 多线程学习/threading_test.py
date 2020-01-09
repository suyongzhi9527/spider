import threading
import time


def coding():
    for i in range(3):
        print("%s正在写代码" % threading.current_thread())
        time.sleep(1)


def run():
    for i in range(3):
        print("%s正在运动" % threading.current_thread())
        time.sleep(1)


def main():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=run)
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
