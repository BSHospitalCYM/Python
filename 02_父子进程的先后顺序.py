import os
import time

ret = os.fork()
if ret == 0:
    print("子进程")
    time.sleep(10)
    print("子进程结束")
else:
    print("父进程")

print("程序执行完毕了")


