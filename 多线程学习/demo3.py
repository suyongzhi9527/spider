import threading

VALUE = 0

Lock = threading.Lock() # 创建一个锁对象

def add_value():
    global VALUE
    Lock.acquire() # 上锁
    for i in range(1000000):
        VALUE += 1
    Lock.release() # 解锁
    print(VALUE)

def main():
    for i in range(2):
        t = threading.Thread(target = add_value)
        t.start()

if __name__ == "__main__":
    main()