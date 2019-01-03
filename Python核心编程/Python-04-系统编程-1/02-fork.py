import os
ret = os.fork()
print(ret)
if ret > 0:#ret==0时，执行子进程，否则执行父进程
    print("父进程--%d"%os.getpid())
else:
    print("子进程--%d-%d"%(os.getpid(),os.getppid()))