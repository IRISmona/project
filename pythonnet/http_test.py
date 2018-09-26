# http_test.py
from socket import *
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8000))
s.listen(5)
while True:
    c, addr = s.accept()
    print('connect from', addr)
    data = c.recv(4096)
    print('--------------------------')
    print(data)  # 浏览器发来的http请求
    print('--------------------------')
    # 组织相应内容
    data='''HTTP/1.1 200 OK
    Content-Encoding:gzip
    Content-Type:text/html

    <h1>welcome to tedu<h1/>
    '''
    c.send(data.encode())
    c.close()
s.close()
