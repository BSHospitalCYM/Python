from threading import Thread, Lock
from time import sleep

g_num = 0

class Task1(Thread):
    def run(self):
        global g_num
        while True:
            if lock1.acquire():
                g_num += 1
                print("---Task1----%d" % g_num)
                sleep(0.5)
                lock2.release()


class Task2(Thread):
    def run(self):
        global g_num
        while True:
            if lock2.acquire():
                g_num += 1
                print("---Task2----%d" % g_num)
                sleep(0.5)
                lock3.release()


class Task3(Thread):
    def run(self):
        global g_num
        while True:
            if lock3.acquire():
                g_num += 1
                print("---Task3----%d" % g_num)
                sleep(0.5)
                lock1.release()

# 使用Lock创建出的锁默认没有锁上
lock1 = Lock()

lock2 = Lock()
lock2.acquire()

lock3 = Lock()
lock3.acquire()

t1 = Task1()
t2 = Task2()
t3 = Task3()

t1.start()
t2.start()
t3.start()
             
