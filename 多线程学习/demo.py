import time
import threading

# 传统方式
# def coding():
#     for x in range(3):
#         print("正在写代码%s" % x)
#         time.sleep(1)


# def drawing():
#     for x in range(3):
#         print("正在画画%s" % x)
#         time.sleep(1)

# def main():
#     coding()
#     drawing()

# if __name__ == "__main__":
#     main()

# 多线程方式
# def coding():
#     for x in range(3):
#         print("正在写代码%s" % threading.current_thread()) # 查看当前线程名字
#         time.sleep(1)


# def drawing():
#     for x in range(3):
#         print("正在画画%s" %  threading.current_thread()) # 查看当前线程名字
#         time.sleep(1)


# def main():
#     t1 = threading.Thread(target=coding)
#     t2 = threading.Thread(target=drawing)

#     t1.start()
#     t2.start()

#     print(threading.enumerate()) # 查看线程数


class codingThread(threading.Thread):  # 继承Thread类，创建run方法，可以自动run方法中的代码
    def run(self):
        for x in range(3):
            print("正在写代码%s" % threading.current_thread())  # 查看当前线程名字
            time.sleep(1)


class drawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print("正在写画画%s" % threading.current_thread())  # 查看当前线程名字
            time.sleep(1)


def main():
    t1 = codingThread()
    t2 = drawingThread()

    t2.start()
    t1.start()


if __name__ == "__main__":
    main()
