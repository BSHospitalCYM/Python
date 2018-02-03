from multiprocessing import Process
import time
import os

class Process_Class(Process):
    # 因为Process父类本身也有__init__方法，我们定义的类相当于重写了Process父类的__init__方法
    # 但是这样就会带来一个问题，我们并没有完全的初始化一个Process类，所以就不能使用从这个类
    # 继承的一些方法，所以我们需要将继承类本身传递给Process父类的__init__方法，完成父类的初
    # 始化工作
    def __init__(self, interval):
        Process.__init__(self)  # 调用父类的__init__方法，并将实例传递给父类完成父类的初始化
        self.interval = interval

    # 重写Process类的run()方法
    def run(self):
        print("子进程(%s)开始执行，父进程为(%s)" % (os.getpid(), os.getppid()))
        t_start = time.time()  # 记录开始时间
        time.sleep(self.interval)
        t_stop = time.time()  #记录结束时间
        print("子进程(%s)执行结束，耗时%0.2f秒" % (os.getpid(), t_stop - t_start))

t_start = time.time()

print("当前程序进程(%s)" % os.getpid())
p1 = Process_Class(2)  # 创建自定义进程类的实例对象
# 对于一个不包含target属性的Process类执行start()方法，就会运行这个类中的run()方法
p1.start()  # 启动进程实例，会运行类中的run()方法
p1.join()  # 主进程等待子进程结束

t_stop = time.time()
print("主进程(%s)执行结束，耗时%0.2f秒" % (os.getpid(), t_stop - t_start))
