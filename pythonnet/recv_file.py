# send_file.py
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)
try:
    while True:
        c, addr = s.accept()
        print('connect from ',addr)
        while True:
            filename = input('文件保存为：')
            f = open(filename, 'wb')
            b = c.recv(4050)
            # print(b)
            f.write(b)
            n = c.send(b'receise you message')
            f.close()
        c.close()
    s.close()
except:
    print('没有接收到任信息')
