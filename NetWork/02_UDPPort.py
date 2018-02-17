from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

# UDP每发送一次数据都要指定IP地址和端口号
udpSocket.sendto("aaa".encode(), ("192.168.247.1",8080))
udpSocket.sendto("bbb".encode(), ("192.168.247.1",8080))
udpSocket.sendto("ccc".encode(), ("192.168.247.1",8080))

udpSocket.close()
