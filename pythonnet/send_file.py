# send_file.py
from socket import *
s = socket(AF_INET, SOCK_STREAM)
# 发起链接
server_addr = ('176.221.18.227', 8888)
s.connect(server_addr)
try:
    while True:
        filename = input('你要发送的文件名是：')
        if filename == '':
            break
        f = open(filename, 'rb')
        b = f.read()
        # print(b)
        s.send(b)
        print('发送文件成功')
        data = s.recv(1024)
        print('接收到：', data.decode())
        f.close()
# 关闭套接字
    s.close()
except:
    print('发送文件失败')
