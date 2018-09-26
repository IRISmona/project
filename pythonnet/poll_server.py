# 1.py
from select import *
from socket import *
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)
# 创建poll对象
p = poll()
# fileno--->IO对象的字典
fdmap = {s.fileno(): s}
# 注册关注IO
p.register(s, POLLIN | POLLERR)

while True:
    # 进行ＩＯ监控
    events = p.poll()
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print('connect from ...', addr)
            # 添加新的关注对象
            p.register(c, POLLIN | POLLHUP)
            fdmap[c.fileno()] = c
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                # 客户端退出，从关注事件移除
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print(data.decode())
                fdmap[fd].send(b'receive')
                
