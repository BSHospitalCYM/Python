from multiprocessing import Pool
import os
import time
import random

def worker(num):
    t_start = time.time()
    print("第%d开始执行，进程号为%d" % (num, os.getpid()))
    time.sleep(1)
    t_stop = time.time()
    print("第%d执行完毕，耗时%0.2f" % (num, t_stop - t_start))

po = Pool(3)  # 定义一个进程池，最大进程数3

for i in range(5):
    print("---%d---" % i)
    # Pool.apply(要调用的目标函数,(传递给目标的参数元组,))
    # apply方式添加进程任务后，主进程就会被堵塞等待添加的进程执行完毕之后
    # 才会再次向进程池中添加任务，添加完后再次堵塞等待依次类推
    # 使用这种方式就相当于又回到了原来一个一个任务去执行的方式了，所以这种方式几乎不用
    po.apply(worker, (i,))

print("---start---")
po.close()  # 关闭进程池，关闭后po不再接收新的请求
po.join()  # 等待po中所有的子进程指向完成，必须放在close语句之后
print("---end---")
