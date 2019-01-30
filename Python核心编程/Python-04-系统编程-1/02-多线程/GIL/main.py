from ctypes import *
from threading import Thread
#加载动态库
lib = cdll.LoadLibrary("./libDeadLoop.so")
#创建一个子线程
for i in range(8):
    t = Thread(target=lib.DeadLoop)
    t.start()

#主线程
while True:
    pass