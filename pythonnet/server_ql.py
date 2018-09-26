# server_ql.py
from socket import *
from select import *
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind('0.0.0.0', 8888)
s.listen(5)
r = [s]
w = []
x = []
d = {}
while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print('connect from ....', addr)
            rlist.append(c)  # 添加到关注列表
            wlist.append(c)
            name = r.recv(1024).decode()
            if name in d:
                print('该用户已经在群里了')
            else:
                d[name] = addr
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
        w.send()
        wlist.remove(w)
    for x in xs:
        if x is s:
            s.close()
