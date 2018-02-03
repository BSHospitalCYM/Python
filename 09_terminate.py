from multiprocessing import Process
import time

def fun():
    while True:
        print("子进程")
        time.sleep(1)

p = Process(target = fun)
p.start()

i = 0
while i < 5:
    print("主进程%d" % i)
    time.sleep(1)
    i += 1
else:
    p.terminate()  # 不管子进程是否结束立即终止子进程

