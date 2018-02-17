from socket import *

# 1、创建socket套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

# 2、从键盘接收要发送的数据
sendData = input("请输入要发送的数据:")

# 3、发送数据到指定的电脑上
udpSocket.sendto(sendData.encode(), ("192.168.247.1",8080))

# 4、关闭socket套接字
udpSocket.close()
