# broadcast_send.py   广播
from socket import *
from time import sleep
# 设置目标地址
dest = ('176.221.18.255', 9999)
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
    sleep(2)
    s.sendto('来呀,打我呀'.encode(), dest)
s.close()
