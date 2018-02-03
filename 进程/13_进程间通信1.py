from multiprocessing import Process
from multiprocessing import Queue
import time

# 写数据进程执行的函数
def write(q):
    for value in ["A", "B", "C"]:
        print("写入数据：%s到Queue中" % value)
        if q.full():  # 判断Queue队列消息是否已满
            print("Queue队列中已满")
        else:
            q.put(value)  # 向Queue队列中写入消息
            time.sleep(1)

# 读数据进程执行的函数
def read(q):
    while True:
        if not q.empty():  # 如果Queue队列消息不为空
            value = q.get()  # 从Queue队列中获取一条消息
            print("获取数据：%s" % value)
            time.sleep(1)
        else:
            print("Queue队列中没有消息")
            break

q = Queue(3)  # 创建Queue消息队列，最多可接收3个消息
# 父进程创建子进程并将Queue对象实例传递给子进程
pw = Process(target=write, args=(q,))
pr = Process(target=read, args=(q,))

pw.start()  # 启动写入数据子进程
pw.join()  # 等待写入数据子进程完毕

pr.start()  # 启动读取数据子进程
pr.join()  # 等待读取数据子进程完毕

print("所有数据都写入并且读取完毕")
