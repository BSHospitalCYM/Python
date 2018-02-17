from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

# 绑定本地的相关信息，如果不绑定则系统会随机分配
# IP地址一般不用写，表示本机的任何一个IP
udpSocket.bind(("", 7788))

# 1024表示本次接收的最大字节数
recvData = udpSocket.recvfrom(1024)

print("接收的数据:%s" % recvData)

udpSocket.close()
