from multiprocessing import Pool
import time
import os

def test():
    print("---进程池中的进程---进程号=%d,父进程号=%d---" % (os.getpid(), os.getppid()))
    for i in range(3):
        print("---%d---" % i)
        time.sleep(1)
    return "haha"

def test2(args):
    print("---调用函数---进程号=%d" % os.getpid())
    print("---调用函数---参数=%s" % args)

pool = Pool(3)
pool.apply_async(test, callback=test2)

while True:
    time.sleep(1)
    print("----主进程pid=%d---" % os.getpid())
