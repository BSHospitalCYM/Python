import os

ret = os.fork()
if ret < 0:
    print("fork调用失败")
elif ret == 0:
    print("我是子进程：%s,我的父进程是：%s" % (os.getpid(), os.getppid()))
else:
    print("我是父进程：%s,我的子进程是：%s" % (os.getpid(), ret))



