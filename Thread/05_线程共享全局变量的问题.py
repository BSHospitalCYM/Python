from threading import Thread
import time

g_num = 0

def work1():
    global g_num
    for i in range(1000000):
        g_num += 1
    print("work1子线程---g_num:%d" % g_num)

def work2():
    global g_num
    for i in range(1000000):
        g_num += 1
    print("work2子线程---g_num:%d" % g_num)

p1 = Thread(target=work1)
p1.start()
time.sleep(3)  # 增加延时保证子线程执行完毕
p2 = Thread(target=work2)
p2.start()
time.sleep(3)  # 增加延时保证子线程执行完毕
print("g_num最终值为：%d" % g_num)
