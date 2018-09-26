# select_server.py
from select import select
from socket import *
# 创建套接字作为外卖的关注ＩＯ
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)

rlist = [s]
wlist = []
xlist = []

while True:
    # 提交监测我们关注的ＩＯ等待ＩＯ发生
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print('connect from ....', addr)
            rlist.append(c)  # 添加到关注列表
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
            else:
                print(data.decode())
                # 将客户端套接字放入wlist列表
                wlist.append(r)
    for w in ws:
        w.send(b'receive your message')
        wlist.remove(w)
    for x in xs:
        if x is s:
            s.close()
