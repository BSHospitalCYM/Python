import sys

if len(sys.argv) < 2:
    print("参数不正确,示例:ping 参数1 参数2")
else:
    print("参数1是:%s,参数2是:%s" % (sys.argv[1], sys.argv[2]))
