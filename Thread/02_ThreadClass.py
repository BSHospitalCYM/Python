import threading
import time

# 自定义线程类继承自threading.Thread类
class MyThread(threading.Thread):
    # 重写run方法
    def run(self):
        for i in range(3):
            # name属性中保存的是当前线程的名字，默认从Thread-1开始
            print("我是子线程：%s---%d" % (self.name, i) )
            time.sleep(1)

if __name__ == "__main__":
    # 创建自定义线程类实例对象
    t1 = MyThread()
    t1.start()  # 启动线程

    t2 = MyThread()
    t2.start()
