# udp_server.py
from socket import *
# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
# 绑定地址
server_addr = ('0.0.0.0', 8888)
sockfd.bind(server_addr)
# 消息收发
while True:
    data, addr = sockfd.recvfrom(5)
    print('receive from %s:%s' % (addr, data.decode()))
    sockfd.sendto('收到你的消息'.encode(), addr)
sockfd.close()
