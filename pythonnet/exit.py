# exit.py
import os
import sys
# os._exit(0)
try:
    sys.exit('hello world')
except SystemExit as e:
    print('退出', e)
# 结束进程后，不再执行后面的内容
print('process exit')
