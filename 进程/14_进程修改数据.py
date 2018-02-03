from multiprocessing import Process
from multiprocessing import Queue
import time

g_num = 34  # 定义全局变量

def fun1(q):
    if q.empty():
        print("fun1---Queue为空")
    else:
        value = q.get()
        print("---fun1---value=%d---" % value)
        value = 87
        q.put(value)
        time.sleep(1)

def fun2(q):
    if q.empty():
        print("fun2---Queue为空")
    else:
        value = q.get()
        print("---fun2---value=%d---" % value)
        value = value + 12
        q.put(value)
        time.sleep(1)

q = Queue()
q.put(g_num)

pw = Process(target=fun1, args=(q,))
pr = Process(target=fun2, args=(q,))

pw.start()
pw.join()

pr.start()
pr.join()

value = q.get()
print("---main value=%d" % value)
