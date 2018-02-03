from multiprocessing import Manager
from multiprocessing import Pool
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

q = Manager().Queue() # 使用Manager中的Queue来初始化
q.put(g_num)

po = Pool()
po.apply(fun1,(q,))
po.apply(fun2,(q,))
po.close()
po.join()

value = q.get()
print("---main value=%d" % value)
