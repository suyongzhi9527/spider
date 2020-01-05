import threading

# 多线程共享全局变量的问题
# 多线程都是同一个进程中运行的，因此在进程中的全局变量所有的线程都是可以共享的，这就造成一个问题
# 因为线程的执行是没有顺序的，有可能会造成数据错乱

VALUE = 0
gLock = threading.Lock() # 创建一个锁，保证数据的完整性
def add_value():
    global VALUE
    gLock.acquire() # 上锁
    for i in range(1000000):
        VALUE += 1
    gLock.release() # 释放锁
    print(VALUE)

def main():
    for i in range(2):
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == "__main__":
    main()