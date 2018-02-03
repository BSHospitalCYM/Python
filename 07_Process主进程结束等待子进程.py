from multiprocessing import Process
import time

def fun():
    while True:
        print("子进程")
        time.sleep(1)

p = Process(target = fun)
p.start()  # 让这个进程开始执行fun函数里面的代码

print("主进程结束")


