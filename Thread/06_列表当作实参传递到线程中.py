from threading import Thread
import time

def work1(nums):
    nums.append(44)
    print("work1子线程:", nums)

def work2(nums):
    time.sleep(1)
    print("work2子线程:", nums)

g_nums = [11, 22, 33]
p1 = Thread(target=work1, args=(g_nums,))
p1.start()
p2 = Thread(target=work2, args=(g_nums,))
p2.start()
