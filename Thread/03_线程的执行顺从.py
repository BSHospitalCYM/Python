import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            print("我是子线程：%s---%d" % (self.name, i) )

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == "__main__":
    test()
