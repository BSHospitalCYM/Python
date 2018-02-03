import os

num = 68
ret = os.fork()
if ret == 0:
    num = 786
    print("子进程num=%d" % num)
else:
    num += 1
    print("主进程num=%d" % num)

print("num=%d" % num)


