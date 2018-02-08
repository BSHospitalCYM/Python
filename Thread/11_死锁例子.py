import threading
import time

class MyThread1(threading.Thread):
    def run(self):
        if mutexA.acquire():
            print(self.name + "---d01---up---")
            time.sleep(1)

            if mutexB.acquire():
                print(self.name + "---d01---down---")
                mutexB.release()
            mutexA.release()

class MyThread2(threading.Thread):
    def run(self):
        if mutexB.acquire():
            print(self.name + "---d02---up---")
            time.sleep(1)
           
            if mutexA.acquire():
                print(self.name + "---d02---down---")
                mutexA.release()
            mutexB.release()

mutexA = threading.Lock()
mutexB = threading.Lock()

t1 = MyThread1()
t2 = MyThread2()
t1.start()
t2.start()
