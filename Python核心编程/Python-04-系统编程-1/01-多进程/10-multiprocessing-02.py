from multiprocessing import Process
import os
import time

def work1(interval):
    print("work1父进程(%d),当前进程(%d)"%(os.getppid(),os.getpid()))
    t_startTime = time.time()
    time.sleep(interval)
    t_endTime = time.time()
    print("work1执行时间%0.3f"%(t_endTime- t_startTime))

def work2(interval):
    print("work2父进程(%d),当前进程(%d)"%(os.getppid(),os.getpid()))
    t_startTime = time.time()
    time.sleep(interval)
    t_endTime = time.time()
    print("work2执行时间%0.3f"%(t_endTime- t_startTime))


if __name__ == "__main__":
    print("当前进程id=%s"%os.getpid())

    p1 = Process(target=work1,args=(2,))
    p2 = Process(target=work2,name="work2-chanage",args=(1,))

    p1.start()
    p2.start()

    print("p2.is_alive()=%s"%p2.is_alive())

    print("p1.name = %s"%p1.name)
    print("p1.pid=%s"%p1.pid)
    print("p2.name = %s" % p2.name)
    print("p2.pid=%s" % p2.pid)

    p1.join(1)#若这里是p1.join(1)，主进程只会等待p11秒，但是p1需要两秒执行，所以p1会在父进程执行完之后结束，
    #所以print("p1.is_alive()=%s" % p1.is_alive())打印p1状态时为True
    #结果会是：
    '''当前进程id=209796
    p2.is_alive()=True
    p1.name = Process-1
    p1.pid=214504
    p2.name = work2-chanage
    p2.pid=214564
    p1.is_alive()=True
    work1父进程(209796),当前进程(214504)
    work2父进程(209796),当前进程(214564)
    work2执行时间1.000
    work1执行时间2.016
    '''
    #若这里是p1.join(),则主进程会等待p1执行完毕再向下执行，所以最终打印p1状态时为False
    #执行结果如下
    '''当前进程id=190696
    p2.is_alive()=True
    p1.name = Process-1
    p1.pid=203252
    p2.name = work2-chanage
    p2.pid=211680
    work1父进程(190696),当前进程(203252)
    work2父进程(190696),当前进程(211680)
    work2执行时间1.000
    work1执行时间2.009
    p1.is_alive()=False'''
    print("p1.is_alive()=%s" % p1.is_alive())



