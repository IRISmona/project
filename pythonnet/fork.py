# fork.py
import os
import time
print('**********************')
a = 1
pid = os.fork()
if pid < 0:
    print('创建进程失败')
elif pid == 0:
    print('这是新的进程')
    print('a=', a)
    a=1000
else:
    time.sleep(1)
    print('这是原有进程')
    print('parent a=',a)
print('演示完毕')
