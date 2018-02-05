import threading
import time

def say():
    print("你好Python")
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        # 创建一个线程，线程执行的函数是say
        t = threading.Thread(target=say)
        t.start()  # 启动线程
