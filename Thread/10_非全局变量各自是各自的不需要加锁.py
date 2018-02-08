'''
import threading
import time

# 自定义线程类继承自threading.Thread类
class MyThread(threading.Thread):
    # 重写构造方法
    def __init__(self, name, num, sleepTime):
        threading.Thread.__init__(self)
        self.name = name
        self.num = num
        self.sleepTime = sleepTime
    # 重写run方法
    def run(self):
        self.num += 1
        # name属性中保存的是当前线程的名字，默认从Thread-1开始
        print("我是子线程:%s---局部变量num:%d" % (self.name, self.num) )
        time.sleep(self.sleepTime)

if __name__ == "__main__":
    # 创建自定义线程类实例对象
    t1 = MyThread("子线程t1", 100, 2)
    t1.start()  # 启动线程

    t2 = MyThread("子线程t2", 200, 1)
    t2.start()
'''

import threading
from time import sleep

def test(sleepTime):
    num = 1
    # threading.current_thread().name 返回执行线程对象的名字
    objName = threading.current_thread().name
    if objName == "Thread-1":
        sleep(sleepTime)
        num += 1
        # threading.current_thread()方法返回当前执行线程的对象
        print("Thread-1子线程:%s---局部变量num:%d" % (threading.current_thread(), num))
    elif objName == "Thread-2":
        sleep(sleepTime)
        num += 100
        print("Thread-2子线程:%s---局部变量num:%d" % (threading.current_thread(), num))

t1 = threading.Thread(target=test, args=(2,))
t2 = threading.Thread(target=test, args=(1,))
t1.start()
t2.start()
