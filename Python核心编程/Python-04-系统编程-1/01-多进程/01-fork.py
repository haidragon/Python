import os
import time

ret = os.fork()#此时创建一个子进程
if ret == 0:
    while True:
        print("---1---")
        time.sleep(1)
else:
    while True:
        print("---2---")
        time.sleep(1)