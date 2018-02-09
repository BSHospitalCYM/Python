import threading
import time

# Python 2.x中
# from Queue import Queue
# Python 3.x中
from queue import Queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            # queue.qsize()方法返回当前队列中包含消息的数量
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = self.name + "线程生成数据:" + str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(50):
                    msg = self.name + "线程处理数据:" + queue.get()
                    print(msg)
            time.sleep(0.5)

queue = Queue()

for i in range(100):
    queue.put("数据" + str(i))
for i in range(2):
    p = Producer()
    p.start()
for i in range(5):
    c = Consumer()
    c.start()
