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

for i in range(0, 10):
    # Pool.apply_async(要调用的目标函数,(传递给目标的参数元组,))
    # 每次循环将会用空闲出来的子进程去调用目标函数
    po.apply_async(worker, (i,))

print("---start---")
po.close()  # 关闭进程池，关闭后po不再接收新的请求
po.join()  # 等待po中所有的子进程指向完成，必须放在close语句之后
print("---end---")
