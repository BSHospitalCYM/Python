from multiprocessing import Process
import time

def fun():
    i = 0
    while i<5:
        print("子进程 i=%d" % i)
        time.sleep(1)
        i += 1

p = Process(target = fun)
p.start()
# 等待2秒子进程结束，2秒后子进程还不结束那么主进程继续向下执行
p.join(2)

print("子进程结束了，主进程结束了")


