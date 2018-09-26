# tcp_server.py
from socket import *
# 创建套接字
sockfd = socket(AF_INET, SOCK_STREAM)
# 绑定本机地址
sockfd.bind(('0.0.0.0', 8888))
# 设置监听
sockfd.listen(5)
# 等待接受连接
print('waiting for connect....')
connfd, addr = sockfd.accept()
print('connect from', addr)
while True:
    try:
        data = connfd.recv(1024).decode()
    # print(data)
        if data == '##':
            break
        elif data == '**':
            connfd, addr = sockfd.accept()
            continue
    finally:
        print(data)
        a = input('回复：')
        # n = connfd.send(b'receive your message')
        n = connfd.send(a.encode('utf-8'))
        print('发送了%d字节的消息' % n)
# 关闭套接字
connfd.close()
sockfd.close()
