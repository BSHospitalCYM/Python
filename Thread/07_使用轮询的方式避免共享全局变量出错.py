from threading import Thread
import time

g_num = 0
g_flg = 0

def work1():
    global g_num
    global g_flg
    
    if not g_flg:
        for i in range(1000000):
            g_num += 1
        g_flg = 1
        print("work1子线程---g_num:%d" % g_num)

def work2():
    global g_num
    global g_flg

    while True:
        if g_flg:
            for i in range(1000000):
                g_num += 1
            print("work2子线程---g_num:%d" % g_num)
            break

p1 = Thread(target=work1)
p1.start()
p2 = Thread(target=work2)
p2.start()
