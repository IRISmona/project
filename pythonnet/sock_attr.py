# sock_attr.py
from socket import *
s = socket()
# 设置端口立即释放
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 获取套接字选项值
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))
# 获取套接字地址族类型
print(s.family)  # AddressFamily.AF_INET
# 获取套接字的类型
print(s.type)  # SocketKind.SOCK_STREAM
# 获取套接字的绑定地址
s.bind(('127.0.0.1', 8888))
print(s.getsockname())  # ('127.0.0.1',8888)
# 获取套接字的文件描述符
print(s.fileno())  # 3
# 获取客户端连接套接字的对应地址
# print(s.getpeername())  # 报错，需要客户端连接，才可以调用
s.listen(5)
while True:
    c, addr = s.accept()
    print('connect from', c.getpeername())  # ('127.0.0.1', 47724)
    c.recv(1024)
