from threading import Thread
import time

g_num = 100  # 定义全局变量

def work1():
    # 函数中访问全局变量需要使用global关键字声明
    global g_num
    for i in range(3):
        g_num += 1  # 修改全局变量的值
    print("work1子线程中全局变量g_num的值为：%d" % g_num)

def work2():
    global g_num
    print("work2子线程中全局变量g_num的值为：%d" % g_num)

print("---线程创建之前g_num的值为：%d" % g_num)

t1 = Thread(target=work1)
t1.start()

# 延时一会，保证t1线程中的事情做完
# 延时1秒的作用：延时1秒在计算机中是很长的时间，通过延时可以保证让某个子线程充分执行完毕
time.sleep(1)

t2 = Thread(target=work2)
t2.start()
