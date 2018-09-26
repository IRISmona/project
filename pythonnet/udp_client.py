# udp_client.py
from socket import *
import sys
try:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    sockfd = socket(AF_INET, SOCK_DGRAM)
    while True:
        data = input('消息：')
        if not data:
            break
        sockfd.sendto(data.encode(), ADDR)
        data, addr = sockfd.recvfrom(1024)
        print('从服务器收到：', data.decode())
    sockfd.close()
except IndexError:
    print('''
        argv is error!
        run as
        python3 udp_client.py 127.0.0.1 8888''')


# tarena@tedu:~/计算机/pythonnet$ python3 udp_client.py 127.0.0.1 8888
# 消息：nihao
# 从服务器收到： 收到你的消息
# 消息：hello
# 从服务器收到： 收到你的消息
# 消息：
