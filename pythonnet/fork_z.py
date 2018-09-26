# fork_z.py
import os
from time import sleep
pid = os.fork()
if pid<0:
    print('create process failed')
elif pid == 0:
    print('child process:',os.getpid())
    print('child process exit')
else:
    print('parent process')
    while True:
        pass
