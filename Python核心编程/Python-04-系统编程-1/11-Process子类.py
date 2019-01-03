from multiprocessing import Process
import os
import time

class Process_class(Process):
    def __init__(self,interval):
        Process.__init__(self)
        self.interval = interval

    #重写Process的run方法
    def run(self):
        print("父进程(%s),子进程(%s)开始执行"%(os.getppid(),os.getpid()))
        t_startTime = time.time()
        time.sleep(self.interval)
        t_endTime = time.time()
        print("%s执行结束，耗时%0.3f"%(os.getpid(),(t_endTime - t_startTime)))

if __name__ == "__main__":
    t_startTime = time.time()
    print("当前程序进程(%s)"%os.getpid())
    p1 = Process_class(2)
    p1.start()
    p1.join()
    t_endTime = time.time()
    print("%s执行结束，耗时%0.3f"%(os.getpid(),(t_endTime - t_startTime)))

'''当前程序进程(110160)
父进程(110160),子进程(208004)开始执行
208004执行结束，耗时2.001
110160执行结束，耗时3.016'''

