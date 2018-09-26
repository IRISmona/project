# fork_pid.py
import os
# from time import sleep
pid = os.fork()
if pid < 0:
    print('create proess failed')
elif pid == 0:
    # sleep(1)
    # 获取子进程的ＰＩＤ
    print('child get pid:', os.getpid())
    # 获取父进程的ＰＩＤ
    print('child get parent pid:', os.getppid())
else:
    print('parent get child pid:', pid)
    print('parent get pid', os.getpid())
