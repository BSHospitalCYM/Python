from threading import Thread
from threading import Lock
import time

g_num = 0

def work1():
    global g_num

    lock.acquire(True) # 加锁
    for i in range(1000000):
        g_num += 1
    lock.release() # 释放锁
    g_flg = 1
    print("work1子线程---g_num:%d" % g_num)

def work2():
    global g_num

    lock.acquire(True)
    for i in range(1000000):
        g_num += 1
    lock.release()
    print("work2子线程---g_num:%d" % g_num)

lock = Lock() # 创建互斥锁对象，这个锁默认是没有上锁的
p1 = Thread(target=work1)
p1.start()
p2 = Thread(target=work2)
p2.start()
