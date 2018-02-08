import threading
import time

class MyThread1(threading.Thread):
    def run(self):
        if mutexA.acquire():
            print(self.name + "---d01---up---")
            time.sleep(1)

            # 添加超时时间5秒避免死锁   
            if mutexB.acquire(True, 5):
                print(self.name + "---d01---down---")
                mutexB.release()
            mutexA.release()

class MyThread2(threading.Thread):
    def run(self):
        if mutexB.acquire():
            print(self.name + "---d02---up---")
            time.sleep(1)

            # 添加超时时间5秒避免死锁
            if mutexA.acquire(True, 5):
                print(self.name + "---d02---down---")
                mutexA.release()
            mutexB.release()

mutexA = threading.Lock()
mutexB = threading.Lock()

t1 = MyThread1()
t2 = MyThread2()
t1.start()
t2.start()
