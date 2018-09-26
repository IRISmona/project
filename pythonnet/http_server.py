# http_server.py
from socket import *


def handelClient(connfd):
    requset = connfd.recv(4096)
    requset_lines = requset.splitlines()
    for line in requset_lines:
        print(line.decode())
    try:
        f = open('index.html')
    except IOError:
        response = 'HTTP/1.1 404 not found\r\n'
        response += '\r\n'  # 空行
        response += '===sorry not found==='
    else:
        response = 'HTTP/1.1 200 not ok\r\n'
        response += '\r\n'  # 空行
        response += f.read()
    finally:
        # 发送给浏览器
        connfd.send(response.encode())


def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(('0.0.0.0', 8888))
    sockfd.listen(3)
    print('listen to the port 8888')
    while True:
        connfd, addr = sockfd.accept()
        # 处理请求
        handelClient(connfd)
        connfd.close()


if __name__ == '__main__':
    main()
