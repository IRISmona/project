# unix_send.py
from socket import *
# 确保两端是用的同一个套接字文件
sock_file = './sock_file'
sockfd = socket(AF_UNIX, SOCK_STREAM)
sockfd.connect(sock_file)
while True:
    msg = input('>>')
    if msg:
        sockfd.send(msg.encode())
        print(sockfd.recv(1024).decode())
    else:
        break
sockfd.close()
